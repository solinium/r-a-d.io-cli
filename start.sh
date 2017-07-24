#!/bin/sh

while getopts ":t:" opt; do
  case $opt in
    t)
      frequency=$OPTARG
      export frequency
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

python3 audio.py &
python3 cli.py