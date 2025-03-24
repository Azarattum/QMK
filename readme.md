**This fork adds the following features:**
- [`5ed88f8`](https://github.com/Azarattum/QMK/commit/5ed88f8a4acf945db7158e2eeccd3a29430c2ed7): Full analog report to support [Wooting Analog SDK](https://github.com/WootingKb/wooting-analog-sdk) via [Universal Analog Plugin](https://github.com/AnalogSense/universal-analog-plugin) (based on [Analog Sense fork](https://github.com/AnalogSense/qmk_firmware/))
- [`ed360bd`](https://github.com/Azarattum/QMK/commit/ed360bdf7b452f4912c8364c7a357a872d21ee3d): `Fn+Esc` puts the keyboard in bootloader mode
- [`2e958f9`](https://github.com/Azarattum/QMK/commit/2e958f9c1072b94b0bc4b3ab71123c35f1487a09): Added full-length Bad Apple backlight animation ([yes, you heard it right](https://youtu.be/G8ZrETE6zp8))
- [`b80ff1f`](https://github.com/Azarattum/QMK/commit/b80ff1fdd85fe8d2eb7c604f02568b8adf5f949f): Added support for per-key RGB configuration with an extended version of [VIA's RGB protocol](https://github.com/the-via/app/blob/80dd7453a2f0a53233cd2c5bcc526847feb17e0e/src/utils/keyboard-api.ts#L372-L384). Full support with OpenRGB can be achieved with [ColorHoster](https://github.com/Azarattum/ColorHoster)

[All the changes](https://github.com/Keychron/qmk_firmware/compare/hall_effect_playground...Azarattum:QMK:hall_effect_custom) are based on [`hall_effect_playground` branch from Keychron](https://github.com/Keychron/qmk_firmware/tree/hall_effect_playground).

**Supported keyboards:**
- Lemokey P1 HE

> *The changes are quite portable, so you should be able to easily adapt them to your own keyboard.*

# Quantum Mechanical Keyboard Firmware

[![Current Version](https://img.shields.io/github/tag/qmk/qmk_firmware.svg)](https://github.com/qmk/qmk_firmware/tags)
[![Discord](https://img.shields.io/discord/440868230475677696.svg)](https://discord.gg/Uq7gcHh)
[![Docs Status](https://img.shields.io/badge/docs-ready-orange.svg)](https://docs.qmk.fm)
[![GitHub contributors](https://img.shields.io/github/contributors/qmk/qmk_firmware.svg)](https://github.com/qmk/qmk_firmware/pulse/monthly)
[![GitHub forks](https://img.shields.io/github/forks/qmk/qmk_firmware.svg?style=social&label=Fork)](https://github.com/qmk/qmk_firmware/)

This is a keyboard firmware based on the [tmk\_keyboard firmware](https://github.com/tmk/tmk_keyboard) with some useful features for Atmel AVR and ARM controllers, and more specifically, the [OLKB product line](https://olkb.com), the [ErgoDox EZ](https://ergodox-ez.com) keyboard, and the Clueboard product line.

## Documentation

* [See the official documentation on docs.qmk.fm](https://docs.qmk.fm)

The docs are powered by [Docsify](https://docsify.js.org/) and hosted on [GitHub](/docs/). They are also viewable offline; see [Previewing the Documentation](https://docs.qmk.fm/#/contributing?id=previewing-the-documentation) for more details.

You can request changes by making a fork and opening a [pull request](https://github.com/qmk/qmk_firmware/pulls), or by clicking the "Edit this page" link at the bottom of any page.

## Supported Keyboards

* [Planck](/keyboards/planck/)
* [Preonic](/keyboards/preonic/)
* [ErgoDox EZ](/keyboards/ergodox_ez/)
* [Clueboard](/keyboards/clueboard/)
* [Cluepad](/keyboards/clueboard/17/)
* [Atreus](/keyboards/atreus/)

The project also includes community support for [lots of other keyboards](/keyboards/).

## Maintainers

QMK is developed and maintained by Jack Humbert of OLKB with contributions from the community, and of course, [Hasu](https://github.com/tmk). The OLKB product firmwares are maintained by [Jack Humbert](https://github.com/jackhumbert), the Ergodox EZ by [ZSA Technology Labs](https://github.com/zsa), the Clueboard by [Zach White](https://github.com/skullydazed), and the Atreus by [Phil Hagelberg](https://github.com/technomancy).

## Official Website

[qmk.fm](https://qmk.fm) is the official website of QMK, where you can find links to this page, the documentation, and the keyboards supported by QMK.
