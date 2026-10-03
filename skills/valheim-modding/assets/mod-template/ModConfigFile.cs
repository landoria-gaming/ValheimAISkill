using BepInEx.Configuration;

namespace ValheimMod
{
    // Holds the BepInEx settings used by this mod.
    internal sealed class ModConfigFile
    {
        public ConfigEntry<bool> Enabled { get; }
        public ConfigEntry<string> Greeting { get; }

        // Binds the feature settings and their default values.
        public ModConfigFile(ConfigFile config)
        {
            Enabled = config.Bind("General", "Enabled", true, "Show the greeting on first spawn.");
            Greeting = config.Bind("General", "Greeting", "Hello World", "Local chat message on first spawn.");
        }
    }
}
