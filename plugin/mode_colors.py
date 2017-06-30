args = sys.argv
mode = "normal"
if len(args) > 1:
    mode = args[1]

#print(mode)

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
    setColor(colors.GREY, keylayout.keys())
    if mode == "visual":
        setColor(colors.ORANGE, keys.functionKeys)
        setColor(colors.ORANGE, keys.visualSelection)
        setColor(colors.RED, keys.modkeys)  
        setColor(colors.ORANGE, keys.movement)
        setColor(colors.GREEN, (*keys.register,'u'))
        setColor(colors.BLUE, ('c',))
    elif mode == "macro":
        macrosSet = ['equals','semicolon','period','forward_slash','minus']
        for reg in "abcdefghijklmnopqrstuvwxyz1234567890":
            if not bool(int(vim.eval("RegisterIsEmpty('"+ reg +"')"))):
                macrosSet.append(reg)
        setColor(colors.RED, macrosSet)
        setColor(colors.BLUE, keys.modkeys)  
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
