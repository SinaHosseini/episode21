from pysynth import make_wav

notes = [('g4', 4), ('e4', 4), ('d4', 4), ('c4', 4), ('d4', 4), ('e4', 4), ('g4', 4), ('g4', 4),
         ('g4', 4), ('e4', 4), ('e4', 4), ('d4',
                                           4), ('d4', 4), ('e4', 4), ('d4', 2), ('c4', 2),
         ('g4', 4), ('e4', 4), ('d4', 4), ('c4',
                                           4), ('d4', 4), ('e4', 4), ('g4', 4), ('g4', 4),
         ('g4', 4), ('e4', 4), ('e4', 4), ('d4', 4), ('d4', 4), ('e4', 4), ('d4', 2), ('c4', 2)]

make_wav(notes, fn="output.wav")
