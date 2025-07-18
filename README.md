# mawaddah-ai-AI-Path-Task1---Smart-Methods-Course
this repository contains task 1 files of AI learning paths - smart methods

TASK ONE :
steps :
1- by using teachable machine I trained an AI model to define if the picture represents Katniss Everdeen or Peeta Mellark (the hunger game’s main character) 

  1.1- adding images of each character 

  1.2-training the model
 
  1.3-testing the model by uploading different images and positions of the characters

  1.4- the model got some error result, so I added other images to the model, so it can recognize more pictures 1.5test other pictures 
 

2- exporting the model to the local environment (laptop) and by using bycharm I coded a program to represent the model output 

  2.1-exporting the model data to the local environment 

  2.2-move the model file into the python program file 

  2.3-add some Improvements, so it can show the results in a better way 

  2.4-entering the paths of test pictures to the output terminal 

  2.5-checking results


## TASK TWO: Real-Time Face Detection Using OpenCV

### Steps:

**1- Installing the required libraries and setting up the environment**  
1.1- Install Python from the official website  
1.2- Install OpenCV library using the terminal using `pip install opencv-python`  
1.3- *(Optional)* create a virtual environment using `python -m venv venv`  
1.4- Open the project in PyCharm or any Python IDE

**2- Preparing the model for detecting human faces**  
2.1- Download the `haarcascade_frontalface_default.xml` model file from OpenCV GitHub  
2.2- Place the XML file in the same folder as the Python script  
2.3- Prepare a video file that contains human faces  
2.4- Update the video file path in the Python code

**3- Writing the Python code using OpenCV to detect faces**  
3.1- Use OpenCV to load the XML cascade file  
3.2- Read the video using `cv2.VideoCapture()`  
3.3- Convert each frame to grayscale for processing  
3.4- Detect the faces using `detectMultiScale()`  
3.5- Draw green rectangles around detected faces  
3.6- Display the output video with rectangles on faces  
3.7- Exit the window when pressing the 'q' key

**4- Testing the result**  
4.1- Run the Python script from PyCharm  
4.2- The video will open in a window  
4.3- Observe the detection of faces in real-time  
4.4- If detection fails, try with clearer or different video  
4.5- Make sure the XML and video file paths are correct

**5- Final result**  
- Green rectangles appear around each detected face  
- Window exits on key press `q`  
- Real-time face detection achieved using OpenCV and a pretrained Haar cascade

