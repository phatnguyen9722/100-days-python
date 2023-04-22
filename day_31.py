def colorChange(color):
    colors = {"red": "\033[31m", "white": "\033[0m", "blue": "\033[34m", 
              "yellow": "\033[33m", "green": "\033[32m", "purple": "\033[35m"}
    return colors[color]

title = f"{colorChange('red')}={'='*13}{colorChange('blue')} Music App {colorChange('red')}={'='*13}{colorChange('white')}"
print(f"{title:^35}")
print(f"🔥▶️\t{colorChange('white')}Radio Gaga")
print(f"{colorChange('white')}{'prev':<35}{colorChange('green')}{'next':^35}{colorChange('purple')}{'pause':>35}")
print("\nWELCOME TO".center(35, ' '))
print("--  ARMBOOK  --".center(35, ' '))
print(f"{colorChange('yellow')}{'Definitely not a rip off':>35}")
print(f"{colorChange('yellow')}{'a certain other social':>35}")
print(f"{colorChange('yellow')}{'networking site':>35}")
print(f"{colorChange('red')}{'Honest.':^35}")
username = input(f"{colorChange('white')}Username: ".center(35, ' '))
password = input(f"{colorChange('white')}Password: ".center(35, ' '))
