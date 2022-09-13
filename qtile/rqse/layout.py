from libqtile import layout
from libqtile.config import Click, Drag, Group, Key, Match
from libqtile.lazy import lazy
from rqse.color import Mocha
from rqse.key import keys, mod

__all__ = ("groups", "layouts", "mouse", "floating_layout")


groups = []

for n in range(5):
    name = str(n + 1)
    grp = Group(name, layout="columns", label="⬤")
    groups.append(grp)

    keys.extend(
        [
            Key([mod], name, lazy.group[grp.name].toscreen()),
            Key([mod, "shift"], name, lazy.window.togroup(grp.name)),
        ]
    )


layouts = [
    layout.Columns(
        border_focus=Mocha.ROSEWATER,
        border_normal=Mocha.MANTLE,
        border_width=3,
        margin=6,
    ),
    layout.Max(),
    layout.Matrix(
        border_focus=Mocha.ROSEWATER,
        border_normal=Mocha.MANTLE,
        border_width=3,
        margin=6,
    ),
]


mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ]
)
