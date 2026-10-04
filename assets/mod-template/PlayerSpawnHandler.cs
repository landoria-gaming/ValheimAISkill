using BepInEx.Logging;

namespace ValheimMod
{
    // Shows a configurable greeting when the local player first spawns.
    internal sealed class PlayerSpawnHandler
    {
        private readonly ModConfigFile _config;
        private readonly ManualLogSource _logger;

        // Receives the settings and plugin log.
        public PlayerSpawnHandler(ModConfigFile config, ManualLogSource logger)
        {
            _config = config;
            _logger = logger;
        }

        // Adds a local chat message without replacing the game's arrival message.
        public void OnPlayerInitialSpawn()
        {
            if (!_config.Enabled.Value)
            {
                return;
            }

            if (Chat.instance == null)
            {
                _logger.LogWarning("Chat is not available at first spawn.");
                return;
            }

            Chat.instance.AddString(_config.Greeting.Value);
        }
    }
}
