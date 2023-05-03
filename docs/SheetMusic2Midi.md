This part of the application focuses on converting the sheet music to a midi representation.
Specficially, we took in `.jpg` or `.png` of the sheet music. By utilizing the Oemer
optical recognition framework, we extract melody and note information from the sheet music and write
it to a newly generated empty midi file.

::: source.SheetMusic2Midi
