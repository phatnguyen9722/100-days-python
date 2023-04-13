import os
import time
from replit import audio


def play():
  source = audio.play_file('audio.wav')
  source.paused = False  # unpause the playback
  while True:
    stopPlayingList = int(
      input("Press 0 to back to the menu: "))
    if stopPlayingList == 0:
      source.paused = True
      return
    else:
      continue

def display(delay, content):
  delayDisplay = float(delay)
  time.sleep(delayDisplay)
  print(content)
  
while True:
  os.system("clear")
  print("🎵 Potify Music Player")
  display(0.5, "Press 1 to Play")
  display(0.5, "Press 2 to Exit")
  display(0.5, "Press 0 to Back to the Menu")
  userInput = int(input())
  
  # Action
  if userInput == 1:
    print("Playing Music Right Now!")
    play()
  elif userInput == 2:
    exit()
  elif userInput == 0:
    continue
  else:
    print("This application has not been released")
    time.sleep(1.5)
    continue
