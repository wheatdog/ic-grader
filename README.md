# IC-grader (nand2tetris part)

A partial auto-grader for projects from nand2tetris in NTU CSIE1000. All codes are only tested on Linux.

## Prerequire

- 7z (for `ceiba-extract.sh`)
- python3 (for `script.py`)
- [Nand2tetris Software Suite](https://www.nand2tetris.org/software)
    - Download and extract it somewhere
    - Make sure `*.sh` in `nand2tetris/tools/` are executable. (Use `chmod +x` or so)

## Usage

### `ceiba-extract.sh`

It will find compressed files (rar or zip) in the current folder and extract them according to the speicial format of ceiba file-naming magic.
For expamle, the content of `hw116345_b03902000_5ee9eefb3983512_1.zip` will be extracted into `b03902000`.

### `script.py`

You can run `script.py --help` to see more information
