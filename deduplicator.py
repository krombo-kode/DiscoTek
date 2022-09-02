from mutagen.easyid3 import EasyID3
import sys
import mutagen
from os import rename, mkdir, getcwd, walk, remove, rmdir
from os.path import isfile, isdir, join


def generate_track_list(path):
    onlytracks = []
    for dirpath, _, fileList in walk(path):
        for x in fileList:
            if x.endswith(".mp3"):
                onlytracks.append(join(x))
                #onlytracks.append(join(dirpath, x))
    if len(onlytracks) == 0:
        print("No tracks found!")
    return onlytracks

def duplicate_list_maker(tracks):
    duplicate_tracks=[]
    for track in tracks:
        if tracks.count(track) > 1:
            duplicate_tracks.append(track)
        else:
            continue
    list.sort(duplicate_tracks)
    return duplicate_tracks


def main_routine(path):
    tracks_list=generate_track_list(path)
    duplicate_tracks=duplicate_list_maker(tracks_list)
    for track in duplicate_tracks:
        print(track)
    print(len(duplicate_tracks))


main_routine("./")
