"""
play

Description:
"""
import pygame
pygame.init()

mp = ".mp3"


def play(recording, number):
    x = number
    time = 0
    for letter in range(len(recording)):
        i = recording[letter]
        if i == "_":
            time += 65
        else:
            pygame.time.wait(time)
            time = 0
            if i == "x":
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
            
            elif i == "z":
                x -= 1
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
            else:
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
            
            if i == "a":
                sound_A.play()
            if i == "b":
                sound_B.play()
            if i == "c":
                sound_C.play()
            if i == "d":
                sound_D.play()
            if i == "e":
                sound_E.play()
            if i == "f":
                sound_F.play()
            if i == "g":
                sound_G.play()
def played(recording):
    x = 0
    time = 0
    for letter in range(len(recording)):
        i = recording[letter]
        if i == "_":
            time += 65
        else:
            pygame.time.wait(time)
            time = 0
            if i == "x":
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
            
            elif i == "z":
                x -= 1
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
            else:
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
            
            if i == "a":
                sound_A.play()
            if i == "b":
                sound_B.play()
            if i == "c":
                sound_C.play()
            if i == "d":
                sound_D.play()
            if i == "e":
                sound_E.play()
            if i == "f":
                sound_F.play()
            if i == "g":
                sound_G.play()
            
