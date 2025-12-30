"""Smart Boat 2000 ESP Integration."""
from __future__ import annotations

from datetime import timedelta
import logging

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.dispatcher import async_dispatcher_send

DOMAIN = "smart2000esp"

_LOGGER = logging.getLogger(__name__)

DEFAULT_UPDATE_INTERVAL_SECONDS: float = 5.0
MIN_UPDATE_INTERVAL_SECONDS: float = 0.1
MAX_UPDATE_INTERVAL_SECONDS: float = 600.0

SERVICE_SET_UPDATE_INTERVAL = "set_update_interval"
SERVICE_FIELD_SECONDS = "seconds"

SIGNAL_UPDATE_INTERVAL_CHANGED = f"{DOMAIN}_update_interval_changed"

PLATFORMS: list[str] = ["sensor", "number"]


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the Smart2000ESP integration."""
    hass.data.setdefault(DOMAIN, {})

    async def _handle_set_update_interval(call: ServiceCall) -> None:
        raw = call.data.get(SERVICE_FIELD_SECONDS)

        # Leave empty to reset to default
        if raw is None:
            seconds = DEFAULT_UPDATE_INTERVAL_SECONDS
        else:
            seconds = float(raw)

        # Validate bounds
        if not (MIN_UPDATE_INTERVAL_SECONDS <= seconds <= MAX_UPDATE_INTERVAL_SECONDS):
            raise vol.Invalid(
                f"{SERVICE_FIELD_SECONDS} must be between {MIN_UPDATE_INTERVAL_SECONDS} and {MAX_UPDATE_INTERVAL_SECONDS}"
            )

        await async_set_update_interval(hass, seconds)

    hass.services.async_register(
        DOMAIN,
        SERVICE_SET_UPDATE_INTERVAL,
        _handle_set_update_interval,
        schema=vol.Schema(
            {
                vol.Optional(SERVICE_FIELD_SECONDS): vol.Coerce(float),
            }
        ),
    )

    return True


async def async_set_update_interval(hass: HomeAssistant, seconds: float) -> None:
    """Update the throttling interval used by Smart2000ESP at runtime."""
    # Store last chosen interval (for the update-interval entity to show immediately)
    hass.data.setdefault(DOMAIN, {})["update_interval_seconds"] = seconds

    for entry in hass.config_entries.async_entries(DOMAIN):
        name = entry.data.get("name")
        if not name:
            continue

        smart2000timestamp_key = f"{name}_smart2000timestamp_key"
        if smart2000timestamp_key not in hass.data:
            continue

        hass.data[smart2000timestamp_key]["min_interval"] = timedelta(seconds=seconds)

        # Notify any listeners (e.g., number entity) to refresh state
        async_dispatcher_send(hass, f"{SIGNAL_UPDATE_INTERVAL_CHANGED}_{entry.entry_id}")

    _LOGGER.debug("Smart2000ESP update interval set to %ss", seconds)


async def update_listener(hass: HomeAssistant, entry: ConfigEntry):
    """Handle options update."""
    _LOGGER.debug("Options for Smart2000ESP have been updated - applying changes")
    # Reload the integration to apply changes
    await hass.config_entries.async_reload(entry.entry_id)


...


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Smart2000ESP from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    entry.async_on_unload(entry.add_update_listener(update_listener))

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    _LOGGER.debug("Unloading Smart2000ESP integration entry: %s", entry.as_dict())
    hass.data.setdefault(DOMAIN, {}).pop(entry.entry_id, None)

    # Forward the unload to the sensor platform
    platforms = PLATFORMS
    _LOGGER.debug("Forwarding unload to platforms: %s", platforms)
    unload_ok = await hass.config_entries.async_unload_platforms(entry, platforms)
    _LOGGER.debug("Unload forwarded with result: %s", unload_ok)

    _LOGGER.debug("Smart2000ESP entry unloaded successfully")
    return True