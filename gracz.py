import os
import sys
import datetime

import pyautogui
import pygame
import save




class Gracz:

    def __init__(self, game):
        self.przycisk = pygame.key.get_pressed()
        self.game = game
        self.dataigodzina = datetime.datetime.now()


    def tps(self):
        self.dataigodzina = datetime.datetime.now()

    def obiekty(self):
        tlo = pygame.image.load("assest/tloglowne.png")
        tlo = pygame.transform.scale(tlo, (self.game.szer_okna, self.game.wys_okna + 20))
        self.game.okno.blit(tlo, (0,0 - 10))

        if pyautogui.size() == ((1920,1080)):
            self.R1920_1080()
        else:
            self.R1920_1080()

    def R1920_1080(self):
        godzina = self.game.czciaka.render(str(str(self.dataigodzina.hour) + ":" + str(self.dataigodzina.minute)), False, (255, 255, 255))
        self.game.okno.blit(godzina, (0, 0))
        start = pygame.image.load("assest/szczalkastart.png")
        start = pygame.transform.scale(start, (int(self.game.szer_okna / 5), int(self.game.wys_okna / 6)))
        self.game.okno.blit(start, (
        (self.game.szer_okna / 2) - (self.game.wys_okna / 1.2), ((self.game.wys_okna / 2) - (start.get_height() / 2))))

        if self.nazwa_pliku("assest/CmdRunIco/Ico1.cmd") == "":
            self.zdjencie("assest/IconaBrak.png", 216 * 2, 1)
        else:
            self.zdjencie("assest/IconaPusta.png", 216 * 2, 1)
            self.nazwa_wyswiatlana_programu(100, 100, self.nazwa_pliku("assest/CmdRunIco/Ico1.cmd"))

        if self.nazwa_pliku("assest/CmdRunIco/Ico2.cmd") == "":
            self.zdjencie("assest/IconaBrak.png", 216 * 1, 2)
        else:
            self.zdjencie("assest/IconaPusta.png", 216 * 1, 2)

        if self.nazwa_pliku("assest/CmdRunIco/Ico3.cmd") == "":
            self.zdjencie("assest/IconaBrak.png", 216 * 0, 3)
        else:
            self.zdjencie("assest/IconaPusta.png", 216 * 0, 3)

        if self.nazwa_pliku("assest/CmdRunIco/Ico4.cmd") == "":
            self.zdjencie("assest/IconaBrak.png", -216 * 1, 4)
        else:
            self.zdjencie("assest/IconaPusta.png", -216 * 1, 4)

        if self.nazwa_pliku("assest/CmdRunIco/Ico5.cmd") == "":
            self.zdjencie("assest/IconaBrak.png", -216 * 2, 5)
        else:
            self.zdjencie("assest/IconaPusta.png", -216 * 2, 5)

        self.ruchstrzalki()



    def ruchstrzalki(self):

        if self.game.strzalka == 1:
            strzalka = pygame.image.load("assest/szczalka.png").convert_alpha(self.game.okno)
            strzalka = pygame.transform.scale(strzalka, (int(self.game.szer_okna / 5), int(self.game.wys_okna / 6)))
            self.game.okno.blit(strzalka, (
                (self.game.szer_okna * 1.05) - (self.game.wys_okna / 1.2),
                ((self.game.wys_okna / 1.11) - (strzalka.get_height() / 2))))
        elif self.game.strzalka == 2:
            strzalka = pygame.image.load("assest/szczalka.png").convert_alpha(self.game.okno)
            strzalka = pygame.transform.scale(strzalka, (int(self.game.szer_okna / 5), int(self.game.wys_okna / 6)))
            self.game.okno.blit(strzalka, (
                (self.game.szer_okna * 1.05) - (self.game.wys_okna / 1.2),
                ((self.game.wys_okna / 1.43) - (strzalka.get_height() / 2))))
        elif self.game.strzalka == 3:
            strzalka = pygame.image.load("assest/szczalka.png").convert_alpha(self.game.okno)
            strzalka = pygame.transform.scale(strzalka, (int(self.game.szer_okna / 5), int(self.game.wys_okna / 6)))
            self.game.okno.blit(strzalka, (
                (self.game.szer_okna * 1.05) - (self.game.wys_okna / 1.2),
                ((self.game.wys_okna / 2) - (strzalka.get_height() / 2))))
        elif self.game.strzalka == 4:
            strzalka = pygame.image.load("assest/szczalka.png").convert_alpha(self.game.okno)
            strzalka = pygame.transform.scale(strzalka, (int(self.game.szer_okna / 5), int(self.game.wys_okna / 6)))
            self.game.okno.blit(strzalka, (
                (self.game.szer_okna * 1.05) - (self.game.wys_okna / 1.2),
                ((self.game.wys_okna / 3.35) - (strzalka.get_height() / 2))))
        elif self.game.strzalka == 5:
            strzalka = pygame.image.load("assest/szczalka.png").convert_alpha(self.game.okno)
            strzalka = pygame.transform.scale(strzalka, (int(self.game.szer_okna / 5), int(self.game.wys_okna / 6)))
            self.game.okno.blit(strzalka, (
                (self.game.szer_okna * 1.05) - (self.game.wys_okna / 1.2),
                ((self.game.wys_okna / 10) - (strzalka.get_height() / 2))))



    def zdjencie(self, file, wys, nmr):
        ikona = pygame.image.load(file).convert_alpha(self.game.okno)
        ikona = pygame.transform.scale(ikona, (int(1920 / 5), int(1080 / 5)))
        if nmr == self.game.strzalka:
            self.game.okno.blit(ikona, (1535 - 100, int(self.game.wys_okna / 2 - ikona.get_height() / 2 + wys)))
        else:
            self.game.okno.blit(ikona, (1535 , int(self.game.wys_okna / 2 - ikona.get_height() / 2 + wys)))

    def nazwa_wyswiatlana_programu(self, x, y, name):
        wyswiatlanie = self.game.czciaka.render(str(name), False, (255, 255, 255))
        self.game.okno.blit(wyswiatlanie, (x, y))

    def nazwa_pliku(self, file_txt):
        path = save.read(file_txt, 2)
        splited = path.split('/')
        print(save.read(file_txt, 2))
        return splited[-1]

    def sila(self, force):
        self.acc += force



