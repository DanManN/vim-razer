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
    setColor(colors.AQUA, keylayout.keys())
    setColor(colors.YELLOW, keys.modkeys)  
elif mode == "replace":
    setColor(colors.RED, keylayout.keys())
    setColor(colors.YELLOW, keys.modkeys)  
else:
    setColor(colors.BLACK, keylayout.keys())
    if mode == "visual":
        setColor(colors.ORANGE, keys.functionKeys)
        setColor(colors.ORANGE, keys.visualSelection)
        setColor(colors.PURPLE, keys.modkeys)  
        setColor(colors.ORANGE, keys.movement)
        setColor(colors.GREEN, (*keys.register,'u'))
        setColor(colors.AQUA, ('c',))
    elif mode == "macro":
        macrosSet = ['period','forward_slash']
        for reg in "abcdefghijklmnopqrstuvwxyz1234567890":
            if not bool(int(vim.eval("RegisterIsEmpty('"+ reg +"')"))):
                macrosSet.append(reg)
        setColor(colors.PINK, macrosSet)
        setColor(colors.YELLOW, keys.modkeys)  
        setColor(colors.BLUE, ('equals','minus','semicolon'))
    else:
        setColor(colors.GREEN, keys.functionKeys)
        setColor(colors.AQUA, keys.toInsert)
        setColor(colors.ORANGE, keys.toVisual)
        setColor(colors.RED, keys.toReplace)
        setColor(colors.PINK, keys.undoredo)
        setColor(colors.GREEN, keys.movement)
        setColor(colors.PINK, keys.deletion)
        setColor(colors.PINK, keys.register)
        setColor(colors.PINK, keys.search)
        setColor(colors.YELLOW, keys.modkeys)  
        setColor(colors.PURPLE,('semicolon',))

# esc always goes to normal mode
setColor(colors.GREEN,('esc',))

# draw colors on keyboard
keyboard.fx.advanced.draw()
