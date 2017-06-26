import colorsys
import random

from razer.client import DeviceManager
from razer.client import constants as razer_constants

# Create a DeviceManager. This is used to get specific devices
device_manager = DeviceManager()


print("Found {} Razer devices".format(len(device_manager.devices)))
print()

# Disable daemon effect syncing.
# Without this, the daemon will try to set the lighting effect to every device.
device_manager.sync_effects = False


dict = {}
# Set random colors for each zone of each device
for device in device_manager.devices:
    rows, cols = device.fx.advanced.rows, device.fx.advanced.cols
    print(str(rows) + ", " + str(cols))
    for row in range(rows):
        for col in range(cols):
            print("row: " + str(row) + " col: " + str(col))
            device.fx.advanced.matrix[row, col] = (0,255,0)
            device.fx.advanced.draw()
            name = input("...")
            if (name != "no"):
                dict[name] = (row,col)
            device.fx.advanced.matrix[row, col] = (0,0,0)


print(dict)

