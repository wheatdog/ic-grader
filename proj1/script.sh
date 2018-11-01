#!/bin/sh

PROJECT_BASE='../../Downloads/nand2tetris'
FOLDER_SUFFIX_REGEX='_(proj|hw)1'
PROJECT_INDEX='01'
TOOL='HardwareSimulator.sh'

python ../script.py "$PROJECT_BASE" "$PROJECT_INDEX" "$TOOL" "$FOLDER_SUFFIX_REGEX"
