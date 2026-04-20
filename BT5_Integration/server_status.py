from sense_emu import SenseHat
import time

sense = SenseHat()
sense.clear()

def map_value(val, in_min, in_max, out_max=8):
    result = int((val - in_min) / (in_max - in_min) * out_max)
    return max(0, min(out_max, result))

def draw_bar(y_start, y_end, cols, color):
    for y in range(y_start, y_end + 1):
        for x in range(8):
            sense.set_pixel(x, y, color if x < cols else [0,0,0])

print("Bang dieu khien Sense HAT dang chay...")
print("- Keo slider nhiet do > 30 do C de xem canh bao HOT!")
print("- Nhan Joystick (Middle) de xem nhiet do hien tai.")

was_hot = False

try:
    while True:
        temp = sense.get_temperature()
        hum = sense.get_humidity()

        temp_cols = map_value(temp, 15, 40)
        draw_bar(0, 2, temp_cols, [255, 0, 0])

        hum_cols = map_value(hum, 20, 90)
        draw_bar(3, 5, hum_cols, [0, 0, 255])

        if temp > 35 and hum > 80:
            status_color = [255, 0, 0]
        elif temp > 35 or hum > 80:
            status_color = [255, 255, 0]
        else:
            status_color = [0, 255, 0]
            
        draw_bar(6, 7, 8, status_color)

        for event in sense.stick.get_events():
            if event.action == 'pressed' and event.direction == 'middle':
                sense.show_message(f"{temp:.1f}C", text_colour=[255, 255, 255], scroll_speed=0.05)

        if temp > 30 and not was_hot:
            sense.show_message('HOT!', text_colour=[255, 0, 0], scroll_speed=0.05)
            was_hot = True
        elif temp <= 30:
            was_hot = False

        time.sleep(0.1)

except KeyboardInterrupt:
    sense.clear()
