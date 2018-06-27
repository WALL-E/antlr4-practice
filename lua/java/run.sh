#!/bin/bash

javac *.java
java LoadLua t.lua > t.dot
dot -Tpng -o t.png t.dot
