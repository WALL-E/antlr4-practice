#!/bin/bash

export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"


java -jar /usr/local/lib/antlr-4.7.1-complete.jar -o java -listener -visitor Cymbol.g4

#java -jar /usr/local/lib/antlr-4.7.1-complete.jar -o python2 -listener -visitor -Dlanguage=Python2 Cymbol.g4

#java -jar /usr/local/lib/antlr-4.7.1-complete.jar -o python3 -listener -visitor -Dlanguage=Python3 Cymbol.g4
