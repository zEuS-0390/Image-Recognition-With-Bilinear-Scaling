from src.detector import Detection
import matplotlib.pyplot as plt 
from src.utils import *
import os, collections, cv2

class ImagesInput(Detection):

    def __init__(self, root, conf):
        super(ImagesInput, self).__init__(root, conf)
        self.conf = conf

    # Perform bilinear scaling with cv2.INTER_LINEAR and keep the aspect ratio
    def bilinear_scaling(self, image):
        image = cv2.resize(image, 
                           (int(image.shape[1] * self.conf.getint("Detection", "scale") / 100), 
                            int(image.shape[0] * self.conf.getint("Detection", "scale") / 100)), 
                           interpolation=cv2.INTER_LINEAR)
        return image

    # Detect in images from directory
    def detectImages(self, directory, save=True, bilinear_scaling=False):
        detected = {}
        newDir = os.path.join(directory, "detected_images")
        if not os.path.exists(newDir) and save:
            os.mkdir(newDir)
        image_file_paths = explore(directory, subdir=True)
        current_no, total = 0, len(image_file_paths)
        for image_file_path in image_file_paths:
            current_no += 1
            image = cv2.imread(image_file_path)
            if bilinear_scaling:
                image = self.bilinear_scaling(image)
                print(f"[DETECT SCALED {image.shape[1]}x{image.shape[0]}]: {os.path.basename(image_file_path)}")
            else:
                print(f"[DETECT {image.shape[1]}x{image.shape[0]}]: {os.path.basename(image_file_path)}")
            detected_objects = self.OBJDetector.detect(image, NMS=self.conf.getboolean("Detection", "NMS"))
            size = detected_objects["size"]
            detected[os.path.basename(image_file_path)] = size
            if save:
                image = self.drawDetected(image, detected_objects)
                check = "detected objects" if size > 1 else "detected object"
                if size > 0:
                    cv2.imwrite(os.path.join(newDir, os.path.basename(image_file_path)), image)
                    print(f"[SAVED][{size} {check}]: {os.path.basename(image_file_path)} {size} ({current_no}/{total} images) {round(current_no/total*100, 3)}% ")
                else:
                    print(f"[NOT SAVED][{size} {check}]: {os.path.basename(image_file_path)} ({current_no}/{total} images) {round(current_no/total*100, 3)}%")
        return detected
    
    # Test and compare detection with and without bilinear interpolation/scaling
    def testImages(self, directory):
        image_file_paths = explore(directory, subdir=True)
        images = [os.path.basename(image_file_path) for image_file_path in image_file_paths]
        not_scaled = self.detectImages(directory, save=False)
        scaled = self.detectImages(directory, save=False, bilinear_scaling=True)
        group = collections.defaultdict(list)
        for image in (not_scaled, scaled):
            for key, value in image.items():
                group[key].append(value)
        group = dict(group)
        plt.figure(facecolor="cornsilk")
        data = tuple(group.values())
        plt.table(cellText = data,
                  cellColours = [["lightpink" for _ in range(len(data[0]))] for _ in range(len(data))],
                  colLabels = ('Not Scaled', 'Scaled'),
                  colColours=["skyblue", "skyblue"],
                  rowLabels = images,
                  rowColours = ["lightgreen" for _ in range(len(images))],
                  cellLoc="center",
                  loc='center')
        plt.axis('off'); plt.grid('off')
        plt.savefig("detected_outputs.png", bbox_inches="tight", dpi=100)
        print(f"[SAVED]: detected_outputs.png")