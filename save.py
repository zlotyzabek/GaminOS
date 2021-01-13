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

    def write_no_new_line(self, file_text, write):
        plik = codecs.open(file_text, "a")
        plik.write(str(write))
        plik.close()

    def number_lines(self, file_text):
        count = len(open(file_text, 'r').readlines())
        return count

    def clear(self, file_text):
        open(file_text, "w+")

    def clear_and_write(self, file_text, write):
        open(file_text, "w+")
        plik = codecs.open(file_text, "a")
        plik.write(str(write) + "\n")
        plik.close()


    def coppy_file(self, file_text, new_coppy_file_text):
        number_yea = 1
        for liczba in range(1, save.number_lines(file_text)):
            number_yea +=1
            save.write(new_coppy_file_text, save.read(file_text, liczba))
        save.write_no_new_line(new_coppy_file_text, save.read(file_text, number_yea))

class save_encrypted():

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
            self.read_no_init(file_text, number_line)
        try:
            if lines[number_line - 1] == "":
                return ""
            else:
                return (base64.b64decode(lines[(number_line - 1)]).decode())


        except Exception:
            read = base64.b64decode(linecache.getline(file_text, number_line)).decode()

            return read
    def read_no_init(self, file_text, number_line):
        self.read(file_text, number_line)


    def write(self, file_text, write):
        source = str(write).encode('utf-8')
        content = base64.b64encode(source).decode('utf-8')
        plik = codecs.open(file_text, "a")
        plik.write(content + "\n")
        plik.close()


    def clear_and_write(self, file_text, write):
        open(file_text, "w+")
        source = str(write).encode('utf-8')
        content = base64.b64encode(source).decode('utf-8')
        plik = codecs.open(file_text, "a")
        plik.write(content + "\n")
        plik.close()

    def clear_and_write(self, file_text, write):
        open(file_text, "w+")
        source = str(write).encode('utf-8')
        content = base64.b64encode(source).decode('utf-8')
        plik = codecs.open(file_text, "a")
        plik.write(content + "\n")
        plik.close()


TEST_MODE = 0
if TEST_MODE == 1:
    save = save()
    save_e = save_encrypted()
   # save.init("TEST.TEST")
    save.clear("NowaKopia.txt")
   # save.write("TEST.TEST", "TEST")
   # print(save.read("TEST.TEST", 1))
   # save_e.write("TEST.TEST", "123456789_QWERTYUIOPLKJHGFDSAZXCVBNM_qwertyuioplkjhgfdsazxcvbnm_łó€ęąśłńćźż_)!@#$%^&*()__-+=}]{[:;"'|\?/>.<,')
    #print(save_e.read("TEST.TEST", 2))
   #print(save.number_lines("TEST.TEST"))
    save.coppy_file("TEST.TEST", "NowaKopia.txt")








