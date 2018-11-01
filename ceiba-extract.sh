#!/bin/sh

for f in $(find * -maxdepth 0 -regextype emacs -regex ".*\(rar\|zip\)"); do
    name=$(echo $f | cut -f2 -d_)
    rm -rf $name && 7z x $f -o$name || break
done
