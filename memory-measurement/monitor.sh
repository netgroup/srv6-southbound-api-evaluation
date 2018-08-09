#!/bin/sh

MAX_SIZE=20000000
MON_FILE=monitor_$(uname -n).dat

monitor(){
  while true
  do
    date >> $MON_FILE
    cat /proc/meminfo >> $MON_FILE
    echo "----------------------" >> $MON_FILE
    cat /proc/slabinfo >> $MON_FILE
    echo "----------------------" >> $MON_FILE
    ps -o pid,comm,stat,time,rss,vsz >> $MON_FILE
    echo "++++++++++++++++++++++" >> $MON_FILE
    fsize=`ls -l $MON_FILE | awk '{print $5}'`
    if [ $fsize -gt $MAX_SIZE ]; then
    	# upload file to TFTP server
      suffix=`cat /proc/uptime | cut -d" " -f1`
      mv $MON_FILE $MON_FILE.$suffix
      # upload to cloud
    fi
    # kmemleak
    kmemleak=/sys/kernel/debug/kmemleak
    [ -r $kmemleak ] && cat $kmemleak > /storage/kmemleak_$(uname -n).out

    sleep 0.5
  done
}

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

monitor
