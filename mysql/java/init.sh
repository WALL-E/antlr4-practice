#!/bin/bash

export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"

#java -jar /usr/local/lib/antlr-4.7.1-complete.jar -visitor -Dlanguage=Python2 MySqlLexer.g4
#java -jar /usr/local/lib/antlr-4.7.1-complete.jar -visitor -Dlanguage=Python2 MySqlParser.g4

#java -jar /usr/local/lib/antlr-4.7.1-complete.jar -listener -Dlanguage=Python2 MySqlLexer.g4
#java -jar /usr/local/lib/antlr-4.7.1-complete.jar -listener -Dlanguage=Python2 MySqlParser.g4

java -jar /usr/local/lib/antlr-4.7.1-complete.jar ../MySqlLexer.g4
java -jar /usr/local/lib/antlr-4.7.1-complete.jar ../MySqlParser.g4
