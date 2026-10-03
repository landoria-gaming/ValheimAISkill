using BepInEx;

namespace ValheimMod
{
    // Owns the plugin metadata and game lifecycle subscriptions.
    [BepInPlugin(PluginGuid, PluginName, PluginVersion)]
    public sealed class Plugin : BaseUnityPlugin
    {
        public const string PluginGuid = "example.valheimmod";
        public const string PluginName = "ValheimMod";
        public const string PluginVersion = "0.1.0";
        private PlayerSpawnHandler _spawnHandler;

        // Creates the feature and listens for the first local player spawn.
        private void Awake()
        {
            var config = new ModConfigFile(Config);
            _spawnHandler = new PlayerSpawnHandler(config, Logger);
            Game.m_playerInitialSpawn += _spawnHandler.OnPlayerInitialSpawn;
            Logger.LogInfo($"{PluginName} {PluginVersion} loaded.");
        }

        // Removes this plugin's subscription when it is destroyed.
        private void OnDestroy()
        {
            if (_spawnHandler != null)
            {
                Game.m_playerInitialSpawn -= _spawnHandler.OnPlayerInitialSpawn;
            }
        }
    }
}
