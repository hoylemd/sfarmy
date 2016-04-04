#! /bin/bash

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
