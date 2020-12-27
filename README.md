# DiscoTek
A small app to read and rename audio files according to ID3 tag contents. 
Requires FFMpeg installed and added to system path.

Changelog:

(v0.6):\
    - combined create_output_library and create_unrecoverable_output functions into single create_directory function that takes desired directory name as argument\
    - fixed bug where program was placing tracks that had bad tags into unrecoverable file directory regardless of whether the recovery function was successful or not


(v0.5):\
    - application now removes empty directories after completion\
    - application now removes temporary audio stub file after processing each bad track (stub can't accidentally be reused on next track)\
    - files that app fails to fix are placed in a separate directory for user to do with as they please

(v0.4):\
    - implimented song-stubbing for Audd.io track identifier.\
    - implimented AudD.io track identifier\
    - added handling for files with no ID3 tag header

(v0.3):\
    - implimented AudioDB tag lookup\
    - began work on Audd.io track identifier, need to write something to send a 20 second stub of the song instead of the entire file (reduce bandwidth use, no need to go through enterprise endpoint)

(v0.2):\
    - added detection for existing tracks with same name in DiscoTek Library (will add prompt to enable copies in future version)\
    - added framework for dealing with tracks that have no/corrupt tags\
        - this includes prompting user about number of bad tracks.\
        - due to cost of using AudD, this may become a prompt for user to provide their own API key (that they can get from AudD themselves), so the developer's API key doesn't get suspended/throttled.\
    - removed eyeD import as the module is not going to be used.

(v0.1):\
    - added functionality for subdirectory traversal\
    - app now checks for an existing DiscoTek Library to write output files to, created directory if it doesn't exist\
    - app now organizes files that have valid tag data into output library in sub-directories by Artist name.


Future hopeful features:\
    - making use of AudD API add tag data to tracks that are missing it*complete*\
    - a UI of some sort\
    - a function to create a new library structure to store songs by artist/album *complete*\
    - option to process wma and m4a files as well (will convert to mp3 in the process)

