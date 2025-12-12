# TFPX-102 Spacer Installation

`Introduction Placeholder`

## Required Materials

- Glued module
- Spacer
- Gluing materials
    - Glue
    - Mixing nozzle
    - Stencil
    - Glue spreader (e.g. plastic card)

## Procedure

### Step 1: Stage parts

Place the module carrier on which the glued module is screwed in onto the desired chuck. Make sure the screws are on the right side of the chuck. 
1. Next, place the brass fixture with the pegs in the top left and bottom right corners on the HDI launch chuck. Place the spacer kapton tape side down in the desired slot (0, 1, 2, 3).

|Step 1|
|-|
|![Step 1](./images/spacer_step1.jpg)|

2. Then, place the stencil over the spacer, ensuring the orientation of the stencil is correct (horizontal line on top and larger vertical line on right). Put a mixing nozzle on the glue gun and deposit a line of glue below only the spacer you wish to glue. Do not put glue below empty holes. Then, slowly spread the glue upwards with the glue spreader.

|Step 2|
|-|
|![Step 2](./images/spacer_step2.jpg)|

3. Lift the stencil off the spacer, being careful that the spacer is not lifted with the stencil. If it is, carefully place it back in the desired location. Then, place the other brass fixture over the spacer, ensuring the orientation is correct (holes should be oriented the same as the stencil).

|Step 3|
|-|
|![Step 3](./images/spacer_step3.jpg)|

4. Pick up the brass sandwich and flip it about its long edge.

|Step 4|
|-|
|![Step 4](./images/spacer_step4.jpg)|

5. Remove the top brass piece, being careful that the spacer is not lifted with it. If the spacer is lifted, carefully place it back where it was.

|Step 5|
|-|
|![Step 5](./images/spacer_step5.jpg)|

### Step 2: Run installation script

You can now load the spacer installation script into the gScript Interpreter, which can be found at:

`./gantry-config-bu/Scripts/TFPXModules/Pre-production Scripts/Spacer_1x2_sensor.gscript`

Run the script and follow the prompts in the pop-ups. The spacer locations are labeled on the brass fixture (0, 1, 2, 3). Once the gantry places the spacer and completes the script, save the generated log file in the Logs directory (`./gantry-config-bu/Logs/`).

FIXME: Put a reference image in script for HDI fiducial measurements

### Step 3: Cure spacer

Let the spacer cure for at least 8 hours (FIXME if wrong). Place a note saying "DO NOT TOUCH, GLUE CURING" next to the module so no one unknowingly interferes with this process.

### Next steps

After the glue is cured, you can now transfer the module carrier to the wirebonding fixture to immediately begin the wirebonding process, or put the module carrier in the dry air cabinet until you are ready to begin wirebonding.