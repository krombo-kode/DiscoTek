from mutagen.easyid3 import EasyID3
# import eyed3
import sys
from os import rename, listdir
from os.path import isfile, join

def rename_track(input_file):
    tags = EasyID3(input_file)
    extension = str(input_file)[-4:]
    new_filename = tags['title'][0] + " - " + tags['artist'][0] + extension
    rename(input_file, new_filename)


def generate_track_list(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    onlyfiles.remove('discotek.py')
    return onlyfiles


def main(path):
    track_queue = generate_track_list(path)
    for track in track_queue:
        try:
            rename_track(track)
        except:
            continue


main('./')
print("Done.")