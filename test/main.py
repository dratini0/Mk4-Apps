"""This is a simple hello world app"""

___name___         = "Echo"
___license___      = "MIT"
___dependencies___ = ["sleep", "app"]
___categories___   = ["0"]

import ugfx, os, time, sleep, app


# initialize screen
ugfx.init()
ugfx.clear()

ugfx.text(5, 5, "Kittens", ugfx.BLACK)

while True:
    a = input()
    print(a)
    if a == "":
        break
