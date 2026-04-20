from sense_emu import SenseHat
import time 

sense = SenseHat()

r = [255, 0, 0]
b = [0, 0, 0]
w = [255, 255, 255]

icon = [
	b, b, b, b, b, b, b, b,
	b, r, r, b, b, r, r, b,
	r, r, r, r, r, r, r, r,
	r, r, r, r, r, r, r, r,
	r, r, r, r, r, r, r, r,
	b, r, r, r, r, r, r, b,
	b, b, r, r, r, r, b, b,
	b, b, b, r, r, b, b, b,
]

sense.set_pixels(icon)
print('Bieu tuong dang hien thi tren Sense Hat Emulator...')

time.sleep(5)
sense.clear()
