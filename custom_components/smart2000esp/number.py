"""Number entities for Smart2000ESP."""
from __future__ import annotations

from datetime import timedelta
import logging

from homeassistant.components.number import NumberEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity

from . import (
    DEFAULT_UPDATE_INTERVAL_SECONDS,
    MAX_UPDATE_INTERVAL_SECONDS,
    MIN_UPDATE_INTERVAL_SECONDS,
    SIGNAL_UPDATE_INTERVAL_CHANGED,
    async_set_update_interval,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Smart2000ESP number entities."""
    async_add_entities([Smart2000ESPUpdateIntervalNumber(hass, entry)], True)


class Smart2000ESPUpdateIntervalNumber(NumberEntity, RestoreEntity):
    """A number entity to show and change the Smart2000ESP update interval."""

    _attr_has_entity_name = True
    _attr_name = "Update interval"
    _attr_icon = "mdi:timer-outline"
    _attr_native_min_value = MIN_UPDATE_INTERVAL_SECONDS
    _attr_native_max_value = MAX_UPDATE_INTERVAL_SECONDS
    _attr_native_step = 0.1
    _attr_native_unit_of_measurement = "s"

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        self.hass = hass
        self.entry = entry
        self._attr_unique_id = f"{entry.entry_id}_update_interval"
        self._attr_device_info = {
            "identifiers": {(entry.domain, entry.entry_id)},
            "name": entry.title,
        }
        self._unsub_dispatcher = None
        self._native_value: float | None = None

    @property
    def native_value(self) -> float | None:
        return self._native_value

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()

        # Restore last state if available
        last_state = await self.async_get_last_state()
        if last_state is not None and last_state.state not in ("unknown", "unavailable"):
            try:
                self._native_value = float(last_state.state)
            except ValueError:
                self._native_value = None

        # If we can read a current interval from hass.data, prefer that
        name = self.entry.data.get("name")
        if name:
            key = f"{name}_smart2000timestamp_key"
            data = self.hass.data.get(key)
            if data and "min_interval" in data:
                mi = data["min_interval"]
                if isinstance(mi, timedelta):
                    self._native_value = mi.total_seconds()

        if self._native_value is None:
            self._native_value = DEFAULT_UPDATE_INTERVAL_SECONDS

        # Listen for interval changes
        self._unsub_dispatcher = async_dispatcher_connect(
            self.hass,
            f"{SIGNAL_UPDATE_INTERVAL_CHANGED}_{self.entry.entry_id}",
            self._handle_interval_changed,
        )

    async def async_will_remove_from_hass(self) -> None:
        if self._unsub_dispatcher is not None:
            self._unsub_dispatcher()
            self._unsub_dispatcher = None
        await super().async_will_remove_from_hass()

    def _handle_interval_changed(self) -> None:
        name = self.entry.data.get("name")
        if name:
            key = f"{name}_smart2000timestamp_key"
            data = self.hass.data.get(key)
            if data and "min_interval" in data:
                mi = data["min_interval"]
                if isinstance(mi, timedelta):
                    self._native_value = mi.total_seconds()
                    self.async_write_ha_state()
                    return

        # Fallback to stored last value
        seconds = self.hass.data.get(self.entry.domain, {}).get("update_interval_seconds")
        if seconds is not None:
            self._native_value = float(seconds)
            self.async_write_ha_state()

    async def async_set_native_value(self, value: float) -> None:
        """Update the interval."""
        seconds = float(value)
        await async_set_update_interval(self.hass, seconds)
        self._native_value = seconds
        self.async_write_ha_state()