#!/bin/python3

# REF: https://stackoverflow.com/questions/53213891/how-to-stop-and-start-a-systemd-service-via-python-script-w-o-requiring-sudo-pas
# REF: https://web.archive.org/web/20160305151936/http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/

import subprocess
import RPi.GPIO as GPIO

if __name__ == '__main__':
    print('START: pi-button-shutdown.py\n')
    try:
        pin = 22
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
    except subprocess.CalledProcessError as err:
        print('ERROR:', err)
    else:
        print('END: pi-button-shutdown.py\n')
