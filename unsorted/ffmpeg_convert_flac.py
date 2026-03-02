"""
  This is the first python script i made. ehe
  
  converts files to flac. note that ffmpeg does the educated guess.

  optionally deletes the original file. That's fun.
"""

from pathlib import Path
import subprocess

files = []

def getFilesInDir(path):

    for x in Path(path).iterdir():
        if x.is_dir():
            getFilesInDir(x)
        else:
            files.append(x)

path = '/home/user/Desktop/music'

getFilesInDir(path)

for item in files:
    inputFilename = str(item)
    outputFilename = str(item.with_suffix(".flac"))

    subprocess.run(["ffmpeg", "-i", inputFilename, outputFilename])
    # item.unlink()

print("done!")
