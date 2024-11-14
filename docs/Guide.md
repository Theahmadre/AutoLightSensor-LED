## Wiring Guide for LDR and LED Circuit with Raspberry Pi

This guide will walk you through how to wire the **LDR** (Light Dependent Resistor) and **LED** circuit to a **Raspberry Pi** using a **10µF capacitor**. Follow these steps to set up your circuit correctly.

## Components Required:
- 1 x Raspberry Pi (any model with GPIO pins)
- 1 x LDR (Light Dependent Resistor)
- 1 x LED (Light Emitting Diode)
- 1 x 10kΩ Resistor
- 1 x 330Ω Resistor (for LED current limiting)
- 1 x 10µF Capacitor
- Jumper wires
- Breadboard

## Wiring Steps:

### LDR and Capacitor Circuit:
1. **LDR**: Place the LDR on the breadboard.
   - **One leg of the LDR** connects to **GPIO Pin 17** (or the GPIO pin you choose on the Raspberry Pi).
   - **The other leg** of the LDR connects to the **positive leg (anode)** of the **10µF Capacitor**.

2. **Capacitor**: 
   - The **negative leg (cathode)** of the **10µF Capacitor** connects to one side of the **10kΩ Resistor**.
   - The **other side** of the **10kΩ Resistor** connects to **Ground (GND)**.

3. **GPIO Pin 17**: 
   - The **junction between the LDR and Capacitor** (where the two components meet) should be connected to **GPIO Pin 17** (to read the voltage level).

4. **Resistor (10kΩ)**: 
   - Place the **10kΩ Resistor** between the **capacitor's cathode** and **Ground (GND)**. This resistor pulls the voltage level to ground when it's dark.

### LED Circuit:
1. **LED**: Place the LED on the breadboard.
   - **Anode (long leg)** of the LED connects to **GPIO Pin 6** (or the GPIO pin you want to use to control the LED).
   - **Cathode (short leg)** of the LED connects to **Ground (GND)**.

2. **Current-Limiting Resistor (330Ω)**:
   - Place a **330Ω Resistor** between **GPIO Pin 6** and the **Anode (long leg)** of the LED. This resistor limits the current flowing through the LED to prevent damage.

### Circuit Summary:
- **LDR to GPIO Pin 17** and connected to the **Capacitor (10µF)**.
- **Capacitor's negative leg** goes to a **10kΩ Resistor**, which then connects to **Ground (GND)**.
- **LED connected to GPIO Pin 6** through a **330Ω Resistor**.
- **LED's cathode** goes to **Ground (GND)**.

---

## Circuit Diagram:
For a visual representation of this circuit, check the **circuit diagram** in the `docs/` folder of this project.

## Notes:
- Make sure to use the correct GPIO pins and adjust the pin numbers in the code if you change the wiring.
- The **LDR** will vary its resistance based on the ambient light, which will affect the voltage at the GPIO pin connected to it.
- The **10µF Capacitor** smooths the readings of the LDR, allowing for more accurate light level detection.
- The **330Ω Resistor** ensures that the **LED** doesn't burn out by limiting the current.
