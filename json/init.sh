#!/bin/bash

export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"


java -jar /usr/local/lib/antlr-4.7.1-complete.jar -o java -listener -visitor JSON.g4

java -jar /usr/local/lib/antlr-4.7.1-complete.jar -o python3 -listener -visitor -Dlanguage=Python3 JSON.g4
