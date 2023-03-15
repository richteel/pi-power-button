#!/bin/python3

# REF: https://stackoverflow.com/questions/53213891/how-to-stop-and-start-a-systemd-service-via-python-script-w-o-requiring-sudo-pas
# REF: https://web.archive.org/web/20160305151936/http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/

import subprocess
import RPi.GPIO as GPIO

if __name__ == '__main__':
    pin = 22
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.wait_for_edge(pin, GPIO.FALLING)
    subprocess.call(['shutdown', '-h', 'now'], shell=False)
