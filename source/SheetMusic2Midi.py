import subprocess
from music21 import *
import sys

class sheetMusic2Midi:
    def __init__(self, sheetMusicFilePath, xmlFilePath="tempSheetMusic.musicxml", midiFilePath="sheetMusic.mid"):
        """Initializes the Sheet Music and loads into the machine's cache.

        Args:
            sheetMusicFilePath (str): File path to the sheet music
            xmlFilePath (str, optional): File Path to the temp musicXML file. Defaults to "tempSheetMusic.musicxml".
            midiFilePath (str, optional): File Path to the final midi file. Defaults to "sheetMusic.mid".
        """
        self.smusFP  = sheetMusicFilePath
        self.midiFP  = midiFilePath
        self.mxmlFP  = xmlFilePath
        self.scanningMusic()
        self.xmlTOmidi()
        

    def scanningMusic(self):
        """Scans the sheet music and generates the musicXML file using Oemer.
        """
        command = ['oemer', self.smusFP, '-o', self.mxmlFP]
        subprocess.run(command, check=True)
    
    def xmlTOmidi(self):
        """Converts the output of the Oemer ML Model and converts it to musicXML.
        """
        s = converter.parse(self.mxmlFP)
        mf = midi.translate.streamToMidiFile(s)
        mf.open(self.midiFP, 'wb')
        mf.write()
        mf.close()
        

def main():
    sheetMusicFilePath = sys.argv[1]
    sheetMusic2Midi(sheetMusicFilePath)

if __name__ == "__main__":
    main()
