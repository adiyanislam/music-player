"""
music_creator

Description:
"""
import play

window = True

while window:
    print("Type in the music you would like to play.")
    print("Instruments:")
    print("Acoustic Guitar")
    print("Bass")
    print("Chiptune")
    print("Drum")
    print("Electric Guitar")
    print("Flute")
    print("Piano")
    print("Pipes")
    print("Trumpet")
    print("Tuba")
    print("Vibraphone")
    print("Violin")
    print("Guide:")
    print("a-g for the notes")
    print("x to change instrument")
    print("_ for a 200 millisecond gap")
    recording = input()
    if recording == "break" or recording == "end":
        break
    play.played(recording)
