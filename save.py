#!/usr/bin/env python
# * coding: utf-8 *

import linecache
import codecs
import base64

import six



def init(file_text):
    plik = open(file_text, "a")
    if plik.readable():
        pass
    else:
        plik = open(file_text, "a")


def read(file_text, number_line):
    try:
        file = open(file_text, 'r+').read()
        lines = file.split('\n')

    except Exception:
        init(file_text)
        read_no_init(file_text, number_line)
    try:
        if lines[number_line - 1] == "":
            return ""
        else:
            return lines[(number_line - 1)]

    except Exception:
        read = linecache.getline(file_text, number_line)

        return read

def read_encrypted(file_text, number_line):
    try:
        file = open(file_text, 'r+').read()
        lines = file.split('\n')

    except Exception:
        init(file_text)
        read_no_init(file_text, number_line)
    try:
        if lines[number_line - 1] == "":
            return ""
        else:
            return (base64.b64decode(lines[(number_line - 1)]).decode())


    except Exception:
        read = linecache.getline(file_text, number_line)

        return read

def write(file_text, write):
    plik = codecs.open(file_text, "a")
    plik.write(write + "\n")
    plik.close()

def write_encrypted(file_text, write):
    if six.PY3:
        source = write.encode('utf-8')
    content = base64.b64encode(source).decode('utf-8')
    plik = codecs.open(file_text, "a")
    plik.write(content + "\n")
    plik.close()

def number_lines(file_text):
    count = len(open(file_text, 'rU').readlines())
    return count


def clear(file_text):
    open(file_text, "w+")

def read_no_init(file_text, number_line):
    read(file_text, number_line)



