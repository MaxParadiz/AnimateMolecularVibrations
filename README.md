# Animate Molecular Vibrations
Generate normal modes using Psi4, and then visualize the vibrations in Blender

![](https://github.com/MaxParadiz/AnimateMolecularVibrations/blob/main/water.gif)


**Requirements**

- Blender (developed using 4.0.1)
- Python (developed using 3.11.6)
  - Psi4 
  - Numpy
  - Pickle

**How-to**

The file "GenerateMolecularData.py" contains an initial guess for the coordinates of water, which you may replace with your desired molecule's coordinates.

This script will:
 - Optimize the geometry
 - Compute the frequencies
 - Create a dictionary with the geometry, the normal mode displacement matrices, and the associated frequencies
 - Use pickle to dump this dictionary into a file called "molecule_data.pkl"

You will then need to open Blender and copy and paste the script into Blender's Python Console. It is important to run it from within Blender and not through the terminal using *blender --python*, as this will define the functions Vibrate() and Render() within Blender's environment.

To animate the modes, type into the python console Vibrate(). 

The only required argument is:
modes: A list with the normal mode indices that you would like to animate. The animation will consist of a some over all of the modes in the list, allowing for any complex motion to be constructed.

Optional arguments are:
speed: A scalar multiplier that defines how fast the animation goes.
amp: A list containing the amplitude of each mode that goes into the sum.
phase: A list that allows you to control the relative phase between the modes, where np.pi/2 is 90-degrees out of phase.
