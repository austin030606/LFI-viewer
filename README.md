## Usage
After installing the required packages, simply use python to run the scripts.

`python find_parameters.py` is a tool for finding the parameters:
- p_width
- N
- offset
for a selected light field image.

killeroo recommended parameters:
- p_width = 15.397
- N = 519
- offset = 5

sanmiguel recommended parameters:
- p_width = 11.5487
- N = 519
- offset = 3

`python process_image.py` use the above parameters to construct and save light field images

It will output the light_field_d it decided to use.

`python refocus.y` refocuses using the light field images generated using `process_image.py` according to an input alpha_inv value range.

`python display_refocused_images.py` can then be used for interactively viewing the refocused images generated in the previous step.