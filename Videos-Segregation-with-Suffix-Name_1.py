import os
import shutil

# Define the directory containing the video files
source_path = 'ADD_YOUR_PATH'

# Define the file extension to filter on
#Example:- (_1.mp4)
file_extension = 'Your_Extension'
# Get a list of all the files in the directory
files = os.listdir(source_path)

# Filter the files based on the file extension
filtered_files = []
for file in files:
    if file.endswith(file_extension):
        filtered_files.append(file)

# Print the filtered list of files
print(filtered_files)

source_dir = 'ADD_YOUR_PATH'
dest_dir = 'ADD_YOUR_PATH'
for file in filtered_files:
    source_path = os.path.join(source_dir, file)
    dest_path = os.path.join(dest_dir, file)
    shutil.copy2(source_path, dest_path)
print(f"Files {', '.join(filtered_files)} copied to {dest_dir}")