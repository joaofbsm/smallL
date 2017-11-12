#!/bin/bash
#title          :execute.sh
#description    :Execute the created tests for the SmallL compiler front-end
#author         :Joao Francisco Martins & Pedro Dalla Vecchia Chaves
#date           :27.10.2017
#usage          :bash execute.sh
#bash_version   :GNU bash, version 4.4.0(1)-release
#==============================================================================

tests_dir=$(pwd)"/tests"
outputs_dir=$(pwd)"/outputs"

for test in "$tests_dir"/*
do
    output_name="${test##*/}"
    if [[ -f $test ]]; then
        echo "Compiling $output_name"
        java code.main.Main < "$test" > "$outputs_dir"/"$output_name"
    fi
done
