# Tuya BLE

A custom integration for Home Assistant to support Tuya BLE (Bluetooth Low Energy) devices natively.

## Features
- Local control of Tuya BLE smart locks, sensors, and more
- No cloud dependency
- Supports auto lock, lock volume, and other advanced features

## Installation (via HACS)
1. Go to HACS > Integrations > Custom repositories
2. Add this repository URL as a custom repository (category: Integration)
3. Search for "Tuya BLE" in HACS and install
4. Restart Home Assistant

## Manual Installation
Copy the `tuya_ble` folder to your Home Assistant `custom_components` directory.

## Configuration
- Add and configure your Tuya BLE devices via the Home Assistant UI (Integrations > Add Integration > Tuya BLE)

## Credits
- Forked and adapted from [Eugene-Musika/ha_tuya_ble](https://github.com/Eugene-Musika/ha_tuya_ble)
- Inspired by and based on [PlusPlus-ua/ha_tuya_ble](https://github.com/PlusPlus-ua/ha_tuya_ble)

## License
MIT 