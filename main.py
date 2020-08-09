from pygame import mixer
from time import time
from datetime import datetime


def initMusicPlay(music, stop_value):
    mixer.init()
    mixer.music.load(music)
    mixer.music.play()
    while True:
        a = input(f"Press {stop_value} to stop this music.")
        if a == stop_value:
            mixer.music.stop()
            break


def log_of_task_done(msg="Task"):
    with open("log.txt", 'a') as file:
        file.write(f"{datetime.now()} :- {msg} has been done \n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exe = time()
    water_sec = 1800
    eyes_sec = 2700
    exe_sec = 3600
    while True:
        if time() - init_water >= water_sec:
            initMusicPlay("water.mp3", "drank water")
            log_of_task_done("Drank water")
            init_water = time()
        if time() - init_eyes >= eyes_sec:
            initMusicPlay("eyes.mp3", "done eyes")
            log_of_task_done("Eyes task")
            init_eyes = time()
        if time() - init_exe >= exe_sec:
            initMusicPlay("excercise.mp3", "jumping done")
            log_of_task_done("Jumping Task")
            init_exe = time()
