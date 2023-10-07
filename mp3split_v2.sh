#!/bin/bash
filename="$1"
#minutes_block=20
minutes_block="$2"

re='^[0-9]+$'
if [ -z "$filename" ] || [ -z "$minutes_block" ] || ! [[ $minutes_block =~ $re ]] ;
then
    echo "ERROR: incorrect/empty parameters."
    echo "Correct syntax: mp3split_v2.sh filename minutes_block"
    exit 1
fi

duration_stamp=$(ffmpeg -i "$filename" 2>&1 | grep Duration | sed 's/^.*Duration: *\([^ ,]*\),.*/\1/g')
title=$(ffmpeg -i "$filename" 2>&1  | grep "title *:" | sed 's/^.*title *: *\(.*\)/\1/g')

echo "----------------------------------------------"
# get minutes as a raw integer number (rounded up)
prefix=$(basename "$filename" .mp3)
echo "Total audio duration =" $duration_stamp
echo "----------------------------------------------"
mins=$(echo "$duration_stamp" | sed 's/\([0-9]*\):\([0-9]*\):\([0-9]*\)\.\([0-9]*\)/\1*60+\2+\3\/60+\4\/60\/100/g' | bc -l | python3 -c "import math; print(int(math.ceil(float(input()))))")
echo "Total audio duration in minutes =" $mins

echo "----------------------------------------------"
ss="0"
count="1"
total_count=$(echo "$mins/$minutes_block"+1 | bc)
echo "Blocks to be produced =" $total_count
echo "----------------------------------------------"

while [ "$ss" -lt "$mins" ]
do
  zcount=$(printf "%05d" $count)
  
  ss_sec=0
  ss_mins=$((ss%60))
  ss_hours=$((ss/60))
    
  if [ $ss_mins != 0 ]
  then
    # putting the count back of 3 seconds to avoid to lose audio between the split files
    ss_sec=57
    ss_mins=$((ss_mins-1))
  fi
  
  ss_stamp=$(printf "%02d:%02d:%02d" $ss_hours $ss_mins $ss_sec)
  
  ffmpeg -i "$filename" -acodec copy -t 00:$minutes_block:00 -ss $ss_stamp -metadata track="$count/$total_count" -metadata title="$title $zcount" "$prefix-$zcount.mp3" 

  echo "----------------------------------------------"  
  echo "Part" $zcount "starting at" $ss_stamp "completed"
  echo "----------------------------------------------"
  ss=$[$ss+$minutes_block]
  count=$[$count+1]
done

echo "SPLIT PROCESS COMPLETED"
echo "----------------------------------------------"
