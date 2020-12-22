# DiscoTek
A small app to read and rename audio files according to ID3 tag contents. 


Changelog:

(v0.2):
    - added detection for existing tracks with same name in DiscoTek Library (will add prompt to enable copies in future version)
    - added framework for dealing with tracks that have no/corrupt tags
        - this includes prompting user about number of bad tracks.
        - due to cost of using AudD, this may become a prompt for user to provide their own API key (that they can get from AudD themselves), so the developer's API key doesn't get suspended/throttled.
    - removed eyeD import as the module is not going to be used.

(v0.1):
    - added functionality for subdirectory traversal
    - app now checks for an existing DiscoTek Library to write output files to, created directory if it doesn't exist
    - app now organizes files that have valid tag data into output library in sub-directories by Artist name.


Future hopeful features:
    - making use of discogs API (may use AudD and AudioDB instead) to add tag data to tracks that are missing it (possibly album art as well?)
    - a UI of some sort
    - a function to create a new library structure to store songs by artist/album *complete*

