# TFPX-103 CROC 1x2 Module Wirebonding

`Introduction Placeholder`

## Required Materials

- Glued module (with spacer) screwed to assembly carrier
- TFPX 1x2 Module Wirebonding Plate
- Equipment
    - Hesse BJ855 Automatic Wirebonder
    - Microscope
    - USB Thumb Drive

## Procedure

**Caleb: Possibly add a "Step 0" with some preflight checks for the bonder. E.g. check the bond head and wire in the E-box and perform a small number of manual bonds on a test coupon** 

### Step 1: Stage module

Slide the module carrier on which the glued module is screwed in into the TFPX 1x2 Module Wirebonding Plate. Unlock the wirebonder window by turning the "A-Mode" key, and place the fixture onto the vacuum chuck. Orient the fixture so the wirebond pad side of the module is the side closest to you. Push the fixture corner into the sets of pegs to make alignment easier. Slide the wirebonder window back up and press the "CLAMP" button on the keypad to turn the vacuum on. You must be logged in to turn on the clamp. You can check that the clamp is on by looking at the clamp status icon at the top of the screen. Below is a picture of what the icon should look like.

|Clamp off|Clamp on|
|-|-|
|INSERT CLAMP OFF ICON|INSERT CLAMP ON ICON|

### Step 2: Load program

Click the folder icon in the top left to load a bond program. Navigate to the desired program, currently named `TFPX_CROC_1x2_SensorModule_WireClasses`.

### Step 3: Define frames

Navigate to the "Define units" tab. Click on the HDI object in the "Aufnahme" drop down. Move the camera to the bottom left corner of the HDI using the red camera joystick.

INSERT PICTURE OF CORRECT LOCATION

Once the crosshair is on the bottom left corner of the HDI, click the "Define origin" button on the left panel. It is important that the HDI object is selected when you click this button so the settings are saved properly. Next, adjust the focus (up and down arrows to the right of the red joystick) and lighting (slide bar to the left of the red joystick) until the HDI bondpads are in focus and reasonably bright. Then, click the "Define focus and lighting" button on the left panel. 

Repeat this process with the SRA by clicking the SRA object in the drop down. Like the HDI, navigate to the bottom left corner of the SRA and click the "Define origin" button. Then, adjust the focus and lighting and click the "Define focus and lighting" button.

### Step 4: Perform alignment

Click the CROC_1x2_Sensor_Module object in the "Aufnahme" drop down and then click the "Start alignment button" on the left. It is this small icon:

|Start alignment button|
|-|
|INSERT PICTURE CIRCLING START ALIGNMENT BUTTON|

The wirebonder will then quickly align the two parts, and will calculate where the bond feet should be. If the yellow lines representing the wires are not visible, enable this using a button on the right side of the camera panel:

|Wire visibility button(s)|
|-|
|INSERT PICTURE CIRCLING WIRE VISIBILITY BUTTON|

If one of the two sets of bond feet are systematically misaligned (e.g. consistently too far to the left side of the bond pads), you can retry the alignment for that part by clicking that object in the drop down and clicking the start alignment button. Once most of the bond feet look good and centered on the pads, you can now adjust any single bond feet that are still not properly centered on their respective bond pads. This can be done by navigating to the "Optimization" tab, entering correction mode by clicking the "Correction" button on the left panel, and dragging the bond feet in the camera window to the desired location. Double check all bond feet on both components are centered well enough. Exit correction mode by clicking the "Correction" button again. 

### Step 5: Bond HDI/SRA wires

Still in the "Optimization tab," click the HDI object in the drop down and click the "Detect touch down" on the left panel. It should now touch down on the first bond pad on both the HDI and SRA to calibrate the height. After it's done, it should be hovering over wire 9 (which is first in the bond order). Note the wire numbers do not correspond to the actual bond order. Make sure the deformation graph is cleared out, which can be done by navigating to the graph tab on the left panel of the camera and clicking the "Clear all process curves" button:

