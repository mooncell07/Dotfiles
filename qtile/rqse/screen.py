from libqtile import bar, widget
from libqtile.config import Screen
from rqse.color import Mocha

__all__ = ("screens", "widget_defaults", "extension_defaults")

widget_defaults = dict(
    font="RobotoMono Nerd Font", fontsize=12, padding=10, background=Mocha.BASE
)
extension_defaults = widget_defaults.copy()


class W_Logic:
    def __init__(self, color):
        self.color = color
        self.state = 0

    def reset(self):
        self.state = 0

    def set_sep(self) -> widget.TextBox:
        color = self.color

        if not self.state:
            color = color[::-1]
            self.state = 1
        else:
            self.reset()

        return widget.TextBox(
            text="",
            background=color[0],
            foreground=color[1],
            padding=0,
            fontsize=30,
        )

    def set_style(self) -> dict:
        col = {"foreground": Mocha.MANTLE, "fontsize": 14}

        if self.state:
            col["background"] = self.color[0]
        else:
            col["background"] = self.color[1]

        return col


w_logic = W_Logic(color=[Mocha.TEXT, Mocha.FLAMINGO])

screens = [
    Screen(
        wallpaper="~/.config/qtile/wallpaper.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method="line",
                    highlight_color=[Mocha.BASE, Mocha.BASE],
                    active=Mocha.TEXT,
                    this_current_screen_border=Mocha.TEXT,
                    center_aligned=False,
                ),
                widget.Prompt(foreground=Mocha.TEXT, prompt=" "),
                widget.Spacer(),
                widget.TextBox(
                    text="",
                    background=Mocha.BASE,
                    foreground=Mocha.FLAMINGO,
                    padding=0,
                    fontsize=30,
                ),
                widget.Clock(**w_logic.set_style(), format="  %H:%M"),
                w_logic.set_sep(),
                widget.Memory(**w_logic.set_style(), measure_mem="G", fmt=" {}"),
                w_logic.set_sep(),
                widget.CPU(**w_logic.set_style(), format="  {freq_current}GHz"),
                w_logic.set_sep(),
                widget.PulseVolume(
                    **w_logic.set_style(), fmt="墳  {}", volume_app="pavucontrol"
                ),
                w_logic.set_sep(),
                widget.QuickExit(
                    **w_logic.set_style(), default_text="  ", countdown_format="{}s"
                ),
            ],
            size=30,
            margin=[8, 8, 1, 8],
            background="#00000000",
        ),
    ),
]
