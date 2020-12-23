#!/usr/bin/env python

import sys
import argparse

from plant_disease_classification import api

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Command Line Interface of plant-disease-classification module that classifies disease on plants"
    )
    parser.add_argument(
        "-c", "--classify", type=str, help="Path of the image file you want to classify"
    )
    args = parser.parse_args()

    if len(sys.argv) < 2:
        print("Specify a key to use")
        sys.exit(1)

    try:
        import argcomplete

        argcomplete.autocomplete(parser)
    except ImportError:
        pass

    args = parser.parse_args()
    if args.classify != None:
        print(api.classify(image_path=args.classify))
