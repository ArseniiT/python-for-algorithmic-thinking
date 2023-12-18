"""
Task: 100 Doors

Problem Description:
There are 100 doors in a row, all initially closed. You make 100 passes by the doors starting from the first door every time.
The first time through, you visit every door and toggle the door
(if the door is closed, you open it; if it is open, you close it).
The second time, you only visit every 2nd door (door #2, #4, #6, ...),
and the third time, every 3rd door (door #3, #6, #9, ...), and so on, until you only visit the 100th door.

The question is: which doors are open?
"""


doors = [False] * 101

for i in range(1, 101):
    for j in range(i, 101, i):
        doors[j] = not doors[j]

for i in range(1, 101):
    if doors[i] is True:
        print(i, end=', ')