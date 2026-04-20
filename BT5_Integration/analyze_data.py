import csv

temps, hums, dists = [], [], []
warnings = 0
intrusions = 0

try:
	with open('/home/pi/iot_lab/wokwi_data.csv', 'r') as f:
		reader = csv.DictReader(f)
		for row in reader:
			t = float(row['temperature'])
			h = float(row['humidity'])
			d = float(row['distance'])

			temps.append(t)
			hums.append(h)
			dists.append(d)

			if row['status'] != 'NORMAL':
				warnings += 1
			if d < 30:
				intrusions += 1

	avg_temp = sum(temps)/len(temps)

	print('===BAO CAO PHONG SEVER===')
	print(f'Tong mau: {len(temps)}')
	print(f'Nhiet do: TB={avg_temp:.1f} do C, Min ={min(temps):.1f} do C, Max={max(temps):.1f} do C')
	print(f'Phat hien nguoi vao: {intrusions} lan')
	print(f'Canh bao: {warnings}/{len(temps)} ({warnings/len(temps)*100:.0f}%)')

	with open('/home/pi/iot_lab/report.txt', 'w') as f:
		f.write(f'Tong mau: {len(temps)}\n')
		f.write(f'Nhiet do TB: {avg_temp:.1f}\n')
		f.write(f'Phat hien nguoi: {intrusions}\n')

	print('--- Da ghi report.txt ---')

except FileNotFoundError:
	print("Loi: Khong tim thay file wokwi_data.csv.")
except Exception as e:
	print(f"Co loi xay ra: {e}")
