# vim-razer

## Pre-installation

Make sure vim was compiled with python3
Run the following command
```
vim --version | grep python3
```
and look for +python3 or +python3/dyn.
If you see a - instead of a + then you need to reinstall vim with the python3 feature enabled.

Once you are sure you got vim with python3, install the open source [razer-drivers](https://terrycain.github.io/razer-drivers/#download) 
for your desired linux distribution.

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/DanManN/vim-razer ~/.vim/bundle/vim-razer`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/DanManN/vim-razer'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/DanManN/vim-razer'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/DanManN/vim-razer'` to .vimrc
  - Run `:PlugInstall`

or for Arch-Linux users vim-razer is also available as an AUR package: [vim-razer-git](https://aur.archlinux.org/packages/vim-razer-git/)<sup>AUR<sup>

## Useage

Once everything is installed just open vim and admire the colors.

## Known Issues

Certain vim versions with both +python3/dyn and +python/dyn (aka python2)
features enabled at the same time might not work with this plugin. 
This is a bug with vim which will hopefully be resolved soon.
The only workaround I found so far is to disable python2 and hope no other plugins depend on it.
You could also try to port this plugin to neovim which shouldn't have that issue.

## Todo

1. Get macro mode to work from visual mode
2. Add more keyboard layouts.
You can help me with that by doing one of the following.
- If you have a keyboard that isn't supported yet run mapLayout.py and send me the output so I can add it. 
- Send a pull request if you add the layout to the plugin/layout.py file.
