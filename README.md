# 7-Segment Display Control with Raspberry Pi

A Python script to cycle through digits 0-9 on a common cathode 7-segment display using a Raspberry Pi.

## Hardware Requirements
- Raspberry Pi (any model with GPIO pins)
- Common cathode 7-segment display
- 7x 220-330Ω resistors (for current limiting)
- Breadboard and jumper wires

## Wiring Instructions
Connect the 7-segment display to the Raspberry Pi GPIO pins (BCM numbering) as follows:

<table>
  <tr>
    <th>GPIO</th>
    <th>segment</th>
  </tr>
  <tr>
    <td>13</td>
    <td>a</td>
  </tr>
  <tr>
    <td>6</td>
    <td>b</td>
  </tr>
  <tr>
    <td>20</td>
    <td>c</td>
  </tr>
  <tr>
    <td>21</td>
    <td>d</td>
  </tr>
  <tr>
    <td>16</td>
    <td>e</td>
  </tr>
  <tr>
    <td>19</td>
    <td>i</td>
  </tr>
    <tr>
    <td>26</td>
    <td>g</td>
  </tr>
</table>

- Connect the **common cathode (GND)** pin of the display to a ground (GND) pin on the Raspberry Pi.
- Add a current-limiting resistor (220-330Ω) between each segment pin and the GPIO pins.

## Installation
1. Ensure the Raspberry Pi is set up and the GPIO interface is enabled.
2. Install the `RPi.GPIO` library (if not already installed):
   ```bash
   pip install RPi.GPIO





