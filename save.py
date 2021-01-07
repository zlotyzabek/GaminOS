import linecache
import codecs


def init(file_txt):
    plik = open(file_txt, "a")
    if plik.readable():
        pass
    else:
        open(file_txt, "a")

def read(file_txt, number_line):
    read = linecache.getline (file_txt, number_line)
    return read
    plik.close()

def write(file_txt, write):
    plik = codecs.open(file_txt, "a")
    plik.write(write + "\n")
    plik.close()

def number_lines(file_txt):
    count = len(open(file_txt, 'rU').readlines())
    return count

def clear(file_txt):
    open(file_txt, "w+")