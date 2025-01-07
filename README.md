# Desktop-Whichkey
This is a menu that provides different options for your desktop shortcuts, as [whichkey does in Neovim](https://github.com/folke/which-key.nvim) (although not as cool and customizable).

This is originally designed for my [i3wm](https://i3wm.org/) deskop, that works very well using [modes](https://i3wm.org/docs/userguide.html#binding_modes), allowing users to have a wider range of key bind options.

The issue with key binds is that sometimes there's many and we can forget what key bind we assigned to some especific rofi menu that we did 3 months ago. Of course we can have a [Rofi menu with our shortcuts](https://github.com/Zeioth/rofi-shortcuts), but this way is faster.

## Instructions

To use this script, you need to create a json with your keybinds (I left mine as an example). And to use it you just need to `python desktop-whichkey.py mode` to activate this; but the goal is to integrate it with our desktop. For i3wm (and Swaymm):

```
# Whichkey for i3 using python (desktop-whichkey.py mode)
set $wkd python ~/.config/i3/scripts/desktop-whichkey.py
set $kme exec killall python ~/.config/i3/scripts/desktop-whichkey.py, exec
set $km exec killall python ~/.config/i3/scripts/desktop-whichkey.py,

# This is an example of how could it be used with an app launcher in i3:
set $mode_apps  Applications
bindsym $mod+a mode "$mode_apps", exec $wkd apps &
mode "$mode_apps" {
    bindsym k exec $kme kate, mode "default"
    bindsym t exec $kme thunderbird, mode "default"
    bindsym u exec $kme thunar, mode "default"
    # […]

    bindsym Escape exec $km mode "default"
    bindsym Return exec $km mode "default"
}
```

![Captura de pantalla_20250107_105419](https://github.com/user-attachments/assets/95a0e290-0658-4a67-8b1d-317e0c3085b0)

The program shows you the menu, so in order to execute each program we call this reminder menu, we can kill it and execute whatever we want or cancel it going back to the "default" mode.

Remember that you don't need to add all your modes to the `keybinds.json` that this script reads. For example, I have a mode to [move between the workspaces using the home row](https://github.com/i3/i3/discussions/6351) of my split keyboard because is more comfortable for me to use, but I don't need a menu to show me what key to press, so I don't need to include this mode into the json file. Also, remember that we can use an AI to automate this process (if you want to use any).
