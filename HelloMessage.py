#!/usr/bin/python

import sys

print("Hello Sir")
if len(sys.argv) == 2:
    result = len(sys.argv[1])
    parameterWord = sys.argv[1]
    if result <= 0:
        print("length eqauls zero")

    print("The enter parameter is called")
    print(parameterWord)
else:
    print("Not Right amount of parameters")



