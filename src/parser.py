import argparse, configparser
from src.imagesInput import ImagesInput

class ArgumentParser(argparse.ArgumentParser):

    def __init__(self, config_file_path):
        super(ArgumentParser, self).__init__()
        self.confparser = configparser.ConfigParser()
        self.confparser.read(config_file_path)
        self.setupInit()

    def setupInit(self):
        self.add_argument("-imgsin", "--imagesinput", action="store", help="Detect and save images.")
        self.add_argument("-test", "--testimages", action="store", help="Test and compare detection with and without bilinear interpolation/scaling.")

    def exec(self, root):
        args = self.parse_args()
        if args.imagesinput is not None:
            ImagesInput(root, self.confparser).detectImages(args.imagesinput)
        if args.testimages is not None:
            ImagesInput(root, self.confparser).testImages(args.testimages)
        