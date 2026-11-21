#TO-DO
#[ ] design game paths
#[ ] write game dialogue
#[ ] design game visuals
#[ ] wite scripts for tft display
#[ ] write controls
#   [ ]using rotary encoder to highlight choices
#   [ ]cicking rotary encoder to select choice



import rotaryio
import board
import displayio


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

#the Circuit Python equivalent to loop()
while True:
    pos = encoder.position
    if last_pos is None or pos != last_pos:
        print(pos)
    last_pos = pos