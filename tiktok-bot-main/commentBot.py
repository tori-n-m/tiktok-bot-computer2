import pyautogui
import time

#Uses iPhone 6/7/8. Modify dimensions depending on what computer is being used

#while True:
#pauses the video
pyautogui.click(403,415)
time.sleep(2)

#opens the comment section
pyautogui.click(518,465)
time.sleep(4)

#clicks input box
pyautogui.click(327,638)
time.sleep(2)

#writes comment
pyautogui.write("follow for follow", interval=0.2)
time.sleep(2)

#sends comment
pyautogui.click(524,637)
time.sleep(2)

#closes the comment section
pyautogui.click(524,318)
time.sleep(2)

#goes to next video
pyautogui.moveTo(403,605)
pyautogui.dragTo(403,184, 1)