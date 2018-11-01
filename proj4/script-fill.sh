#!/bin/sh

PROJECT_BASE='../../Downloads/nand2tetris'
FOLDER_SUFFIX_REGEX='_(proj|hw)4'
PROJECT_INDEX='04/fill'
TOOL='CPUEmulator.sh'

python ../script.py --max-score 66.67 "$PROJECT_BASE" "$PROJECT_INDEX" "$TOOL" "$FOLDER_SUFFIX_REGEX"
