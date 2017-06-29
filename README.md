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

## Issues

Note: certain vim versions with both +python3 and +python (aka python2)
features enabled might not work either. To get around this either wait for
vim update to fix the issue, let go of python2 for vim or port this plugin to neovim.

## Todo

1. Add special key colors
2. Add macro register key colors
3. Add more keyboard layouts
