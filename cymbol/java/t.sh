#!/bin/bash

export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"

javac *.java
cat t.cymbol | java org.antlr.v4.gui.TestRig CYMBOL root -tree -gui
