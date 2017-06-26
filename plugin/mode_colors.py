#import sys
#import colors

#from layout import layouts

#from razer.client import DeviceManager
# from razer.client import constants as razer_constants

#args = sys.argv
#mode = "normal"
#if len(args) > 1:
#    mode = args[1]


def updateKeyColors(mode):
    import sys
    import colors

    from layout import layouts

    from razer.client import DeviceManager
    print(mode)

    # Create a DeviceManager. This is used to get specific devices
    device_manager = DeviceManager()

    # Disable daemon effect syncing.
    # Without this, the daemon will try to set the lighting effect to every device.
    device_manager.sync_effects = False
    
    # Find the keyboard
    keyboard = None
    for device in device_manager.devices:
        if (device.type == "keyboard"):
            keyboard = device

    # get proper keyboard layout
    if keyboard:
        keylayout = layouts[keyboard.name]
    else:
        return 

    mat = keyboard.fx.advanced.matrix
    
    # helper function to set main color
    def setBaseColor(color):
        for key, coord in keylayout.items():
            mat[coord] = color

    if mode == "insert":
        setBaseColor(colors.BLUE)    
    elif mode == "replace":
        setBaseColor(colors.RED)    
    elif mode == "visual":
        setBaseColor(colors.ORANGE)    
    else:
       setBaseColor(colors.GREEN)    

    keyboard.fx.advanced.draw()
