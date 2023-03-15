#!/bin/bash

# REF: https://github.com/simonprickett/bash-traffic-lights-pi/blob/master/trafficlights.sh
# REF: https://github.com/LowPowerLab/ATX-Raspi/blob/master/shutdownchecksetup.sh
# https://github.com/LowPowerLab/ATX-Raspi/

# Common path for all GPIO access
BASE_GPIO_PATH=/sys/class/gpio

# Assign names to GPIO pin number for the switch
POWER_BUTTON=22

# Utility function to export a pin if not already exported
exportPin()
{
  if [ ! -e $BASE_GPIO_PATH/gpio$1 ]; then
    echo "$1" > $BASE_GPIO_PATH/export
  fi
}

# Utility function to set a pin as an input
setInput()
{
  echo "in" > $BASE_GPIO_PATH/gpio$1/direction
}

setInputPullup()
{
    echo "high" > $BASE_GPIO_PATH/gpio$1/direction
}

# Utility function to set a pin as an output
setOutput()
{
  echo "out" > $BASE_GPIO_PATH/gpio$1/direction
}

# Utility function to change state of a light
sendOutValue()
{
  echo $2 > $BASE_GPIO_PATH/gpio$1/value
}

# trap shutdown SIGINT

# Export pins so that we can use them
exportPin $POWER_BUTTON

# Set pins as inputs
setOutput $POWER_BUTTON

# Set pin low
sendOutValue $POWER_BUTTON 0

exit 0