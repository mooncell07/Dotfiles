#!/bin/sh

if ! pgrep -x "eww" > /dev/null; then
    eww daemon &
fi

