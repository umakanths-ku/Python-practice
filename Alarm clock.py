import pygame
import time 
import datetime

def alarm_time(set_alram):
    
    is_running = True 

    while is_running: 
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == set_alram: 
            print("WAKE UP!!😒")
            is_running = False 
            pygame.mixer.init()
            pygame.mixer.music.load("background_track.mp3")
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(0)
            while pygame.mixer.music.get_busy():
                time.sleep(1)


        time.sleep(1)      

if __name__ == "__main__":
    set_alram = input("Enter the alarm time: ")
    alarm_time(set_alram)