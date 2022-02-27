if !has('python3')
	finish
endif


let vim_razer_can_run = 0

python3 << EEOOFF

import sys
import vim

# add plugin to path
sys.path.append(vim.eval('expand("<sfile>:h")'))

import colors
import keys
from layout import layouts

# keyboard serial number
serial = ""

try:
	from dbus.exceptions import DBusException
	from openrazer.client import DeviceManager
	from openrazer.client import DaemonNotFound

	device_manager = DeviceManager()
	keyboard = None



	# get the keyboard
	for device in device_manager.devices:
		if (device.type == "keyboard"):
			keyboard = device

	if keyboard:
		device_manager.sync_effects = False
		serial = str(keyboard.serial)
		keyboard.fx.none()

		# get proper keyboard layout
		if keyboard.name in layouts:
			keylayout = layouts[keyboard.name]
		else:
			#print("vim razer: error: no layout found for " + keyboard.name)
			keylayout = layouts["default"]

		vim.command('let vim_razer_can_run = 1')

	else:
		#print("vim-razer: error: keyboard not found")
		pass

except ImportError:
	#print("vim-razer: error: openrazer not installed")
	pass

except (DaemonNotFound, DBusException):
	#print("vim-razer: error: razer-daemon not running")
	pass

EEOOFF


" finish if no daemon running or valid keyboard doesn't exist
if !vim_razer_can_run
	finish
end

" find path of color script
let s:updateColors = fnamemodify(resolve(expand('<sfile>:p')), ':h') . '/mode_colors.py'

" function to reset keyboard effect if using polychromatic
function! ResetProfile()
	python3 << EOF
try:
	from polychromatic import middleman
	from polychromatic import middleman as mm
	from polychromatic.middleman import common as common
	mdbg = common.Debugging()
	def dummy(s):
		return s
	mymiddle = mm.Middleman(mdbg,common,dummy)
	mymiddle.init()
	#print('in reset')
	#print(first_state)
	middle_device = mymiddle.get_device_by_serial(keyboard.serial)
	mm = middle_device
	first_state = mymiddle._get_current_device_option(middle_device)
	mymiddle.set_device_state(mm['backend'],mm['uid'],mm['serial'],None,first_state[0],first_state[1],first_state[2])

except Exception as E:
	print(E)
	print("vim-razer: polychromatic not installed")
EOF
endfunction


function! SetKeyboardColorInsert(mode)
	" Insert mode: blue
	if a:mode == "i"
		python3 sys.argv = ["mode_colors.py", "insert"]
		execute 'py3file ' . s:updateColors

	" Replace mode: red
	elseif a:mode == "r"
		python3 sys.argv = ["mode_colors.py", "replace"]
		execute 'py3file ' . s:updateColors
	endif
endfunction

function! SetKeyboardColorVisual()
	set updatetime=0
	" Visual mode: orange
	python3 sys.argv = ["mode_colors.py", "visual"]
	execute 'py3file ' . s:updateColors
	return ''
endfunction

function! SetKeyboardColorMacroSelect()
	" macro select: white and red
	python3 sys.argv = ["mode_colors.py", "macro"]
	execute 'py3file ' . s:updateColors
	return ""
endfunction

function! ResetKeyboardColor()
	set updatetime=250
	python3 sys.argv = ["mode_colors.py", "normal"]
	execute 'py3file ' . s:updateColors
endfunction

function! RegisterIsEmpty(reg)
	if getreg(a:reg) == ""
		return 1
	else
		return 0
	endif
endfunction

call ResetKeyboardColor()

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
	autocmd VimLeave * call ResetProfile()
augroup END
