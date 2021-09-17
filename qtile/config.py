### sav3d's Qtile Config ###
# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "kitty"      # My terminal of choice
myBrowser = "librewolf" # My terminal of choice
myDmenu = "dmenu_run -c -bw 2 -l 20 -g 4 -p 'Run'" #dmenu
myEditor = "atom" #atom
myFile = "pcmanfm" #pcmanfm
myGFX = "gimp" #gimp
mySVG = "inkscape"
myOffice = "libreoffice"
myLogOut = "arcolinux-logout"
myWallpaper = "dwall -s earth"
myStats = "urxvt -T 'bpytop' -e bpytop"
myMath = "galculator"
myUpdate = "pamac-manager"
myCloud = "/home/sav3d/Applications/Nextcloud-3.3.1-x86_64_332d890d59fed28c70f0e58f2a1b04f3.AppImage"

keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod], "r",
             lazy.spawn(myWallpaper),
             desc='dwall -s earth'
             ),   
         Key([mod], "h",
             lazy.spawn(myStats),
             desc='bpytop'
             ), 
         Key([mod], "c",
             lazy.spawn(myMath),
             desc='galculator'
             ), 
         Key([mod], "n",
             lazy.spawn(myCloud),
             desc='Nextcloud'
             ),            
         Key([mod], "d",
             lazy.spawn(myDmenu),
             desc='Run Launcher'
             ),
         Key([mod], "u",
             lazy.spawn("ulauncher"),
             desc='Run ULauncher'
             ),
         Key([mod], "g",
             lazy.spawn(myGFX),
             desc='gimp'
             ),
         Key([mod], "o",
             lazy.spawn(myOffice),
             desc='libreoffice'
             ), 
         Key([mod], "i",
             lazy.spawn(mySVG),
             desc='gimp'
             ),  
          Key([mod], "x",
             lazy.spawn(myLogOut),
             desc='logout'
             ),         
         Key([mod], "w",
             lazy.spawn(myBrowser),
             desc='librewolf'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "Return",
             lazy.spawn(myFile),
             desc='pcmanfm'
             ),
         #Key([mod, "shift"], "q",
           #  lazy.shutdown(),
            # desc='Shutdown Qtile'
            # ),
         Key([mod], "e",
             lazy.spawn(myEditor),
             desc='atom'
             ),
         
         ### Window controls
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod, "shift"], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod, "shift"], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
       
         
]

group_names = [("WWW", {'layout': 'monadtall'}),
               ("DEV", {'layout': 'monadtall'}),
               ("SYS", {'layout': 'monadtall'}),
               ("DOC", {'layout': 'monadtall'}),
               ("MISC", {'layout': 'monadtall'}),
               ("CHAT", {'layout': 'monadtall'}),
               ("MUS", {'layout': 'monadtall'}),
               ("VID", {'layout': 'monadtall'}),
               ("GFX", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 3,
                "margin": 8,
                "border_focus": "#51afef",
                "border_normal": "1D2330"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = "1c1f24",
         active_bg = "51afef",
         active_fg = "000000",
         inactive_bg = "a9a1e1", ##LOOK AT THIS LATER
         inactive_fg = "1c1f24", ##LOOK AT THIS LATER
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**layout_theme)
]

colors = [["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#51afef", "#51afef"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#807E7E", "#807E7E"], # color for the 'even widgets'
          ["#51afef", "#51afef"], # window name
          ["#ecbbfb", "#ecbbfb"]] # backbround for inactive screens

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Image(
                       filename = "/home/sav3d/face.png",
                       scale = "False",
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myDmenu)}
                       ),
             widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 9,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[4],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[2],
                       this_screen_border = colors [5],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[5],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Prompt(
                       prompt = prompt,
                       font = "Ubuntu Mono",
                       padding = 10,
                       foreground = colors[3],
                       background = colors[1]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              widget.Systray(
                       background = colors[0],
                       padding = 5
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[0],
                       padding = -12,
                       fontsize = 60
                       ),
              widget.Net(
                       interface = "wlan1",
				       format = '{down} ↓↑ {up}  ',
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0
                       ),
		      widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = -12,
                       fontsize = 60
                       ),         
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[0],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Battery(
                       full_char = "=",
                       #hide_threshold = "1",
                       format = "{percent:2.0%}",
                       update_interval = "60",
                       foreground = colors[0],
                       background = colors[4],
                       padding = 5
                       ),
              
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[0],
                       padding = -12,
                       fontsize = 60
                       ),
              widget.TextBox(
                       text = "",
                       padding = 0,
                       foreground = colors[2],
                       background = colors[0],
                       fontsize = 30
                       ),
              widget.ThermalSensor(
                       foreground = colors[2],
                       background = colors[0],
                       threshold = 90,
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = -12,
                       fontsize = 60
                       ),
              widget.TextBox(
                       text = "⟳",
                       padding = 2,
                       foreground = colors[0],
                       background = colors[4],
                       fontsize = 25
                       ),
              widget.CheckUpdates(
                       update_interval = 1000,
                       distro = "Arch_checkupdates",
                       display_format = "{updates} Updates",
                       foreground = colors[2],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                       background = colors[4]
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[0],
                       padding = -12,
                       fontsize = 60
                       ),
              widget.TextBox(
                       text = "",
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0,
                       fontsize = 30
                       ),
              widget.Memory(
                       foreground = colors[2],
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e bpytop')},
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = -12,
                       fontsize = 60
                       ),
              widget.CPU(
                       #app_key = "74ca44597e7741a1eef59f4fb808fa6a",
                       #weather_0_icon
                       #metric = "false",
                       #cityid = "5313457",
                       #update_interval = "600",
                       #fmt = {bold},
                       foreground = colors[0],
                       background = colors[4],
                       padding = 0
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[0],
                       padding = -12,
                       fontsize = 60
                       ),
              widget.Volume(
                       foreground = colors[2],
                       background = colors[0],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = -12,
                       fontsize = 60
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[4],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colors[0],
                       background = colors[4],
                       padding = 3
                       ),
              widget.TextBox(
                       text = ' ',
                       background = colors[4],
                       foreground = colors[0],
                       padding = -12,
                       fontsize = 60
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[0],
                       format = "%A, %B %d - %I:%M%p "
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    #del widgets_screen1[7:8]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=25)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=25))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
