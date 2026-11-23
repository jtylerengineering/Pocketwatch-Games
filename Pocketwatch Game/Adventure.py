import rotaryio
import board
import displayio


#cell description strings
awake_desc = """You awaken on an uncomfortable cot. The room is dim, and you are sore. You don't know where you are. Do you get up from the cot?"""

situp_desc = """
As you slowly rise from your cot, you take in the room before you."""

cell_front_desc="""
_________________________________________________
|XXXXXXXXXXXXXXXXXXXX======================XXXXX|
|X+----------------+X||  ||  ||  ||  ||  ||XXXXX|
|X|'.'.'.'.'.'.'.'.|X||  ||  ||  ||  ||  ||XXXXX|
|X|'.'.'.'.'.'.'.'.|X||  ||  ||  ||  ||  ||XXXXX|
|X+----------------+X||==================||XXXXX|
|XXXXXXXXXXXXXXXXXXXX||iiiiiiiiiiiiiiiiii||XXXXX|
|XXXXXXXXXXXXXXXXXXXX||iiiiiiiiiiiiiiiiii||XXXXX|
|XXXXXXXXXXXXXXXXXXXX||iiiiiiiiiiiiiiiiii||XXXXX|
|XXXXXXXXXXXXXXXXXXXX||ioiiiiiiiiiiiiiiii||XXXXX|
|XXXXXXXXXXXXXXXXXXXX||iiiiiiiiiiiiiiiiii||XXXXX|
-------------------------------------------------

In front of you is a bulletin board and the cell door. You can:
Examine the door, Examine the bulletin board, or turn.
"""

cell_left_desc="""
__________________________________________________
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|X+----------+XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|X|''''(o''''|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|X|'''''|)'''|XXXXXXXXXXXXX+============+XXXXXXXX|
|X|''''((''''|XXXXXXXXXXXXX|iiiiiiiiiiii|XXXXXXXX|
|X|''''''''''|XXXXXXXXXXXXX|iiiiiiiiiiii|XXXXXXXX|
|X+----------+XXXXXXXXXXXXX+------------+XXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXX|(~~~~~~~~)|XXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXX||~~~~~~~~||XXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXX==========XXXXXXXXXX|
--------------------------------------------------

In front of you is a sink, a mirror and a poster of a person dancing. You can:
Examine the sink and mirror, Examine the poster, or turn.
"""
cell_back_desc = """
__________________________________________________
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXX+=================+XXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXX|| || || || || || ||XXXXXXXXXXXXXXXX|
|XXXXXXXXXXXX|| || || || || || ||XXXXXXXXXXXXXXXX|
|XXXXXXXXXXX======================XXXXXXXXXXXXXXX|
|XXXXXXXXXXX|'.'.'.'.'.'.'.'.'.'.|XXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|rTTTTT9.+-----------------+XXXXXXXXXXXXXXXXXXXXX|
|IIIIIIII|IIIIIIIIIIIIIIIII|XXXXXXXXXXXXXXXXXXXXX|
|--------------------------+XXXXXXXXXXXXXXXXXXXXX|
--------------------------------------------------

It's the cot you woke up in.  There is a small, barred, window in the wall. You can:
Look out the window, Look under the cot, or turn.
"""
cell_r_desc = """
__________________________________________________
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXX|////|XXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
--------------------------------------------------

Not much to tell here. It's a wall.You can:
Examine the wall, or Turn.
"""
#hall description strings
hall_desc="""
__________________________________________________
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXX+-----------+XXXX+-------------+XXXXXXX|
|XXXXXXXXX| <-- LAB   |XXXX|   EXIT -->  |XXXXXXX|
|XXXXXXXXX+-----------+XXXX+-------------+XXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
--------------------------------------------------

It's a long hallway. You can:
Turn.
"""

#exit description string

#encoder pin Numbers:
sw_pin = board.D4
rot_a = board.D0
rot_b = board.D2

#tft display pins
scl_pin = board.D8
bl_pin = board.D1
tft_rst = board.D3
cs_pin = board.D7
miso_pin = board.D9


encoder = rotaryio.IncrementalEncoder(rot_a, rot_b)
last_pos = None

#game vars
room_no = 1
view_no = 1
game_state = False

class door:
    is_open = False



    
class Player:
    situp = False

    

def Game():
    while game_state == True:
        print(awake_desc)
        wakeup_state = input("Do you sit up?")
        

#the Circuit Python equivalent to loop()
while True:
    pos = encoder.position
    if last_pos is None or pos != last_pos:
        print(pos)
    last_pos = pos

    print("Are you ready to play?")
    game_begin = input()

    