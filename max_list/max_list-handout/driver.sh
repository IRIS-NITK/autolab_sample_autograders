#!/bin/bash
echo "Started running test cases"
score=0
for i in {1..2}
do
  if out=$(python3 max_list.py "$(cat input-${i}.txt)");
  then
    if [ "$out" == "$(cat output-$i.txt)" ];
    then
      ((score=score+50))
    fi
  fi
done
echo "{\"scores\": {\"Find max element\": $score}}"
