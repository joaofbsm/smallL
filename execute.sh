#!/bin/bash
#title          :execute.sh
#description    :Execute the created tests for the SmallL compiler front-end
#author         :Joao Francisco Martins & Pedro Dalla Vecchia
#date           :27.10.2017
#usage          :bash execute.sh
#bash_version   :GNU bash, version 4.4.0(1)-release
#==============================================================================

main_path="/Users/joaofbsm/Documents/UFMG/2017-2/Compiladores/TP2/code/main"
tests_dir="/Users/joaofbsm/Documents/UFMG/2017-2/Compiladores/TP2/tests"
outputs_dir="/Users/joaofbsm/Documents/UFMG/2017-2/Compiladores/TP2/outputs"

for test in "$tests_dir"/*
do
    output_name="${test##*/}"
    echo "Compiling $output_name"
    java code.main.Main < "$test" > "$outputs_dir"/"$output_name"
done