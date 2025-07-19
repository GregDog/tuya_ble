[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=flat-square)](https://hacs.xyz/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/gregd72002/tuya_ble?style=flat-square)](https://github.com/gregd72002/tuya_ble/issues)
[![GitHub stars](https://img.shields.io/github/stars/gregd72002/tuya_ble?style=flat-square)](https://github.com/gregd72002/tuya_ble/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/gregd72002/tuya_ble?style=flat-square)](https://github.com/gregd72002/tuya_ble/commits/main)

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