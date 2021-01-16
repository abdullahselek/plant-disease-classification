#!/usr/bin/env python

import sys
import argparse
import base64

from plant_disease_classification import api

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Command Line Interface of plant-disease-classification module that classifies disease on plants"
    )
    parser.add_argument(
        "-p", "--path", type=str, help="Path of image file you want to classify"
    )
    parser.add_argument(
        "-d",
        "--data",
        type=str,
        help="Base64 encoded string of image file you want to classify",
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
    if args.path != None:
        print(api.classify(image_path=args.path))
    if args.data != None:
        data = base64.b64decode(args.data)
        print(api.classify(image_data=data))
