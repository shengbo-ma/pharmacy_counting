#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
GRADER_ROOT=$(dirname ${BASH_SOURCE})

PROJECT_PATH=${GRADER_ROOT}/..

python3 ./src/pharmacy_counting.py ./input/itcont.txt ./output/top_cost_drug.txt
