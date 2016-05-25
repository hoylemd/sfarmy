#! /bin/bash

# Prompt the user for input
#  usage: $(read_reject_blank "<prompt>" "<error>")
#  <prompt> will be displayed to the user when asking for input
#  <error> will be displayed if the user does not enter anything
#  If the user doesn't enter anything, they will be re-prompted until they do.
read_reject_blank () {
  prompt=$1
  error=$2

  if [ -z "$error" ]; then
    error="Please enter a string: "
  fi

  entered=""

  while [ -z "$entered" ]; do
    read -p "$prompt" entered
    if [ "$entered" ]; then
      break;
    else
      >&2 echo "$error"
    fi
  done

  echo $entered
}

env_name=$(read_reject_blank)
