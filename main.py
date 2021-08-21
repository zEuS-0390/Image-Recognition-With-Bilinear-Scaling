from src.parser import ArgumentParser
import os, sys

"""
    TITLE: RECYCLABLE MATERIAL DETECTION TEST WITH BILINEAR SCALING IMPLEMENTATION
    DATE PERFORMED: AUGUST 21, 2021; SATURDAY
"""

root_dir = os.path.dirname(os.path.abspath(__file__))

if __name__=="__main__":
    try:
        argparser = ArgumentParser(os.path.join(root_dir, "config.ini"))
        argparser.exec(root_dir)
    except KeyboardInterrupt:
        sys.exit()