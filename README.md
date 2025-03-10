# 7-Segment Display Control with Raspberry Pi

This is a Python script to cycle through digits 0-9 on a 7-segment display using Raspberry Pi.

## Hardware Requirements
- Raspberry Pi 4 model B
- 7-segment display
- Breadboard and wires

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

![Example Image](https://drive.google.com/uc?id=[1V6INvQqwRdr_U_8Xs995vFQGCe7N8LEy])
## Installation
1. Ensure the Raspberry Pi is set up and the GPIO interface is enabled.
2. Install the `RPi.GPIO` library (if not already installed):
   ```bash
   pip install RPi.GPIO

![Example Image](https://drive.google.com/uc?id=[1V6INvQqwRdr_U_8Xs995vFQGCe7N8LEy])
> [!TIP]
> Guide to hexadecimal numbers used in code
![Example Image](https://drive.google.com/uc?id=[1V6INvQqwRdr_U_8Xs995vFQGCe7N8LEy])
