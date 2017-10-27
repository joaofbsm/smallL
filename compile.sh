#!/bin/bash
#title          :compile.sh
#description    :Compile the compiler front-end for the SmallL mini-language
#author         :Joao Francisco Martins & Pedro Dalla Vecchia
#date           :27.10.2017
#usage          :bash compile.sh
#bash_version   :GNU bash, version 4.4.0(1)-release
#==============================================================================

javac code/lexer/*.java
javac code/symbols/*.java
javac code/inter/*.java
javac code/parser/*.java
javac code/main/Main.java