"""
music_player

Description:
"""
import play
import tsapp
import pygame



window = tsapp.GraphicsWindow()
pygame.init()
mp = ".mp3"

background = tsapp.Sprite("AbstractRedPaleWave.jpg", 0 , 0)
window.add_object(background)

number = 0


file = open("recording.txt", "r")
recording = file.read()
file.close()

print("Welcome to the music player!")
"""
print("Select an instrument from the following:")
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
"""

print("The keys are: A, S, D, UP, LEFT, DOWN, and RIGHT")
print("To start, press Q")
print("To switch instruments, press Q")
x = 0
instrument = "acoustic_guitar"
print("The current instrument is:" + instrument)
record = False

window.frame_rate = 50

while window.is_running:
    num = 0
    if tsapp.was_key_pressed(tsapp.K_x):
        if record:
            recording += "x"
        x += 1
        if x == 0:
            instrument = "acoustic_guitar"
        if x == 1:
            instrument = "bass"
        if x == 2:
            instrument = "chiptune"
        if x == 3:
            instrument = "drum"
        if x == 4:
            instrument = "electric_guitar"
        if x == 5:
            instrument = "flute"
        if x == 6:
            instrument = "piano"
        if x == 7:
            instrument = "pipes"
        if x == 8:
            instrument = "trumpet"
        if x == 9:
            instrument = "tuba"
        if x == 10:
            instrument = "vibraphone"
        if x == 11:
            instrument = "violin"
        if x > 11:
            x = 0
            instrument = "acoustic_guitar"
        print("The current instrument is:" + instrument)
    else:
        num += 1
        
    if tsapp.was_key_pressed(tsapp.K_z):
        x -= 1
        if record:
            recording += "z"
        if x == 0:
            instrument = "acoustic_guitar"
        if x == 1:
            instrument = "bass"
        if x == 2:
            instrument = "chiptune"
        if x == 3:
            instrument = "drum"
        if x == 4:
            instrument = "electric_guitar"
        if x == 5:
            instrument = "flute"
        if x == 6:
            instrument = "piano"
        if x == 7:
            instrument = "pipes"
        if x == 8:
            instrument = "trumpet"
        if x == 9:
            instrument = "tuba"
        if x == 10:
            instrument = "vibraphone"
        if x == 11:
            instrument = "violin"
        if x > 11:
            x = 0
            instrument = "acoustic_guitar"
        if x < 0:
            x = 11
            instrument = "violin"
        print("The current instrument is:" + instrument)
    else:
        num += 1
        
        
    if not instrument == "drum":
        orig = instrument.replace(" ", "_")
        A = orig + "_A" + mp
        B = orig + "_B" + mp
        C = orig + "_C" + mp
        D = orig + "_D" + mp
        E = orig + "_E" + mp
        F = orig + "_F" + mp
        G = orig + "_G" + mp
    else:
        orig = "drum"
        A = orig + "1" + mp
        B = orig + "2" + mp
        C = orig + "3" + mp
        D = orig + "4" + mp
        E = orig + "5" + mp
        F = orig + "6" + mp
        G = orig + "6" + mp
    
    sound_A = pygame.mixer.Sound(A)
    sound_B = pygame.mixer.Sound(B)
    sound_C = pygame.mixer.Sound(C)
    sound_D = pygame.mixer.Sound(D)
    sound_E = pygame.mixer.Sound(E)
    sound_F = pygame.mixer.Sound(F)
    sound_G = pygame.mixer.Sound(G)

    
    if tsapp.was_key_pressed(tsapp.K_a):
        if record:
            recording += "a"
        sound_A.play()
    else:
        num += 1
    if tsapp.was_key_pressed(tsapp.K_s):
        if record:
            recording += "b"
        sound_B.play()
    else:
        num += 1
    if tsapp.was_key_pressed(tsapp.K_d):
        if record:
            recording += "c"
        sound_C.play()
    else:
        num += 1
    if tsapp.was_key_pressed(tsapp.K_f):
        if record:
            recording += "d"
        sound_D.play()
    else:
        num += 1
    if tsapp.was_key_pressed(tsapp.K_g):
        if record:
            recording += "e"
        sound_E.play()
    else:
        num += 1
    if tsapp.was_key_pressed(tsapp.K_h):
        if record:
            recording += "f"
        sound_F.play()
    else:
        num += 1
    if tsapp.was_key_pressed(tsapp.K_j):
        if record:
            recording += "g"
        sound_G.play()
    else:
        num += 1
    if tsapp.was_key_pressed(tsapp.K_r):
        if record is False:
            record = True
            print("Recording...")
            number = x
            recording = ""
        else:
            print("Recording has stopped...")
            record = False
    if tsapp.was_key_pressed(tsapp.K_p):
        play.play(recording, number)
    
    if num == 9 and  record:
        recording += "_"
    
    
    
    
    window.finish_frame()

file = open("recording.txt", "w")
file.write(recording)
file.close()
