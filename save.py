import linecache
import codecs


def init(file_txt):
    plik = open(file_txt, "a")
    if plik.readable():
        pass
    else:
        plik = open(file_txt, "a")


def read(file_txt, number_line):
    file = open(file_txt, 'r').read()
    lines = file.split('\n')
    try:
        if lines[number_line - 1] == (""):
            return("")
        else:
            return lines[(number_line - 1)]

    except Exception:
        read = linecache.getline(file_txt, number_line)
        return read

    read.close()

def write(file_txt, write):
    plik = codecs.open(file_txt, "a")
    plik.write(write + "\n")
    plik.close()

def number_lines(file_txt):
    count = len(open(file_txt, 'rU').readlines())
    return count

def clear(file_txt):
    open(file_txt, "w+")

init("assest/CmdRunIco/Ico1.cmd")
print(read("assest/CmdRunIco/Ico1.cmd", 2))