|Deformation data tab|
|-|
|INSERT RELEVANT IMAGE|

You can now start the bonding by clicking the "All wires (Start)" button on the left panel. The bottom camera tab provides the best angle for watching the bonding. Wait for the bonding to complete, and then look over the bonds.

If any bonds are missing, you can retry individual wires by selecting the wire you wish to redo (something like W50 in the bottom left drop down), right-clicking it, and resetting its state. To make sure it does the correct wire, make sure this input box has the correct wire number:

|Wire input box|
|-|
|INSERT IMAGE|

You can now press "Detect touch down" and then "Single wire."

### Step 6: Export deformation data

Navigate back to the deformation data tab and click the "Save process curves" button (see below), and save the file to a flash drive. It will save as a .btd file, which can be parsed with a script. Alternatively, take a screenshot of the deformation graph and save that. After saving the data, you can now clear the process curves.

### Step 7: Repeat steps 3-6 for the second chip on the module

This step is self-explanatory, just make sure to reset the state of all wires and ensure that wire 9 will be the first one bonded. 

### Step 8: Bond specialty wires manually

Apart from the main wirebonds between the HDI and SRA, there are three sets of wirebonds you must do manually: the bias wires, pull-test wires, and trim bit wires. To enter manual bonding mode, click the "Fn2" button on the keypad and press "OK."

To define a wire in manual bonding mode, click the "Define wires..." button and input the correct dimensions, orientation, quantity, and offset for the set of wires you wish to place. Exit the window by clicking "Finish." Define the location of the first bond foot by clicking the "Define position" button and clicking where you want the first bond foot. If it looks like the bond feet are correctly located, you may click "Detect TD" followed by clicking "Bond all" to bond the wires (or click "Single wire" repeatedly if you wish to do them one at a time).

To do the trim bit wires, you must first figure out what the correct configuration of wires is (this changes from module to module). This information can be found on the [Purdue DB](https://www.physics.purdue.edu/cmsfpix/Phase2_Test/login.php?) entry for the module you are assembling. See this example.

|Purdue DB Entry|
|-|
|![Purdue DB](./images/PurdueDB.png)|

The left image at the bottom will be the pads you are looking for on the left side of the module, and the right image are the pads you are looking for on the right side of the module. Make sure that you refer to the correct image when bonding these wires. Once you find the pads, bond vertical wires where the image has a red line, skipping the pads where the image has a gray line.

For the locations of the pull test and bias wires, refer to this image where the pull test is the lower left blue circle and the bias is the upper right blue circle:

|Pull test and bias wires|
|-|
|![Pull test/bias](./images/pulltest_bias.png)|

### Step 9: Inspect and image wirebonds

Once you are ready to remove the module from the wirebonder, press "Clamp" to turn off the vacuum (this should also unlock the window), and pick up the module carrier. Take it over to a microscope and inspect the wirebonds, making sure there are wires everywhere there should be. Take and save pictures of the wires for both chips, along with the trim bit, bias, and pull test wires. 

|Left Chip Wires, Left Chip Trim Bits, & Pull Test Wires|Right Chip Wires and Right Trim Bits|Bias Wires|
|-|-|-|
|![leftchip](./images/left_wires_trimbits_pulltest.png)|![rightchip](./images/right_wires_trimbits.png)|![biaswires](./images/biaswires.png)|

### Step 10: Update Purdue DB

Log into the Purdue database ([login page](https://www.physics.purdue.edu/cmsfpix/Phase2_Test/main.php)) and login. Here's what to do from there:

1. Click the "Inspect part (read/write)" button
2. Type in the serial number of the module you're assembling into the "Serial #" field (e.g. RH0136)
3. Click the search button (pressing enter won't work)
4. Click the "Edit" button on the left side of the module's entry
5. Click the "Status" dropdown and change it to "Wirebonded"
6. Click the "Update" button


### Next steps

You can now put the module into it's module testing carrier, or put it into the dry air cabinet until you are ready to do so.
