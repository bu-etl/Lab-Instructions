# TFPX-202 Test 1x2 CROC Module

`Introduction Placeholder`

## Required Materials

1x2 CROC Module, 1x2 Probe Card, ADC Board, Coldbox, Dry Air, Chiller, Test Stand PC,  

## Procedure

```
Install Module in Cold Box

Cool and Dry the Box

Run tests

Upload test results

Warm up box & remove module
```

### Step 1: Install Module in Cold Box

1. Gather the module and probe card from the dry air cabinent in the clean room. Be carful not to damage the pins on the probe card as you carry it to the test stand.
2. Ensure the valve connecting the coolant line to the coldbox is closed **[include picture of closed state]**. Begin cooling the coolant in the chiller. Turn the chiller on using the red button on the chiller. Using the dial, highlight temperature, and press the dial in to select. Using the dial, select 5.0 degrees Celsius as the setpoint. Press the dial to select. Select the power button in the top-right corner using the dial and press to start chilling the coolant **[need pictures of all these steps]**.
3. Ensure the Keysight E3633A low voltage supply, Keithley 2470 high voltage supply, FC7, and coldbox electronics box are powered off. There's no power button on the coldbox electronics box. Simply unplug it from the wall.
4. Remove the coldbox lid. Place the module on top of the coldplate, ensuring the screw holes on the module carrier and coldplate align. Using a 5/64" hex key (AKA Allen wrench), secure the module to the coldplate using the screw **[what kind of screw?]**. Do NOT overtighten the screw; it is okay if the module carrier can rotate slightly.
5. Place the probe card on top of the module, ensuring the probe card pins align with the pin holes on the module cover. Be careful not to bend the pins. The probe card pins should drop into the module cover with zero resistance. You should not apply any force in placing the probe card on the module.
6. Secure the probe card to the module cover using a 1/16" hex key (Allen wrench) and the screws **[what kind of screws?]**. Do not overtighten the screws.
7. Connect the ADC board to the probe card **[picture needed]**.
8. Connect the ADC board to the test stand PC using the micro-USB cable running through the side of the coldbox **[picture needed]**. There are 2 micro-USB ports on the ADC board. Connect the micro-USB cable to the port closest to you when the ports face left.
9. Connect the module to the Keysight E3633A low voltage supply using the 4-pin molex connector **[picture of molex needed]**. The clip on the male end must face up. The connector only goes in this way.
10. Connect the module to the Keithley 2470 high voltage supply using the MCX connector **[picture needed]**.
11. Connect the moduel to the FC7 using the micro-HDMI connector **[picutre needed]**.
12. Place the coldbox lid onto the coldbox. Secure the lid with a Phillips-head screwdriver and the 6 screws **[what kind of screws?]**. Tighten the screws in such an order as to spread out the force over the entire lid evenly as you secure it **[This doesn't make any sense, re-explain]**.

### Step 2: Cool and Dry the Coldbox

1. Turn on the Keysight E3633A low voltage supply, Keithley 2470 high voltage supply, FC7, and plug in the coldbox electronics box.
2. Launch Ph2_ACF_GUI ("OSU GUI") from the command line on the test stand PC:

    ```bash
    cd ~/Ph2_ACF_GUI **[check this is the dir name]**
    bash run_docker.sh
    ```

3. When the login screen appears, enter your Panthera credentials and click "Login".



### Etc.
