import time 
import datetime
import winsound


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    is_running = True 

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!!🗿")
            winsound.Beep(1000,500)
            time.sleep(1)

            is_running = False

        time.sleep(1)

        


if __name__ == "__main__":
    alram_time = input("Enter the alram time (HH:MM:SS): ")
    set_alarm(alram_time)     
