#!/bin/sh

PROJECT_BASE='../../Downloads/nand2tetris'
FOLDER_SUFFIX_REGEX='_(proj|hw)5'
PROJECT_INDEX='05'
TOOL='HardwareSimulator.sh'

python ../script.py "$PROJECT_BASE" "$PROJECT_INDEX" "$TOOL" "$FOLDER_SUFFIX_REGEX"
