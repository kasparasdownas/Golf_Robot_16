Trin til at installere på microSD:

Download EV3 MicroPython SD card image:

Flash it to a microSD card (at least 8GB) using Balena Etcher.

Insert the SD card into your EV3 Brick and power it on.

Once your EV3 Brick is ready, install the necessary Python library:
pip install python-ev3dev2

After that, change ev3_movement.py


🚀 Run the script
Connect your EV3 Brick to your computer via SSH:
ssh robot@ev3dev.local
Password: maker


Transfer the file:
scp src/ev3_movement.py robot@ev3dev.local:~


Run it on the EV3 Brick:
python3 ev3_movement.py


