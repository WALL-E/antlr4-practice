#!/bin/bash

export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"

javac *.java
java org.antlr.v4.gui.TestRig JSON json -tree -gui
