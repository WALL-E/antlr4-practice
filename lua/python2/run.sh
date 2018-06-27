#!/bin/bash

./main.py > t.dot
dot -Tpng -o t.png t.dot
