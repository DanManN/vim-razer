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
    import keys

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

    # helper function to set color of keys
    def setColor(color, keyset):
        for key in keyset:
            mat[keylayout[key]] = color
    
    # set colors depending on mode
    if mode == "insert":
        setColor(colors.BLUE, keylayout.keys())
        setColor(colors.RED, keys.modkeys)  
    elif mode == "replace":
        setColor(colors.RED, keylayout.keys())
        setColor(colors.BLUE, keys.modkeys)  
    else:
        if mode == "visual":
            setColor(colors.ORANGE, keys.functionKeys)
            setColor(colors.ORANGE, keys.visualSelection)
            setColor(colors.BLUE, keys.modkeys)  
            setColor(color.GREEN, keys.movement)
        else:
            setColor(colors.GREEN, keys.functionKeys)
            setColor(colors.BLUE, keys.toInsert)
            setColor(colors.ORANGE, keys.toVisual)
            setColor(colors.RED, keys.toReplace)
            setColor(colors.RED, keys.undoredo)
            setColor(colors.GREEN, keys.movement)
            setColor(colors.RED, keys.deletion)
            setColor(colors.RED, keys.register)
            setColor(colors.RED, keys.search)
            setColor(colors.RED, keys.modkeys)  
            setColor(colors.RED,('semicolon',))


    # esc always goes to normal mode
    setColor(colors.GREEN,('esc',))

    # draw colors on keyboard
    keyboard.fx.advanced.draw()
    return 0
