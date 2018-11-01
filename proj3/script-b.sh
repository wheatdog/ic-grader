#!/bin/sh

PROJECT_BASE='../../Downloads/nand2tetris'
FOLDER_SUFFIX_REGEX='_(proj|hw)3'
PROJECT_INDEX='03/b'
TOOL='HardwareSimulator.sh'

python ../script.py --max-score 37.5 "$PROJECT_BASE" "$PROJECT_INDEX" "$TOOL" "$FOLDER_SUFFIX_REGEX"
