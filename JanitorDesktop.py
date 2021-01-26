# Creation date: 01/21/2021
# Description: A janitor script for my desktop PC downloads folder.
#   Moves files based on filetype (document, image, video, meme)
#   Deletes .exe files if older than 3 days

import os
import datetime
import shutil

DOWNLOAD_DIR = "C:\\Users\\Jeff\\Downloads"
MEME_DIR = "C:\\Users\\Jeff\\Downloads\\memes"

DOC_TYPES = [".epub", ".docx", ".doc", ".odt", ".xls", ".xlsx", ".ppt", "pptx", ".txt", ".pdf"]
#CODE_TYPES = [".html", ".css", ".php", ".xml", ".java", ".json", ".js", ".py", ".c", ".pro", ".pl"]
IMAGE_TYPES = [".jpeg", ".jpg", ".gif", ".bmp", ".png"]
VIDEO_TYPES = [".avi", ".flv", ".wmv", ".mp4", ".mkv"]

DOC_DIR = "C:\\Users\\Jeff\\Downloads\\documents"
#CODE_DIR = "C:\\Users\\Jeff\\Downloads\\code"
IMG_DIR = "C:\\Users\\Jeff\\Downloads\\images"
VIDEO_DIR = "C:\\Users\\Jeff\\Downloads\\videos"

for fname in os.listdir(DOWNLOAD_DIR): # For each filename in download directory
    fpath = DOWNLOAD_DIR + "\\" + fname
    if os.path.isdir(DOWNLOAD_DIR + "\\" + fname): # Ignore directories
        continue
    elif ".exe" in fname: # Delete .exes
        f_time = datetime.datetime.fromtimestamp(os.path.getctime(fpath))
        curr_time = datetime.datetime.now()
        time_diff_raw = curr_time - f_time
        time_diff_days = time_diff_raw.days
        if time_diff_days >= 3:
            os.remove(fpath)
    elif "meme" in fname: # Move memes
        shutil.move(fpath,MEME_DIR)
    else: # Handle filetypes
        for doc_type in DOC_TYPES:
            if(doc_type in fname):
                shutil.move(fpath,DOC_DIR)
                break
        """
        for code_type in CODE_TYPES:
            if(code_type in fname):
                shutil.move(fpath,CODE_DIR)
                break
        """
        for image_type in IMAGE_TYPES:
            if(image_type in fname):
                shutil.move(fpath,IMG_DIR)
                break
        for video_type in VIDEO_TYPES:
            if(video_type in fname):
                shutil.move(fpath,VIDEO_DIR)
                break