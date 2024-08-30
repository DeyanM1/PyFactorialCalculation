import cv2
import os
import re

def sort_key(filename):
    match = re.search(r'(\d+)', filename)
    return int(match.group(1)) if match else 0

# Path to the directory containing the images
image_folder = 'charts/'
video_name = 'output_video.avi'

# Get a list of all images in the directory
images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]
images.sort(key=sort_key)  # Ensure images are in the correct order

# Read the first image to get the size
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter(video_name, fourcc, 10, (width, height))  # FPS is set to 1 here

for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    video.write(frame)  # Write each image to the video

video.release()  # Finalize the video
cv2.destroyAllWindows()