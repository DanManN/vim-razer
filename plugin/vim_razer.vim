if !has('python3')
	finish
endif
" --------------------------------
" Add our plugin to the path
" --------------------------------
python3 import sys
python3 import vim
python3 sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
"
"function! TemplateExample()
"python << endOfPython
"
"from vim_razer import vim_razer_example
"
"for n in range(5):
"    print(vim_razer_example())
"
"endOfPython
"endfunction

function! SetKeyboardColorInsert(mode)
    " Insert mode: blue
    if a:mode == "i"
	python3 << EOF
from mode_colors import updateKeyColors
updateKeyColors("insert")
EOF

    " Replace mode: red
    elseif a:mode == "r"
	python3 << EOF
from mode_colors import updateKeyColors
updateKeyColors("replace")
EOF

    endif
endfunction


function! SetKeyboardColorVisual()
    set updatetime=0

    " Visual mode: orange
    python3 << EOF
from mode_colors import updateKeyColors
updateKeyColors("visual")
EOF
    return ''
endfunction


function! ResetKeyboardColor()
    set updatetime=4000
    python3 << EOF
from mode_colors import updateKeyColors
updateKeyColors("normal")
EOF
endfunction


" --------------------------------
"  Expose our commands to the user
" --------------------------------
"command! Example call TemplateExample()

vnoremap <expr> <SID>SetKeyboardColorVisual SetKeyboardColorVisual()
nnoremap <script> v v<SID>SetKeyboardColorVisual
nnoremap <script> V V<SID>SetKeyboardColorVisual
nnoremap <script> <C-v> <C-v><SID>SetKeyboardColorVisual
vnoremap <script> <LeftDrag> <LeftDrag><SID>SetKeyboardColorVisual

augroup KeyboardColorSwap
    autocmd!
    autocmd InsertEnter * call SetKeyboardColorInsert(v:insertmode)
    autocmd InsertLeave * call ResetKeyboardColor()
    autocmd CursorHold * call ResetKeyboardColor()
augroup END
