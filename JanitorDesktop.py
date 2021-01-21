# Creation date: 01/21/2021
# Description: A janitor script for my desktop PC downloads folder.

import os
import datetime
import shutil

IMAGE_TYPES = [".jpeg", ".jpg", ".gif", ".bmp", ".png"]
VIDEO_TYPES = [".avi", ".flv", ".wmv", ".mp4", ".mkv"]
DOC_TYPES = [".epub", ".docx", ".doc", ".odt", ".xls", ".xlsx", ".ppt", "pptx", ".txt", ".pdf"]

DOWNLOAD_DIR = "C:\\Users\\Jeff\\Downloads"
DOC_DIR = "C:\\Users\\Jeff\\Downloads\\documents"
IMG_DIR = "C:\\Users\\Jeff\\Downloads\\videos"
VIDEO_DIR = "C:\\Users\\Jeff\\Downloads\\images"
MEME_DIR = "C:\\Users\\Jeff\\Downloads\\memes"

for fname in os.listdir(DOWNLOAD_DIR): # For each filename in download directory
    fpath = DOWNLOAD_DIR + "\\" + fname
    print("Filename: " + fname, end='')
    if os.path.isdir(DOWNLOAD_DIR + "\\" + fname):
        continue
    elif ".exe" in fname:
        print()
        f_time = datetime.datetime.fromtimestamp(os.path.getctime(fpath))
        curr_time = datetime.datetime.now()
        time_diff_raw = curr_time - f_time
        time_diff_days = time_diff_raw.days
        print("curr:")
        print(f_time)
        print("curr_time:")
        print(curr_time)
        print("time_diff_raw:")
        print(time_diff_raw)
        print("time_diff_days:")
        print(time_diff_days)
        #print("created: %s" %  test)
    elif "meme" in fname:
        shutil.move(fpath,MEME_DIR)
    else:
        for doc_type in DOC_TYPES:
            if(doc_type in fname):
                shutil.move(fpath,DOC_DIR)
                break
        for image_type in IMAGE_TYPES:
            if(image_type in fname):
                shutil.move(fpath,IMG_DIR)
                break
        for video_type in VIDEO_TYPES:
            if(video_type in fname):
                shutil.move(fpath,VIDEO_DIR)
                break