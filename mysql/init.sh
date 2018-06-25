#!/bin/bash

export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"

#java -jar /usr/local/lib/antlr-4.7.1-complete.jar -visitor -Dlanguage=Python2 MySqlLexer.g4
#java -jar /usr/local/lib/antlr-4.7.1-complete.jar -visitor -Dlanguage=Python2 MySqlParser.g4

java -jar /usr/local/lib/antlr-4.7.1-complete.jar -o python3 -listener -visitor -Dlanguage=Python3 MySqlLexer.g4
java -jar /usr/local/lib/antlr-4.7.1-complete.jar -o python3 -listener -visitor -Dlanguage=Python3 MySqlParser.g4

java -jar /usr/local/lib/antlr-4.7.1-complete.jar -o java MySqlLexer.g4
java -jar /usr/local/lib/antlr-4.7.1-complete.jar -o java MySqlParser.g4
