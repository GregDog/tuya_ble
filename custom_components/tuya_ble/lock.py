"""Lock platform for Tuya BLE integration."""
from __future__ import annotations
from dataclasses import dataclass
import logging
from typing import Any

from homeassistant.components.lock import LockEntity, LockEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN
from .devices import TuyaBLEData, TuyaBLEEntity, TuyaBLEProductInfo
from .tuya_ble import TuyaBLEDataPointType, TuyaBLEDevice

_LOGGER = logging.getLogger(__name__)

@dataclass
class TuyaBLELockMapping:
    dp_id: int
    description: LockEntityDescription
    force_add: bool = True
    dp_type: TuyaBLEDataPointType | None = None

# Mapping for jtmspro/wwbdbt3h
mapping: dict[str, dict[str, TuyaBLELockMapping]] = {
    "jtmspro": {
        "wwbdbt3h": TuyaBLELockMapping(
            dp_id=47,
            description=LockEntityDescription(
                key="lock_motor_state",
                name="Lock Motor State",
                icon="mdi:lock"
            ),
        ),
    },
}

def get_mapping_by_device(device: TuyaBLEDevice) -> TuyaBLELockMapping | None:
    category = mapping.get(device.category)
    if category is not None:
        return category.get(device.product_id)
    return None

class TuyaBLELock(TuyaBLEEntity, LockEntity):
    """Representation of a Tuya BLE Lock."""

    def __init__(
        self,
        hass: HomeAssistant,
        coordinator: DataUpdateCoordinator,
        device: TuyaBLEDevice,
        product: TuyaBLEProductInfo,
        mapping: TuyaBLELockMapping,
    ) -> None:
        super().__init__(hass, coordinator, device, product, mapping.description)
        self._mapping = mapping

    @property
    def is_locked(self) -> bool:
        """Return true if lock is locked."""
        datapoint = self._device.datapoints[self._mapping.dp_id]
        if datapoint:
            # Invert the value: True means unlocked, False means locked
            return not bool(datapoint.value)
        return False

    def lock(self, **kwargs: Any) -> None:
        """Lock the device."""
        # Special logic for mqc2hevy and jtmspro/wwbdbt3h: lock is dp_id 46, bool True
        if self._device.product_id in ("mqc2hevy", "wwbdbt3h"):
            datapoint = self._device.datapoints.get_or_create(
                46,
                TuyaBLEDataPointType.DT_BOOL,
                True,
            )
            if datapoint:
                self._hass.create_task(datapoint.set_value(True))
        else:
            datapoint = self._device.datapoints.get_or_create(
                self._mapping.dp_id,
                TuyaBLEDataPointType.DT_BOOL,
                False,
            )
            if datapoint:
                self._hass.create_task(datapoint.set_value(False))

    def unlock(self, **kwargs: Any) -> None:
        """Unlock the device."""
        # Special logic for mqc2hevy and jtmspro/wwbdbt3h: unlock is dp_id 6, raw AQE=
        if self._device.product_id in ("mqc2hevy", "wwbdbt3h"):
            import base64
            raw_value = base64.b64decode("AQE=")
            datapoint = self._device.datapoints.get_or_create(
                6,
                TuyaBLEDataPointType.DT_RAW,
                raw_value,
            )
            if datapoint:
                self._hass.create_task(datapoint.set_value(raw_value))
        else:
            datapoint = self._device.datapoints.get_or_create(
                self._mapping.dp_id,
                TuyaBLEDataPointType.DT_BOOL,
                True,
            )
            if datapoint:
                self._hass.create_task(datapoint.set_value(True))

    @property
    def available(self) -> bool:
        return super().available

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Tuya BLE lock entity."""
    data: TuyaBLEData = hass.data[DOMAIN][entry.entry_id]
    mapping = get_mapping_by_device(data.device)
    if mapping:
        entity = TuyaBLELock(
            hass,
            data.coordinator,
            data.device,
            data.product,
            mapping,
        )
        async_add_entities([entity])
