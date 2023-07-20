put:
	# @ampy -p /dev/ttyACM1 put code.py
	# @ampy -p /dev/ttyACM1 put boot.py
	cp code.py /run/media/rodrigokimura/CIRCUITPY/code.py
	cp lib/adafruit_hid /run/media/rodrigokimura/CIRCUITPY/lib -r

check:
	@rshell -l

test:
	@ampy -p /dev/ttyACM1 run code.py

ls:
	@ampy -p /dev/ttyACM1 ls

lint:
	@pipenv run black .
	@pipenv run isort .
