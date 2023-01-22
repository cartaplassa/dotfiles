from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import psutil
from subprocess import call
from libqtile.utils import guess_terminal
from datetime import datetime


current_theme = 'nord'

# def scroll_themes(themes: dict[str, dict]):
#     global current_theme
#     ki = dict()
#     ik = dict()
#     for i, k in enumerate(themes):
#         ki[k] = i   # dictionary index_of_key
#         ik[i] = k   # dictionary key_of_index
#     next = ki[current_theme] + 1
#     current_theme = ik[next] if next in ik else ik[0]

BAR_SIZE=20
BAR_COLOR="#8b0c15"
TRANSPARENT="#00000000"
BLACK="#000000"
WHITE="#ffffff"
GRAY="#808080"
# SPACER_CHAR=" "
SPACER_CHAR = ""
SPACER_HEIGHT=32 
SPACER_PADDING=-5

colors = dict(
    white = "#ffffff",
    gray = "#808080",
    black = "#000000",
    bordeax = "#8b0c15",
    lush = "#336600",
    golden = "#fede00",
    corall = "#fda276",
    pink = "#f06b8e",
    light_purple = "#a54080",
    dark_purple = "#68367b",
    sky_blue = "#4d65a4",
    terminal_green = "#8fbcbb",
    # Nord palette
    polarnight0 = "#2e3440",
    polarnight1 = "#3b4252",
    polarnight2 = "#434c5e",
    polarnight3 = "#4c566a",
    snowstorm0 = "#d8dee9",
    snowstorm1 = "#e5e9f0",
    snowstorm2 = "#eceff4",
    frost0 = "#8fbcbb",
    frost1 = "#88c0d0",
    frost2 = "#81a1c1",
    frost3 = "#5e81ac",
    aurora_red = "#bf616a",
    aurora_orange = "#d08770",
    aurora_yellow = "#ebcb8b",
    aurora_green = "#a3be8c",
    aurora_purple = "#b48ead"
)

themes = dict(
    
    sunrise = dict(
        widget1 = dict(
            foreground = colors['black'],
            background = colors['golden']
        ),
        widget2 = dict(
            foreground = colors['white'],
            background = colors['corall']
        ),
        widget3 = dict(
            foreground = colors['white'],
            background = colors['pink']
        ),
        widget4 = dict(
            foreground = colors['white'],
            background = colors['light_purple']
        ),
        widget5 = dict(
            foreground = colors['white'],
            background = colors['dark_purple']
        ),
        groupbox = dict(
            active = colors['white'],
            inactive = colors['pink'],
            highlight_color = colors['pink'],
            background = colors['light_purple']
        ),
        status_bar = dict(
            border_width=[0, 0, 0, 0],
            border_color=["#000000", "#000000", "#000000", "#000000"]
        ),
        bar_item = dict(
            foreground = colors['white'],
            background = colors['sky_blue']
        ),
        wallpaper = '~/Pictures/Wallpapers/sunrise.jpg'
    ),
    
    shodan = dict(
        widget1 = dict(
            foreground = colors['black'],
            background = colors['terminal_green']
        ),
        widget2 = dict(
            foreground = colors['white'],
            background = colors['black']
        ),
        widget3 = dict(
            foreground = colors['black'],
            background = colors['terminal_green']
        ),
        widget4 = dict(
            foreground = colors['white'],
            background = colors['black']
        ),
        widget5 = dict(
            foreground = colors['black'],
            background = colors['terminal_green']
        ),
        groupbox = dict(
            active = colors['white'],
            inactive = colors['black'],
            highlight_color = colors['black'],
            background = colors['terminal_green'],
            block_highlight_text_color = colors['terminal_green']
        ),
        status_bar = dict(
            border_width=[1, 0, 1, 0], 
            border_color=[colors["terminal_green"], "#000000", colors["terminal_green"], "#000000"]
        ),
        bar_item = dict(
            foreground = colors['white'],
            background = colors['black']
        ),
        wallpaper = '~/Pictures/Wallpapers/shodan-nordic.jpg'
    ),
    
    nord = dict(
        widget1 = dict(
            foreground = colors['polarnight0'],
            background = colors['aurora_red']
        ),
        widget2 = dict(
            foreground = colors['polarnight0'],
            background = colors['aurora_orange']
        ),
        widget3 = dict(
            foreground = colors['polarnight0'],
            background = colors['aurora_yellow']
        ),
        widget4 = dict(
            foreground = colors['polarnight0'],
            background = colors['aurora_green']
        ),
        widget5 = dict(
            foreground = colors['polarnight0'],
            background = colors['aurora_purple']
        ),
        groupbox = dict(
            active = colors['snowstorm0'],
            inactive = colors['polarnight1'],
            highlight_color = colors['polarnight2'],
            this_current_screen_border = colors['polarnight2'],
            background = colors['frost3'],
            block_highlight_text_color = colors['snowstorm0']
        ),
        status_bar = dict(
            border_width=[0, 0, 0, 0], 
            border_color=[colors["terminal_green"], "#000000", colors["terminal_green"], "#000000"]
        ),
        bar_item = dict(
            foreground = colors['snowstorm0'],
            background = colors['polarnight1']
        ),
        wallpaper = '~/Pictures/Wallpapers/misc/wallhaven-4d93jg.jpg'
    )
)

def datestamp():
    now = datetime.now()
    text = f'[[{str(now.date())}]] {now.time().isoformat(timespec="minutes")} '
    return text

def timestamp():
    return f'{datetime.now().time().isoformat(timespec="minutes")} '

