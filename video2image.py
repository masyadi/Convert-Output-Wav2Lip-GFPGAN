import cv2
from tqdm import tqdm
from os import path, makedirs
from pathlib import Path

inputPath = input("Masukkan path video: ")
outputPath = "results/" + Path(inputPath).stem

# Define paths and create the output directory if it doesn't exist
inputVideoPath = inputPath
unprocessedFramesFolderPath = outputPath

if not path.exists(unprocessedFramesFolderPath):
    makedirs(unprocessedFramesFolderPath)

# Open the video file
vidcap = cv2.VideoCapture(inputVideoPath)

# Get video properties
numberOfFrames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = vidcap.get(cv2.CAP_PROP_FPS)
print("FPS: ", fps, "Frames: ", numberOfFrames)

# Loop through each frame and save it as an image
for frameNumber in tqdm(range(numberOfFrames)):
    success, image = vidcap.read()  # Read the next frame
    if not success:
        break  # Break if there are no more frames

    # Save the frame as an image
    cv2.imwrite(path.join(unprocessedFramesFolderPath, f"{frameNumber:04d}.jpg"), image)

# Release the video capture object
vidcap.release()
