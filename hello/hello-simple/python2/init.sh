#!/bin/bash

export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"

java -jar /usr/local/lib/antlr-4.7.1-complete.jar -visitor -Dlanguage=Python2 ../Hello.g4
