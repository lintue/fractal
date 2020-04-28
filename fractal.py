"""A simple program for producing fractals.

Implemented by pixel-tree, 2020.
"""

import argparse
import time

from tools import Algorithms, Utils

# Optional arguments.
# TO DO: add help.
parser = argparse.ArgumentParser(description=None)
parser.add_argument("-p", "--pattern",
                    type=str,
                    help="choose fractal pattern")
parser.add_argument("-d", "--dimensions",
                    type=int,
                    nargs=2,
                    help="choose image dimensions")
parser.add_argument("-s", "--scale",
                    type=float,
                    help="choose scale factor")
parser.add_argument("-w", "--save",
                    type=str,
                    help="choose whether to save output")
args = parser.parse_args()

# Default parameters.
default_pattern = "Julia"
default_width, default_height = 1200, 900
default_scale = 3
default_save = False

if __name__ == "__main__":
    """Determine parameters."""

    # Greeting.
    # DISCLAIMER: text decoration tested only on Mac OS.
    NONE = "\033[0m"
    BOLD = "\033[1m"
    OBLIQUE = "\033[3m"
    REVERSE = "\033[7m"
    print(REVERSE)
    print("       __/\__       ")
    print("       \    /       ")
    print(" __/\__/    \__/\__ ")
    print(" \                / ")
    print(" /_              _\ ")
    print("   \            /   ")
    print(" __/            \__ ")
    print(" \                / ")
    print(" /_  __      __  _\ ")
    print("   \/  \    /  \/   ")
    print("       /_  _\       ")
    print("         \/         " + NONE + "\n")
    print(BOLD + "WELCOME TO THE WORLD\nOF FRACTAL GEOMETRY!" + NONE + "\n")

    # Parameters.
    # TO DO: implement error messages for invalid options.
    if args.pattern:
        pattern = args.pattern
        print("Pattern:", args.pattern)
    else:
        pattern = default_pattern
        print("Falling on default pattern:", default_pattern)

    if args.dimensions:
        w, h = args.dimensions[0], args.dimensions[1]
        print("Dimensions:", w, "x", h, "px")
    else:
        w, h = default_width, default_height
        print("Falling on default dimensions:", w, "x", h, "px")

    # TO DO: TEST MIN/MAX VALUES + IMPLEMENT ERROR MSGS.
    if args.scale:
        scale = args.scale
        print("Scale factor:", args.scale)
    else:
        scale = default_scale
        print("Falling on default scale factor:", default_scale)

    if args.save in ["true", "True", "TRUE"]:
        save = True
        print("Save: True")
    elif args.save in ["false", "False", "FALSE"]:
        save = False
        print("Save: False")
    else:
        save = default_save
        print("Save:", default_save)

    # Call appropriate method.
    start = time.time()
    image = Algorithms(pattern, w, h, scale).heuristic()
    end = time.time()
    elapsed = round(end - start, 1)

    # Display and/or save image.
    if save is False:
        Utils.display_img(image)
        print("\n" + "COMPLETED. Time elapsed:", elapsed, "s" + "\n")
    else:
        Utils.save_img(image)
        Utils.display_img(image)
        print("\n" + "COMPLETED & SAVED. Time elapsed:", elapsed, "s." + "\n")
