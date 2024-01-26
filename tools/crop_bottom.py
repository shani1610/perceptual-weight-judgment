import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.all import crop

def crop_bottom(video_path, output_path):
    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Calculate the new height after cropping 10% from the bottom
    new_height = int(video_clip.size[1] )

    # Crop the bottom 10% of the video
    cropped_clip = crop(video_clip, y1=0, y2=new_height)

    # Write the result to a new file
    cropped_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Close the video clip
    video_clip.close()

def process_videos(input_directory, output_directory):
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Process each MOV file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".MOV"):
            input_path = os.path.join(input_directory, filename)
            new_filename = filename
            # new_filename = filename[:-5]+"1.MOV"
            output_path = os.path.join(output_directory, f"{new_filename}")
            crop_bottom(input_path, output_path)

# Specify the input and output directories
input_directory = "./normal"
output_directory = "./output2"

# Process all videos in the input directory
process_videos(input_directory, output_directory)
