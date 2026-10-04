// Run only in an isolated Unity Editor test project, never in a game or mod.
using System;
using System.IO;
using System.Linq;
using UnityEditor;
using UnityEngine;
using UnityEngine.Rendering;

public static class ModelExportValidation
{
    public static void Run()
    {
        try
        {
            string package = Environment.GetEnvironmentVariable("VALHEIM_MODEL_PACKAGE");
            AssetDatabase.importPackageCompleted += OnImported;
            AssetDatabase.importPackageFailed += (name, message) => Fail(new Exception(message));
            AssetDatabase.importPackageCancelled += name => Fail(new Exception("Package import cancelled"));
            AssetDatabase.ImportPackage(package, false);
        }
        catch (Exception error) { Fail(error); }
    }

    private static void OnImported(string package)
    {
        AssetDatabase.importPackageCompleted -= OnImported;
        EditorApplication.delayCall += Validate;
    }

    private static void Validate()
    {
        try
        {
            string report = Environment.GetEnvironmentVariable("VALHEIM_MODEL_REPORT");
            AssetDatabase.Refresh(ImportAssetOptions.ForceSynchronousImport);
            string[] prefabs = AssetDatabase.FindAssets("t:Prefab", new[] { "Assets/ValheimModels" });
            if (prefabs.Length != 1) throw new Exception("Expected one prefab");
            var asset = AssetDatabase.LoadAssetAtPath<GameObject>(AssetDatabase.GUIDToAssetPath(prefabs[0]));
            var instance = (GameObject)PrefabUtility.InstantiatePrefab(asset);
            int vertices = 0;
            foreach (Transform transform in instance.GetComponentsInChildren<Transform>(true))
            {
                if (GameObjectUtility.GetMonoBehavioursWithMissingScriptCount(transform.gameObject) != 0)
                    throw new Exception("Missing component scripts");
            }
            if (instance.GetComponentsInChildren<MonoBehaviour>(true).Length != 0)
                throw new Exception("Unexpected gameplay script");
            foreach (MeshFilter filter in instance.GetComponentsInChildren<MeshFilter>(true))
            {
                Mesh mesh = filter.sharedMesh;
                if (mesh == null || mesh.vertexCount == 0 || mesh.subMeshCount == 0)
                    throw new Exception("Missing or empty mesh");
                vertices += mesh.vertexCount;
            }
            Renderer[] renderers = instance.GetComponentsInChildren<Renderer>(true);
            foreach (Renderer renderer in renderers)
            {
                foreach (Material material in renderer.sharedMaterials)
                {
                    if (material == null || material.shader == null || ShaderUtil.ShaderHasError(material.shader))
                        throw new Exception("Missing or broken material/shader");
                    // A color-only material is allowed, but an unresolved texture reference is not.
                    var serialized = new SerializedObject(material);
                    var property = serialized.GetIterator();
                    while (property.Next(true))
                    {
                        if (property.propertyType == SerializedPropertyType.ObjectReference &&
                            property.objectReferenceValue == null)
                        {
                            // Unity 6.5 replaced instance IDs with entity IDs.
                            var idProperty = typeof(SerializedProperty).GetProperty("objectReferenceEntityIdValue") ??
                                             typeof(SerializedProperty).GetProperty("objectReferenceInstanceIDValue");
                            object id = idProperty.GetValue(property);
                            if (!id.Equals(Activator.CreateInstance(id.GetType())))
                                throw new Exception("Broken material reference: " + property.propertyPath);
                        }
                    }
                }
            }
            Renderer[] active = renderers.Where(r => r.enabled && r.gameObject.activeInHierarchy).ToArray();
            if (active.Length == 0) throw new Exception("No visible model renderer");
            var bounds = active[0].bounds;
            foreach (var renderer in active.Skip(1)) bounds.Encapsulate(renderer.bounds);
            if (bounds.size.sqrMagnitude < 0.0001f) throw new Exception("Empty bounds");
            var light = new GameObject("Validation light").AddComponent<Light>();
            light.type = LightType.Directional;
            light.intensity = 1.4f;
            light.transform.rotation = Quaternion.Euler(35, -35, 0);
            RenderSettings.ambientMode = AmbientMode.Flat;
            RenderSettings.ambientLight = new Color(0.5f, 0.5f, 0.5f);
            var camera = new GameObject("Validation camera").AddComponent<Camera>();
            camera.clearFlags = CameraClearFlags.SolidColor;
            camera.backgroundColor = new Color(0.18f, 0.2f, 0.24f);
            float radius = bounds.extents.magnitude;
            camera.transform.position = bounds.center + new Vector3(1, 0.65f, -1).normalized * radius * 3.5f;
            camera.transform.LookAt(bounds.center);
            camera.nearClipPlane = 0.01f;
            camera.farClipPlane = radius * 20;
            var target = new RenderTexture(768, 768, 24);
            camera.targetTexture = target;
            camera.Render();
            RenderTexture.active = target;
            var image = new Texture2D(768, 768, TextureFormat.RGB24, false);
            image.ReadPixels(new Rect(0, 0, 768, 768), 0, 0);
            image.Apply();
            File.WriteAllBytes(Path.ChangeExtension(report, ".png"), image.EncodeToPNG());
            File.WriteAllText(report, JsonUtility.ToJson(new Result {
                unityVersion = Application.unityVersion, renderers = renderers.Length,
                activeRenderers = active.Length, vertexInstances = vertices,
                textures = AssetDatabase.FindAssets("t:Texture2D", new[] { "Assets/ValheimModels" }).Length,
                bounds = bounds.size.ToString("F3"), imported = true
            }, true));
            EditorApplication.Exit(0);
        }
        catch (Exception error) { Fail(error); }
    }

    private static void Fail(Exception error)
    {
        Debug.LogException(error);
        EditorApplication.Exit(1);
    }

    [Serializable]
    private class Result
    {
        public string unityVersion;
        public bool imported;
        public int renderers, activeRenderers, vertexInstances, textures;
        public string bounds;
    }
}
