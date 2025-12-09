# UART → OLED Display Example (Raspberry Pi Pico)

This project is a **simple demonstration** showing how to read data from the UART interface on a **Raspberry Pi Pico** and display the received text on a **128×32 I²C OLED display**.

---

## Hardware Setup

### Raspberry Pi Pico UART (UART0)

| Signal | Pin |
|--------|-----|
| **RX** | GP5 |
| **TX** | GP4 |

### Raspberry Pi Pico I²C (I2C0)

| Signal | Pin |
|--------|-----|
| **SDA** | GP0 |
| **SCL** | GP1 |

### OLED Display
- Resolution: **128×32**
- Interface: **I²C**
- Typical address: `0x3C`

---

## Description

This example reads incoming UART data and immediately displays it on the OLED.  
Useful for debugging serial data or creating simple text-based UIs.



