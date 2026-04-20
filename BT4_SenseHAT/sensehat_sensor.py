from sense_emu import SenseHat
import time

sense = SenseHat()

print("--- Dang doc du lieu tu cam bien Sense HAT ---")
print("Nhan Ctrl+C de dung lai.")

try:
	while True:
		temp = sense.get_temperature()
		hum = sense.get_humidity()
		press = sense.get_pressure()

		print(f'Temp: {temp:.1f} do C | Humidity: {hum:.1f}% |Pressure: {press:.1f} mbar')
		time.sleep(1)

except KeyboardInterrupt:
	sense.clear()
	print('Da dung doc cam bien.')
