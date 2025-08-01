# mawaddah-ai-AI-Path-Task1---Smart-Methods-Course
# all AI tasks will be in this repository
this repository contains task 1 files of AI learning paths - smart methods

## TASK ONE :
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

## TASK THREE 
FOUR FILES  
- Converting.py
- converted_audio.wav
- terminal.txt
- response_audio.mp3
# Note: The API key was removed from this project for security reasons.
# Steps:
1- Transcribing audio using Vosk speech recognition model

1.1 Loading the WAV audio file (Mono, 16kHz PCM)
1.2 Loading the Vosk pre-trained speech recognition model
1.3 Processing audio in chunks and converting speech to text
1.4 Handling errors if audio format or file is incorrect
1.5 Retrieving the full transcription text

2- Generating response text using Cohere language model API

2.1 Setting up Cohere API client with API key
2.2 Sending the transcribed text as prompt to generate a response
2.3 Handling API errors and invalid model issues
2.4 Receiving and extracting generated text from response

3- Converting the generated text to speech audio

3.1 Using Google Text-to-Speech (gTTS) library to synthesize audio
3.2 Saving the generated speech to an MP3 file
3.3 Handling any exceptions during audio generation

4- Playing the generated audio on Windows

4.1 Using system command to launch Windows Media Player silently
4.2 Optional: skipping playback if not needed


## TASK four 
# 1- Understanding File Permissions
The file permission system in Linux/Unix is composed of three types of access:

r = read (allows viewing the contents of the file)

w = write (allows modifying the file)

x = execute (allows running the file as a program or script)

These permissions are assigned to three categories of users:

User – the owner of the file

Group – users who belong to the file's group

Others – all other users on the system

# 2- Flowchart , uploaded in files section 
# 3- 
