## for pytest, there is a name convention that needs to be used

## for .py file name, it could be either test_*.py OR *_test.py

## for any method or function, start with the keyword "test"

## examples are given below

## vscode or any IDE needs a framework to work with pytest

import pytest

def testlogin():
    print("testing login")

def testlogout():
    print("testing logout")
