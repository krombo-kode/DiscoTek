from mutagen.easyid3 import EasyID3
import eyed3
import sys
from os import rename, mkdir, getcwd, walk
from os.path import isfile, isdir, join


def rename_track(input_file, output_directory):
    tags = EasyID3(input_file)
    extension = str(input_file)[-4:]
    title = tags['title'][0]
    artist = tags['artist'][0]
    new_filename = title + " - " + artist + extension
    destination_path = output_directory + "\\" + artist.title()
    if not isdir(destination_path):
        mkdir(destination_path)
    destination = destination_path +"\\"+ new_filename
    rename(input_file, destination)


def generate_track_list(path):
    onlytracks = []
    for dirpath, subdirList, fileList in walk(path):
        for x in fileList:
            if x.endswith(".mp3"):
                onlytracks.append(join(dirpath, x))
    if len(onlytracks) == 0:
        print("No tracks found!")
    return onlytracks


def create_output_library():
    directory = "DiscoTek Library"
    parent_dir = getcwd()
    path = join(parent_dir, directory)
    if not isdir(path):
        mkdir(path)
    else:
        print("Existing DiscoTek Library Found!")
    return path


def main(path):
    track_queue = generate_track_list(path)
    output_directory = create_output_library() + "\\"
    for track in track_queue:
        try:
            rename_track(track, output_directory)
        except:
            print(f"{track} has bad tags, trying to find the right ones!")
            continue


print(getcwd())
main('./')
