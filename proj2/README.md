# Workflow

1. cd into this folder
2. download all the compressed files from ceiba and put them here
3. run `../ceiba-extract.sh`
4. change `PROJECT_BASE` and `FOLDER_SUFFIX_REGEX` in `script.sh` if required
5. run `./script.sh > out.1_init.raw`. `out.1_init.raw` will contain all the information you need to grade this project, like the error messages and scores
6. run `grep '\[' out.1_init.raw > out.1_init.score` to list score only
7. if you found "folder format incorrect" in `out.1_init.score`, you can start from 5. again but rename output file to `out.2_fix.raw` or so

