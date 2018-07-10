#!/bin/sh

while getopts ":v:u:thd" opt; do
  case $opt in
    v)
      radiovolume=$OPTARG
      export radiovolume
      ;;
    u)
      updatetime=$OPTARG
      export updatetime
      ;;
    t)
      openthread=true
      export openthread
      ;;
    h)
      echo "Use -u and a number to choose the interval in which the timer updates, use -t to open the thread, use -v to set volume (1-100), and use -d if you are testing to run in the current directory."
      exit 0
      ;;
    d)
      dev=true
      ;;
    \?)
      echo "Invalid option: -$OPTARG. Use radiocli -h for help."
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument. Use radiocli -h for help."
      exit 1
      ;;
  esac
done
pyver=`python -c 'import sys; print("%i" % (sys.hexversion<0x03000000))'`
if [ $pyver -eq 0 ]; then
	if [ $dev ]; then
    python radio.py
  else
    python /opt/r-a-d.io-cli/radio.py
  fi
else 
	if [ $dev ]; then
    python3 radio.py
  else
    python3 /opt/r-a-d.io-cli/radio.py
  fi
fi