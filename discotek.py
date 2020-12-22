from mutagen.easyid3 import EasyID3
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
    destination = destination_path + "\\" + new_filename
    if isfile(destination):
        print(f'{new_filename} already exists in the DiscoTek Library!')
    else:
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


def process_tracks(track_queue, output_directory):
    failed_tracks = []
    for track in track_queue:
        try:
            rename_track(track, output_directory)
        except:
            print(f"{track} has bad tags!")
            failed_tracks.append(track)
            continue
    return failed_tracks


def bad_track_prompt(bad_tag_tracks):
    print(
        f'Found {len(bad_tag_tracks)} tracks with bad tags. Do you want to try to fix them?')
    response = input("Y/N?> ").upper()
    if response == "Y":
        for track in bad_tag_tracks:
            print(track)
        print("This feature is not yet implimented")
        return
    elif response == "N":
        return False
    else:
        print("Please input Y or N.")
        bad_track_prompt(bad_tag_tracks)


def process_bad_tag_tracks(bad_tag_tracks, output_directory):
    for track in bad_tag_tracks:
        found_tags = tag_finder(track)
        # Should return a dict of tags
        repaired_track = tag_fixer(track, found_tags)
        # Add tags to track
        process_tracks([repaired_track], output_directory)


def tag_finder(track):
    # Will use AudD to find track, AudioDB to generate tags, return tags as dict
    return track


def tag_fixer(track, tags):
    # will read from tag_finder dict and apply tags to track
    return {}


def main(path):
    track_queue = generate_track_list(path)
    output_directory = create_output_library() + "\\"
    bad_tag_tracks = process_tracks(track_queue, output_directory)
    if bad_track_prompt(bad_tag_tracks):
        process_bad_tag_tracks(bad_tag_tracks, output_directory)
    else:
        pass
    print("Complete!")


main('./')
