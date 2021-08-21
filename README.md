# Image Recognition Test with Bilinear Scaling

Classes:
- paper
- plastic bottle
- cardboard
- glass bottle
- can
- aluminum bottle

Dependencies:
- matplotlib
- opencv-python

State-of-the-Art Object Detection Algorithm: 
- AlexeyAB's Darknet YOLOv3: https://github.com/AlexeyAB/darknet

Download Model File: https://drive.google.com/drive/folders/1-43Jx55K6gSR6jJgCm7Zd1rmRtUrO0kj?usp=sharing

### Instructions:
1. Download and save the model file in the req folder
2. To see the available arguments in the program, follow this command:
```
python main.py --help
```
2. To test and compare the performance of the trained model from images input with and without bilinear scaling, follow this command to generate a single output image:
  ```
  python main.py --testimages "<absolute_path_of_images_folder>"
  ```
3. To detect and save images without bilinear scaling, follow this command:
  ```
  python main.py --imagesinput "<absolute_path_of_images_folder>"
  ```
4. You can change the configurations of the program by changing the settings in config.ini
  ```
  [Requirements]
  weights: model.weights
  cfg: model_config.cfg
  names: classes.names

  [GPU]
  CUDA: True

  [Detection]
  nn_width: 608
  nn_height: 608
  scale: 10
  confidence_thresh: 0.5
  NMS: True
  ```
