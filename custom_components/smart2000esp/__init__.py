"""Smart Boat 2000 ESP Integration."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
import logging

DOMAIN = "smart2000esp"

_LOGGER = logging.getLogger(__name__)

async def update_listener(hass: HomeAssistant, entry: ConfigEntry):
    """Handle options update."""
    _LOGGER.info("Options for Smart2000ESP have been updated - applying changes")
    # Reload the integration to apply changes
    await hass.config_entries.async_reload(entry.entry_id)


async def async_setup(hass: HomeAssistant, config: dict):
    _LOGGER.info("Setting up Smart2000ESP integration")
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    _LOGGER.info("Setting up Smart2000ESP integration entry: %s", entry.as_dict())
    hass.data.setdefault(DOMAIN, {})

    # Register the update listener
    entry.async_on_unload(entry.add_update_listener(update_listener))

    hass.data[DOMAIN][entry.entry_id] = entry.data
    # Forward the setup to the sensor platform
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    _LOGGER.info("Smart2000ESP entry setup completed successfully and update listener registered")
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    _LOGGER.info("Unloading Smart2000ESP integration entry: %s", entry.as_dict())
    hass.data[DOMAIN].pop(entry.entry_id)
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    _LOGGER.info("Smart2000ESP entry unloaded successfully")
    return True

