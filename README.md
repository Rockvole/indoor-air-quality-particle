indoor-air-quality-particle
==============================

Collection of hardware and firmware for the Particle Photon - firmware sends data to the [indoor-air-quality-dashboard](https://github.com/Rockvole/indoor-air-quality-dashboard) project.

### Supported Sensors
|Sensor         |Type                                  |
|---------------|--------------------------------------|
|DHT22          |Temperature/Humidity                  |
|Shinyei PPD42NS|Dust Particles                        |
|Figaro TGS2600 |Carbon Monoxide and Air Contaminants) |
|Figaro TGS2602 |VOCs and Hydrogen Sulfide (Sewer Gas) |
|WSP2110        |Formaldehyde                          |

### Directories
|Directory           |Description                                                      |
|--------------------|-----------------------------------------------------------------|
|breadboard          |Diagram to make your own IAQ Monitor on a breadboard             |
|dht22               |Spark Core firmware for dht22 temperature / humidity sensor      |
|documentation       |Documentation regarding hardware recommendations for V2 of the indoor air quality shield      |
|firmware            |Particle Photon firmware supporting full suite of indoor air quality sensors |
|hardware            |Details about the indoor air quality shield hardware             |
|firmware-mini       |Particle Photon firmware supporting cut down hardware with TGS2602 & DHT22 only |
|firmware-oled       |Particle Photon firmware supporting TGS2602, DHT22 & IIC I2C 128X64 OLED LCD Display Module|
|firmware-oled-co    |Particle Photon firmware supporting TGS2600, DHT22 & IIC I2C 128X64 OLED LCD Display Module Arduino/STM32 |
|hardware-oled       |Details of the PCB hardware for the TGS2602, DHT22 & IIC I2C 128X64 OLED LCD Display Module Arduino/STM32 |
|hardware-case       |PCB Schematics and assembley photos of the final hardware in an off-the-shelf enclosure |
|libs                |firmware libraries for the sensors                               |
|sht15               |Particle Photon & Core firmware for sht15 temperature / humidity sensor      |

### History
<a href="https://community.particle.io/t/custom-shield-indoor-air-quality-monitor/121" title="Development evolution of the hardware"><img src="particle.png"/></a>
