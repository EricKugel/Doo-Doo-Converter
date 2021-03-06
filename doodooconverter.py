import mido
import statistics

def convert(filename, channel, devConst = 3):
    midi = mido.MidiFile(filename)
    track = midi.tracks[0]
    speeds = []
    notes = []
    output = ""

    for message in track:
        if isinstance(message, mido.Message) and message.type == 'note_on':
            speeds.append(message.time)
            notes.append(message)

    stdev = statistics.stdev(speeds)
    mean = statistics.mean(speeds)

    prevNote = notes[0]
    for note in notes:
        if note.velocity == 0 and prevNote.velocity > 0 and note.channel == channel:
            speed = note.time
            devs = int((speed - mean) / stdev * devConst)

            sound = "doo"

            if devs > 0:
                for x in range(devs):
                    sound += "ooo"

            output += sound + " "
        
        elif prevNote.velocity == 0 and note.time > 120 and note.velocity > 0 and len(output) > 0:
            output = output[0:len(output) - 1] + ", "

        prevNote = note

    return output

if __name__ == "__main__":
    output = open("output.txt", "w")
    output.write(convert("Double.mid", 0, devConst = 3))
    print(convert("Spring.mid", 0, devConst = 2))