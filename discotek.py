from mutagen.easyid3 import EasyID3
import sys
import requests
import json
import mutagen
from pydub import AudioSegment
from os import rename, mkdir, getcwd, walk, remove, rmdir
from os.path import isfile, isdir, join
from bs4 import BeautifulSoup


def rename_track(input_file, output_directory):
    tags = EasyID3(input_file)
    extension = str(input_file)[-4:]
    title = tags['title'][0]
    artist = tags['artist'][0]
    album = tags['album'][0]
    new_filename = title + " - " + artist + extension
    destination_path = output_directory + "\\" + artist.title()
    if not isdir(destination_path):
        mkdir(destination_path)
    destination = destination_path + "\\" + new_filename
    if isfile(destination):
        pass
    else:
        rename(input_file, destination)
    return


def generate_track_list(path):
    onlytracks = []
    for dirpath, _, fileList in walk(path):
        for x in fileList:
            if x.endswith(".mp3") and (dirpath.startswith("./DiscoTek Library") or dirpath.startswith("./Unrecoverable Tracks")) == False:
                onlytracks.append(join(dirpath, x))
    if len(onlytracks) == 0:
        print("No tracks found!")
    return onlytracks

def generate_art_list(path):
    onlyart = []
    for dirpath, _, fileList in walk(path):
        for x in fileList:
            if x.endswith(".jpg") and dirpath.startswith("./Music"):
                onlyart.append(join(dirpath, x))
    if len(onlyart) == 0:
        print("No tracks found!")
    return onlyart





def create_directory(directory):
    parent_dir = getcwd()
    path = join(parent_dir, directory)
    if not isdir(path):
        mkdir(path)
    else:
        print(f"Existing {directory} Folder Found!")
    return path + "\\"


def process_tracks(track_queue, output_directory):
    failed_tracks = []
    for track in track_queue:
        try:
            rename_track(track, output_directory)
            print(f"Moved {track} to {output_directory}")
        except:
            failed_tracks.append(track)
            continue
    return failed_tracks


def bad_track_prompt(bad_tag_tracks):
    if len(bad_tag_tracks) != 0:
        print(
            f'Found {len(bad_tag_tracks)} tracks with bad tags. Do you want to try to fix them?')
        response = ""
        while response != "Y" or "N":
            response = input("Y/N?> ").upper()
            if response == "Y":
                return True
            elif response == "N":
                return False
            else:
                print("Please input Y or N.")
                bad_track_prompt(bad_tag_tracks)
    else: 
        return False


def bad_track_mover(track, directory):
    print(f"Moving {track}.")
    track_path = track.split("\\")
    track_name = track_path[-1]
    destination = directory + track_name
    if isfile(destination):
        pass
    else:
        rename(track, destination)


def process_bad_tag_tracks(bad_tag_tracks, output_directory, api_token):
    unrecoverable_output_directory = create_directory("Unrecoverable Tracks")
    for track in bad_tag_tracks:
        try:
            track_stubber(track)
            track_identity = track_identifier(api_token)
            tag_fixer(track, track_identity)
            process_tracks([track], output_directory)
            remove("10_sec_stub.mp3")
        except:
            bad_track_mover(track, unrecoverable_output_directory)
            continue
    return


def track_identifier(api_token):
    identity = {}
    data = {
        "api_token": f"{api_token}",
        "return": "apple_music"
    }
    files = {
        "file": open("10_sec_stub.mp3", "rb")
    }
    result = requests.post("https://api.audd.io/", data=data, files=files)
    track_info = json.loads(result.text)
    identity["track"] = track_info["result"]["title"]
    identity["artist"] = track_info["result"]["artist"]
    identity["album"] = track_info["result"]["album"]
    return identity


def track_stubber(track):
    ten_second = 10 * 1000
    try:
        song = AudioSegment.from_mp3(track)
        quarter_point = len(song) / 4
        quarter_ten_seconds = song[quarter_point:(quarter_point+ten_second)]
        quarter_ten_seconds.export("10_sec_stub.mp3")
        return True
    except:
        raise Exception(f"{track} is corrupt. Skipping.")


def tag_fixer(track, tags):
    try:
        track_tags = EasyID3(track)
    except mutagen.id3.ID3NoHeaderError:
        try:
            track_tags = mutagen.File(track, easy=True)
            track_tags.add_tags()
        except:
            raise Exception(f"Couldn't fix {track}")
    track_tags["artist"] = tags["artist"]
    track_tags["title"] = tags["track"]
    track_tags["album"] = tags["album"]
    # track_tags["genre"] = tags["genre"]
    track_tags.save(v2_version=3)
    return


def cleanup():
    root = getcwd()
    folders = sorted(list(walk(root))[1:], reverse=True)
    for folder in folders:
        try:
            rmdir(folder[0])
        except OSError:
            continue


def main(path):
    track_queue = generate_track_list(path)
    output_directory = create_directory("DiscoTek Library")
    bad_tag_tracks = process_tracks(track_queue, output_directory)
    if bad_track_prompt(bad_tag_tracks):
        api_token = input("API Token:> ")
        process_bad_tag_tracks(bad_tag_tracks, output_directory, api_token)
    else:
        pass
    cleanup()
    print("Complete!")


main('./')
