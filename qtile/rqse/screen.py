from libqtile import bar, widget
from libqtile.config import Screen
from rqse.color import Mocha

__all__ = ("screens", "widget_defaults", "extension_defaults")

widget_defaults = dict(font="iosevka", fontsize=13, padding=10, background=Mocha.BASE)
extension_defaults = widget_defaults.copy()


def _separate(bg: str, fg: str) -> widget.TextBox:
    return widget.TextBox(
        text="（",
        background=bg,
        foreground=fg,
        padding=-20,
        fontsize=71,
    )


def _set_defaults(rose: bool = False) -> dict:
    col = {"foreground": Mocha.MANTLE}

    if rose:
        col["background"] = Mocha.ROSEWATER
    else:
        col["background"] = Mocha.RED

    return col


screens = [
    Screen(
        wallpaper="~/.config/qtile/wallpaper.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method="line",
                    highlight_color=[Mocha.BASE, Mocha.BASE],
                    active=Mocha.ROSEWATER,
                    this_current_screen_border=Mocha.RED,
                    center_aligned=False,
                ),
                widget.Prompt(foreground=Mocha.ROSEWATER, prompt="➜ "),
                widget.Spacer(),
                _separate(Mocha.BASE, Mocha.ROSEWATER),
                widget.Clock(**_set_defaults(rose=True), format="🕑 %H:%M"),
                _separate(Mocha.ROSEWATER, Mocha.RED),
                widget.Memory(**_set_defaults(), measure_mem="G"),
                _separate(Mocha.RED, Mocha.ROSEWATER),
                widget.Net(
                    **_set_defaults(rose=True), prefix="M", format="{down} ⥯{up}"
                ),
                _separate(Mocha.ROSEWATER, Mocha.RED),
                widget.CPU(**_set_defaults(), format="CPU {freq_current}GHz"),
                _separate(Mocha.RED, Mocha.ROSEWATER),
                widget.PulseVolume(
                    **_set_defaults(rose=True), fmt="Vol {}", volume_app="pavucontrol"
                ),
                _separate(Mocha.ROSEWATER, Mocha.RED),
                widget.QuickExit(
                    **_set_defaults(),
                    default_text="⏻ ",
                    padding=7,
                    fontsize=15,
                    countdown_format="{}s"
                ),
            ],
            size=30,
            margin=[8, 8, 1, 8],
        ),
    ),
]
