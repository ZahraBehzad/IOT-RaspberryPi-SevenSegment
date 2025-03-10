# 7-Segment Display Control with Raspberry Pi

A Python script to cycle through digits 0-9 on a common cathode 7-segment display using a Raspberry Pi.

## Hardware Requirements
- Raspberry Pi (any model with GPIO pins)
- Common cathode 7-segment display
- 7x 220-330Ω resistors (for current limiting)
- Breadboard and jumper wires

## Wiring Instructions
Connect the 7-segment display to the Raspberry Pi GPIO pins (BCM numbering) as follows:

| Segment | GPIO Pin |
|---------|----------|
|   a     |    13    |
|   b     |    6     |
|   c     |    20    |
|   d     |    21    |
|   e     |    16    |
|   f     |    19    |
|   g     |    26    |

- Connect the **common cathode (GND)** pin of the display to a ground (GND) pin on the Raspberry Pi.
- Add a current-limiting resistor (220-330Ω) between each segment pin and the GPIO pins.

## Installation
1. Ensure the Raspberry Pi is set up and the GPIO interface is enabled.
2. Install the `RPi.GPIO` library (if not already installed):
   ```bash
   pip install RPi.GPIO




<table>
  <tr>
    <th>GPIO</th>
    <th>segment</th>
  </tr>
  <tr>
    <td>13</td>
    <td>a   1</td>
  </tr>
  <tr>
    <td>6</td>
    <td>b   2</td>
  </tr>
  <tr>
    <td>20</td>
    <td>c   4</td>
  </tr>
  <tr>
    <td>21</td>
    <td>d   8</td>
  </tr>
  <tr>
    <td>16</td>
    <td>e   10</td>
  </tr>
  <tr>
    <td>19</td>
    <td>i   20</td>
  </tr>
    <tr>
    <td>26</td>
    <td>g   40</td>
  </tr>
</table>
