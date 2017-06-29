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

    from dbus.exceptions import DBusException
    from razer.client import DeviceManager
    from razer.client import DaemonNotFound

    # Create a DeviceManager. This is used to get specific devices
    try:
        device_manager = DeviceManager()
    except (DaemonNotFound, DBusException): 
        #print("vim-razer: error: razer-daemon not running")
        return 1

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
        if keyboard.name in layouts:
            keylayout = layouts[keyboard.name]
        else:
            #print("vim-razer: error: no layout found for " + keyboard.name)
            keylayout = layouts["default"]
    else:
        #print("vim-razer: error: no keyboard found")
        return 0 

    # get the keyboard color matrix
    mat = keyboard.fx.advanced.matrix

    # helper function to set main color
    def setBaseColor(color):
        for key, coord in keylayout.items():
            mat[coord] = color
    
    # set colors depending on mode
    if mode == "insert":
        setBaseColor(colors.BLUE)
    elif mode == "replace":
        setBaseColor(colors.RED)
    else:
        if mode == "visual":
            setBaseColor(colors.ORANGE)
        else:
            setBaseColor(colors.GREEN)
        mat[keylayout['i']] = colors.BLUE
        mat[keylayout['o']] = colors.BLUE
        mat[keylayout['a']] = colors.BLUE
        mat[keylayout['s']] = colors.BLUE
        mat[keylayout['c']] = colors.BLUE
        mat[keylayout['v']] = colors.ORANGE
        mat[keylayout['h']] = colors.YELLOW
        mat[keylayout['j']] = colors.YELLOW
        mat[keylayout['k']] = colors.YELLOW
        mat[keylayout['l']] = colors.YELLOW
        mat[keylayout['w']] = colors.YELLOW
        mat[keylayout['b']] = colors.YELLOW
        mat[keylayout['y']] = colors.RED
        mat[keylayout['d']] = colors.RED
        mat[keylayout['p']] = colors.RED
        mat[keylayout['r']] = colors.RED
        mat[keylayout['x']] = colors.RED
        mat[keylayout['u']] = colors.RED
        mat[keylayout['n']] = colors.RED
        mat[keylayout['forward_slash']] = colors.RED
        mat[keylayout['left_ctrl']] = colors.RED
        mat[keylayout['left_shift']] = colors.RED
        mat[keylayout['right_ctrl']] = colors.RED
        mat[keylayout['right_shift']] = colors.RED


    # esc always goes to normal mode
    mat[keylayout['esc']] = colors.GREEN

    # draw colors on keyboard
    keyboard.fx.advanced.draw()
    return 0
