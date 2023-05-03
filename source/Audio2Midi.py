import sys
import subprocess
import os


class Audio2Midi:
    def __init__(self, audioFilePath, midiFilePath = "userInput.mid"):
        """This is the conversion of audio inputs (.mp3 or .wav) into midi files.
        
        Utilizing Spotify's Basic Pitch library, we extract the notes and melody from the song and convert the audio representation into a midi representation.

        
            audioFilePath (str): file path to the audio recording
            midiFilePath (str, optional): file path that the midi will write to. Defaults to "userInput.mid".
        """
        subprocess.run(["basic-pitch", ".", audioFilePath, "--save-midi"])
        # path = "./audioMidiTemp"
        # fileName = os.listdir(path)[0]
        # # Detect the encoding of the file
        # with open(fileName, 'rb') as f:
        #     result = chardet.detect(f.read())
        
        

    
def main():
    Audio2Midi(sys.argv[1])



if __name__ == "__main__":
    main()