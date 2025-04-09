import datetime
import time
import winsound
from colorama import Fore,Style,init
init()
alarm_clock=input("Enter the Time: ")
while True:
    current_Time = datetime.datetime.now().strftime("%H:%M:%S")
    print(Fore.LIGHTYELLOW_EX+current_Time,end='\r'+Style.RESET_ALL)
    if current_Time == alarm_clock:
        print(Fore.GREEN+"\n\tWake Up!"+Style.RESET_ALL)
        for i in range(6):
            winsound.Beep(1000, 1000)
        break
    time.sleep(1)
    