#!/bin/bash
#title          :translate.sh
#description    :Translate Three Address Code into Jasmin(JAVA) Bytecode
#author         :Joao Francisco Martins & Pedro Dalla Vecchia Chaves
#date           :11.11.2017
#usage          :bash translate.sh
#bash_version   :GNU bash, version 4.4.0(1)-release
#==============================================================================

translator_dir=$(pwd)"/code/translator"
krakatau_dir=$(pwd)"/tools/Krakatau"
input_dir=$(pwd)"/outputs"
output_dir=$(pwd)"/outputs/translated"

mkdir -p "$output_dir"

for input in "$input_dir"/*
do
    output_name="${input##*/}"
    output_name="${output_name%.*}"
    if [[ -f $input ]]; then
        binary_dir="$output_dir/$output_name-bin"
        mkdir -p "$binary_dir"

        echo "Translating $output_name"

        python3 "$translator_dir/translator.py" "$input" > "$output_dir"/"$output_name.j"
        python "$krakatau_dir/assemble.py" -out "$binary_dir" "$output_dir"/"$output_name.j"
        
        echo ""
    fi
done