mod = "mod4"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key(
        [mod], "h", lazy.layout.left(), 
        desc="Move focus to left"
        ),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "e", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.spawn("librewolf"), desc="Launch librewolf"),
    Key([mod], "z", lazy.spawn("dm-tool lock"), desc="Lock screen"),
    Key([], "Print", lazy.spawn("scrot 'screenshot-%Y-%m-%d-%H%M%S.jpg' -e 'mv $f ~/Pictures/Screenshots'"), desc="Take screenshot"),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    # Key([mod], "a", scroll_themes(themes), desc="Scroll themes"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn("rofi -show drun -theme rounded-nord-dark"), desc="Launch rofi"),
    # Timestamp commands
    Key([mod], "d", lazy.spawn(f'xdotool keyup meta+d sleep 0.4 type "{datestamp()}"'), desc="Insert current date"),
    Key([mod], "t", lazy.spawn(f'xdotool keyup meta+d sleep 0.4 type "{timestamp()}"'), desc="Insert current time")
]

groups = [Group(i) for i in [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "]]
group_hotkeys = "123456789"

for icon, hotkey in zip(groups, group_hotkeys):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                hotkey,
                lazy.group[icon.name].toscreen(),
                desc=f"Switch to group {icon.name}"
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                hotkey,
                lazy.window.togroup(icon.name, switch_group=False),
                desc=f"Switch to & move focused window to group {icon.name}"
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        margin=5, 
        border_focus=themes[current_theme]['groupbox']['background'],
        border_focus_stack=themes[current_theme]['groupbox']['background'], 
        border_width=1
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Cantarell",
    fontsize=14,
    padding=0,
)
extension_defaults = widget_defaults.copy()


def get_widgets(primary=False):
    widgets = [
        # widget.CurrentLayout(),
        widget.GroupBox(
            highlight_method='block',
            # margin_x = 10,
            **themes[current_theme]['groupbox']
        ),
        # widget.TextBox(
        #    text="    ", 
        #    padding=-1, 
        #    fontsize=BAR_SIZE, 
        #    foreground=themes[current_theme]['groupbox']['background'],
        #    background=themes[current_theme]['bar_item']['background']
        #),
        widget.Prompt(**themes[current_theme]['bar_item']),
        widget.WindowName(**themes[current_theme]['bar_item']),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
            **themes[current_theme]['bar_item']
        ),
        # widget.TextBox("default config", name="default"),
        # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.Systray(**themes[current_theme]['bar_item']),
        widget.KeyboardLayout(
            configured_keyboards=['us', 'ru'],
            **themes[current_theme]['bar_item']
        ),
        widget.TextBox(
            text=SPACER_CHAR, 
            padding=SPACER_PADDING, 
            fontsize=SPACER_HEIGHT, 
            foreground=themes[current_theme]['widget5']['background'],
            background=themes[current_theme]['bar_item']['background']
        ),
        widget.Net(
            fmt = ' net: {}',
            format = '{down} ↓↑{up}',
            width = 170,
            **themes[current_theme]['widget5'],
        ),
        widget.TextBox(
            text=SPACER_CHAR, 
            padding=SPACER_PADDING, 
            fontsize=SPACER_HEIGHT, 
            foreground=themes[current_theme]['widget4']['background'],
            background=themes[current_theme]['widget5']['background']
        ),
        widget.Memory(
            fmt=" ram: {}",
            format='{MemPercent}% ({MemUsed:.2f}/{MemTotal:.2f}{mm})',
            measure_mem='G',
            width = 160,
            **themes[current_theme]['widget4']
        ),
        widget.TextBox(
            text=SPACER_CHAR, 
            padding=SPACER_PADDING, 
            fontsize=SPACER_HEIGHT, 
            foreground=themes[current_theme]['widget3']['background'],
            background=themes[current_theme]['widget4']['background']
        ),
        widget.DF(
            fmt=" rom: {}",
            format='{r:.1f}% ({uf:.1f}/{s}{m})',
            visible_on_warn=False,
            width = 150,
            **themes[current_theme]['widget3']
        ),
        widget.TextBox(
            text=SPACER_CHAR, 
            padding=SPACER_PADDING, 
            fontsize=SPACER_HEIGHT, 
            foreground=themes[current_theme]['widget2']['background'],
            background=themes[current_theme]['widget3']['background']
        ),
        widget.Battery(
            charge_char=" charge+",
            discharge_char=" charge-",
            empty_char=" charge0",
            full_char=" chargeF",
            format='{char} {percent:2.0%}',
            low_foreground=BAR_COLOR,
            low_percentage=0.1,
            width = 100,
            **themes[current_theme]['widget2']
        ),
        widget.TextBox(
            text=SPACER_CHAR, 
            padding=SPACER_PADDING, 
            fontsize=SPACER_HEIGHT, 
            foreground=themes[current_theme]['widget1']['background'],
            background=themes[current_theme]['widget2']['background']
        ),
        widget.Clock(
            fmt=" time: {}",
            format="%A, %B %-d, %H:%M:%S",
            width = 250,
            **themes[current_theme]['widget1']
        ),
        widget.TextBox(
            text=" ", 
            padding=2, 
            fontsize=SPACER_HEIGHT, 
            **themes[current_theme]['widget1']
        ),
        # widget.QuickExit(),
    ]
    return widgets

screens = [
    Screen(
        top=bar.Bar(
            get_widgets(primary=True),
            size=BAR_SIZE,
            **themes[current_theme]["status_bar"]
        ),
        wallpaper=themes[current_theme]['wallpaper'],
        wallpaper_mode='fill'
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry")
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# @hook.subscribe.startup_once
# def start_once():
#     call('picom')

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
