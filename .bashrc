#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'

# https://askubuntu.com/a/1128771
PROMPT_COMMAND=build_prompt

build_prompt() {
  EXIT=$?               # save exit code of last command
  red='\[\e[0;31m\]'    # colors
  green='\[\e[0;32m\]'
  cyan='\[\e[1;36m\]'
  reset='\[\e[0m\]'
  PS1='${debian_chroot:+($debian_chroot)}'  # begin prompt

  if [ $EXIT != 0 ]; then  # add arrow color dependent on exit code
    PS1+="$red"
  else
    PS1+="$green"
  fi

  PS1+="➜$reset  $cyan\w$reset \\$ " # construct rest of prompt
}
