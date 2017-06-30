if !has('python3')
	finish
endif


let vim_razer_can_run = 1

python3 << EEOOFF

# --------------------------------
# Add our plugin to the path
# --------------------------------

import sys
import vim
sys.path.append(vim.eval('expand("<sfile>:h")'))

import colors
import keys

from layout import layouts

from dbus.exceptions import DBusException
from razer.client import DeviceManager
from razer.client import DaemonNotFound

try:
	device_manager = DeviceManager()
	keyboard = None
	for device in device_manager.devices:
		if (device.type == "keyboard"):
			keyboard = device
	if keyboard:
		device_manager.sync_effects = False

		# get proper keyboard layout
		if keyboard.name in layouts:
			keylayout = layouts[keyboard.name]
		else:
    			#print("vim-razer: error: no layout found for " + keyboard.name)
			keylayout = layouts["default"]
	else:
		#print("vim-razer: error: keyboard not found")
		vim.eval('let vim_razer_can_run = 0')

except (DaemonNotFound, DBusException): 
	#print("vim-razer: error: razer-daemon not running")
	vim.eval('let vim_razer_can_run = 0')
EEOOFF

" finish if no daemon running or valid keyboard doesn't exist
if !vim_razer_can_run
	finish
end	


function! SetKeyboardColorInsert(mode)
	" Insert mode: blue
	if a:mode == "i"
		python3 sys.argv = ["mode_colors.py", "insert"]
		py3file mode_colors.py

	" Replace mode: red
	elseif a:mode == "r"
		python3 sys.argv = ["mode_colors.py", "replace"]
		py3file mode_colors.py
	endif
endfunction

function! SetKeyboardColorVisual()
	set updatetime=0

	" Visual mode: orange
	python3 sys.argv = ["mode_colors.py", "visual"]
	py3file mode_colors.py
	return ''
endfunction

function! SetKeyboardColorMacroSelect()
	" macro select: white and red
	python3 sys.argv = ["mode_colors.py", "macro"]
	py3file mode_colors.py
endfunction

function! ResetKeyboardColor()
	set updatetime=250 
	python3 sys.argv = ["mode_colors.py", "normal"]
	py3file mode_colors.py
endfunction

function! RegisterIsEmpty(reg)
	if getreg(a:reg) == ""
		return 1
	else
		return 0
	endif	
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
"command! Example call TemplateExample()

vnoremap <expr> <SID>SetKeyboardColorVisual SetKeyboardColorVisual()
nnoremap <script> v v<SID>SetKeyboardColorVisual
nnoremap <script> V V<SID>SetKeyboardColorVisual
nnoremap <script> <C-v> <C-v><SID>SetKeyboardColorVisual
vnoremap <script> <LeftRelease> <LeftRelease><SID>SetKeyboardColorVisual
inoremap <script> <C-c> <C-c><SID>ResetKeyboardColor()
nnoremap <expr> <SID>SetKeyboardColorMacroSelect SetKeyboardColorMacroSelect()
nnoremap <script> @ <SID>SetKeyboardColorMacroSelect@
"vnoremap <expr> <SID>SetKeyboardColorMacroSelect SetKeyboardColorMacroSelect()
"vnoremap <script> @ <SID>SetKeyboardColorMacroSelect@

augroup KeyboardColorSwap
    autocmd!
    autocmd InsertEnter * call SetKeyboardColorInsert(v:insertmode)
    autocmd InsertLeave * call ResetKeyboardColor()
    autocmd CursorHold * call ResetKeyboardColor()
augroup END
