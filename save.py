#!/usr/bin/env python
# * coding: utf-8 *

import linecache
import codecs
import base64

class save():

    def __init__(self):
        pass

    def __del__(self):
        pass

    def init(self, file_text):
        plik = open(file_text, "a")
        if plik.readable():
            pass
        else:
            plik = open(file_text, "a")


    def read(self, file_text, number_line):
        try:
            file = open(file_text, 'r+').read()
            lines = file.split('\n')

        except Exception:
            self.init(file_text)

        try:


            if lines[number_line - 1] == "":
                return ""
            else:
                return lines[(number_line - 1)]

        except Exception:
            read = linecache.getline(file_text, number_line)

            return read


    def read_no_init(self, file_text, number_line):
        self.read(file_text, number_line)


    def write(self, file_text, write):
        plik = codecs.open(file_text, "a")
        plik.write(str(write) + "\n")
        plik.close()

    def number_lines(self, file_text):
        count = len(open(file_text, 'rU').readlines())
        return count

    def clear(self, file_text):
        open(file_text, "w+")



class save_encrypted():


    def read(self, file_text, number_line):
        try:
            file = open(file_text, 'r+').read()
            lines = file.split('\n')

        except Exception:
            self.init(file_text)
            self.read_no_init(file_text, number_line)
        try:
            if lines[number_line - 1] == "":
                return ""
            else:
                return (base64.b64decode(lines[(number_line - 1)]).decode())


        except Exception:
            read = linecache.getline(file_text, number_line)

            return read
    def read_no_init(self, file_text, number_line):
        self.read(file_text, number_line)


    def write(self, file_text, write):
        source = str(write).encode('utf-8')
        content = base64.b64encode(source).decode('utf-8')
        plik = codecs.open(file_text, "a")
        plik.write(content + "\n")
        plik.close()


TEST_MODE = 0
if TEST_MODE == 1:
    save = save()
    save_e = save_encrypted()
    save.init("TEST.TEST")
    save.clear("TEST.TEST")
    #save.write("TEST.TEST", "TEST")
    #print(save.read("TEST.TEST", 1))
    #print(save.number_lines("TEST.TEST"))
    save_e.write("TEST.TEST", "123456789_QWERTYUIOPLKJHGFDSAZXCVBNM_qwertyuioplkjhgfdsazxcvbnm_łó€ęąśłńćźż_)!@#$%^&*()__-+=}]{[:;"'|\?/>.<,')
    print(save_e.read("TEST.TEST", 1))








