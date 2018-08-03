from pprint import pprint

from openrazer.client import DeviceManager
from openrazer.client import constants as razer_constants

# Create a DeviceManager. This is used to get specific devices
device_manager = DeviceManager()


print("Found {} Razer devices".format(len(device_manager.devices)))
print()

# Disable daemon effect syncing.
# Without this, the daemon will try to set the lighting effect to every device.
device_manager.sync_effects = False


# loop through devices and their key layouts
for device in device_manager.devices:
    dic = {}
    rows, cols = device.fx.advanced.rows, device.fx.advanced.cols
    print(str(rows) + ", " + str(cols))
    for row in range(rows):
        for col in range(cols):
            print("row: " + str(row) + " col: " + str(col))
            print(device.fx.advanced.matrix[row, col])
            if device.name != 'Razer Ornata':
                device.fx.advanced.matrix[row, col] = (0, 255, 0)
            else:
                device.fx.advanced.matrix[row, col] = 255
            device.fx.advanced.draw()
            name = input("...")
            if (name != "no"):
                dic[name] = (row, col)
            if device.capabilities['lighting']:
                device.fx.advanced.matrix[row, col] = (0, 0, 0)
            else:
                device.fx.advanced.matrix[row, col] = 0

    print(device.name + ":")
    pprint(device.capabilities)
    pprint(dic)
