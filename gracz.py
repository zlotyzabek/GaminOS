#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import datetime

import pyautogui
import pygame

import save


class Gracz:

    def __init__(self, game):
        self.przycisk = pygame.key.get_pressed()
        self.dataigodzina = datetime.datetime.now()
        # pygame.mouse.get_pos()

        self.game = game
        self.save = save.save()
        self.save_e = save.save_encrypted()



    def tps(self):
        self.dataigodzina = datetime.datetime.now()

    def obiekty(self):
        tlo = pygame.image.load("assest/tloglowne.png").convert_alpha(self.game.okno)
        tlo = pygame.transform.scale(tlo, (self.game.szer_okna, self.game.wys_okna + 20))
        self.game.okno.blit(tlo, (0, 0 - 10))

        if pyautogui.size() == ((1920, 1080)):
            self.R1920_1080()
        else:
            self.R1920_1080()


    def R1920_1080(self):
        self.czciaka70 = pygame.font.SysFont("Showcard Gothic", 80)
        godzina = self.czciaka70.render(str(str(self.dataigodzina.hour) + ":" + str(self.dataigodzina.minute)), False, (255, 255, 255))
        self.game.okno.blit(godzina, (1240, 0))

        mnoznik = 2
        for numerpliku in range(1, 6):
            if self.nazwa_pliku(f"assest/CmdRunIco/Ico{numerpliku}.cmd") == "" or self.nazwa_pliku(f"assest/CmdRunIco/Ico{numerpliku}.cmd") == "\"":
                self.zdjencie("assest/IconaBrak.png", 216 * mnoznik, 0, numerpliku, 2)
                mnoznik -= 1
            else:
                self.zdjencienapis("assest/IconaPusta.png", 216 * mnoznik, 0, numerpliku, 2, self.nazwa_pliku(f"assest/CmdRunIco/Ico{numerpliku}.cmd"))
                mnoznik -= 1

        mnoznik = 2
        for numerpliku in range(1, 6):
            self.zdjencieGryZaDarmo("assest/IconaPusta.png", 216 * mnoznik, 1536, numerpliku, 1)
            mnoznik -= 1

        self.ruchstrzalki(1, 1.11)
        self.ruchstrzalki(2, 1.43)
        self.ruchstrzalki(3, 2)
        self.ruchstrzalki(4, 3.35)
        self.ruchstrzalki(5, 10)
        self.ruchstrzalkiDarmoweGry(1, 1.11)
        self.ruchstrzalkiDarmoweGry(2, 1.43)
        self.ruchstrzalkiDarmoweGry(3,2)
        self.ruchstrzalkiDarmoweGry(4,3.35)
        self.ruchstrzalkiDarmoweGry(5,10)
        self.pobieranie_okno()


    def zdjencie(self, file, wys, szer, nmr1, nmr2):
        ikona = pygame.image.load(file).convert_alpha(self.game.okno)
        ikona = pygame.transform.scale(ikona, (int(1920 / 5), int(1080 / 5)))
        if nmr1 == self.game.strzalka_y and nmr2 == self.game.strzalka_z:
            self.game.okno.blit(ikona, (1535 - 100 - szer, int(self.game.wys_okna / 2 - ikona.get_height() / 2 + wys)))
        else:
            self.game.okno.blit(ikona, (1535 - szer, int(self.game.wys_okna / 2 - ikona.get_height() / 2 + wys)))


    def zdjencienapis(self, file, wys, szer, nmr1, nmr2, name):
        ikona = pygame.image.load(file).convert_alpha(self.game.okno)
        ikona = pygame.transform.scale(ikona, (int(1920 / 5), int(1080 / 5)))
        if nmr1 == self.game.strzalka_y and nmr2 == self.game.strzalka_z:
            self.game.okno.blit(ikona, (1535 - 100 - szer, int(self.game.wys_okna / 2 - ikona.get_height() / 2 + wys)))
            self.czciaka20 = pygame.font.SysFont(self.game.czciakapod, 20)
            wyswiatlanie = self.czciaka20.render(str(name), False, (255, 255, 255))
            self.game.okno.blit(wyswiatlanie, (1728 - wyswiatlanie.get_width() / 2 - 100 - szer, wys + 525))
        else:
            self.game.okno.blit(ikona, (1535 - szer, int(self.game.wys_okna / 2 - ikona.get_height() / 2 + wys)))
            self.czciaka20 = pygame.font.SysFont(self.game.czciakapod, 20)
            wyswiatlanie = self.czciaka20.render(str(name), False, (255, 255, 255))
            self.game.okno.blit(wyswiatlanie, (1728 - wyswiatlanie.get_width() / 2 - szer, wys + 525))


    def nazwa_pliku(self, file_txt):
        path = self.game.save.read(file_txt, 1)
        split = path.split('/')
        return split[-1][:-1]


    def zdjencieGryZaDarmo(self, file, wys, szer, nmr1, nmr2):
        ikona = pygame.image.load(file).convert_alpha(self.game.okno)
        ikona = pygame.transform.scale(ikona, (int(1920 / 5), int(1080 / 5)))
        if nmr1 == self.game.strzalka_y and nmr2 == self.game.strzalka_z:
            self.game.okno.blit(ikona, (1535 - szer + 100, int(self.game.wys_okna / 2 - ikona.get_height() / 2 + wys)))
            self.czciaka20 = pygame.font.SysFont(self.game.czciakapod, 20)
            wyswiatlanie = self.czciaka20.render(str(self.save_e.read("assest/Zapisane_Gry.windowsFile", nmr1)), False, (255, 255, 255))
            self.game.okno.blit(wyswiatlanie, (1728 - wyswiatlanie.get_width() / 2 - szer + 100, wys + 525))
        else:
            self.game.okno.blit(ikona, (1535 - szer, int(self.game.wys_okna / 2 - ikona.get_height() / 2 + wys)))
            self.czciaka20 = pygame.font.SysFont(self.game.czciakapod, 20)
            wyswiatlanie = self.czciaka20.render(str(self.save_e.read("assest/Zapisane_Gry.windowsFile", nmr1)), False, (255, 255, 255))
            self.game.okno.blit(wyswiatlanie, (1728 - wyswiatlanie.get_width() / 2 - szer, wys + 525))


    def ruchstrzalki(self, pozycja_strzalki, dzielnik_wys):
        if self.game.strzalka_y == pozycja_strzalki and self.game.strzalka_z == 2:
            strzalka = pygame.image.load("assest/szczalka.png").convert_alpha(self.game.okno)
            strzalka = pygame.transform.scale(strzalka, (int(self.game.szer_okna / 5), int(self.game.wys_okna / 5)))
            RESET = pygame.Rect(1819, ((self.game.wys_okna / dzielnik_wys) - (strzalka.get_height() / 2) + strzalka.get_height() / 2), 100, strzalka.get_height() / 2)
            START = pygame.Rect(1819, ((self.game.wys_okna / dzielnik_wys) - (strzalka.get_height() / 2)), 100, strzalka.get_height() / 2)
            self.game.okno.blit(strzalka, (
                (self.game.szer_okna * 1.04) - (self.game.wys_okna / 1.2),
                ((self.game.wys_okna / dzielnik_wys) - (strzalka.get_height() / 2))))
            pygame.draw.rect(self.game.okno, (255, 0, 0), RESET)
            pygame.draw.rect(self.game.okno, (0, 252, 0), START)
            R = self.czciaka70.render("R", False, (255, 255, 255))
            self.game.okno.blit(R, (1842, ((self.game.wys_okna / dzielnik_wys) + 20)))
            E = self.czciaka70.render("E", False, (255, 255, 255))
            self.game.okno.blit(E, (1842, ((self.game.wys_okna / dzielnik_wys - (strzalka.get_height()/2) + 20))))

    def ruchstrzalkiDarmoweGry(self, pozycja_strzalki, dzielnik_wys):
        if self.game.strzalka_y == pozycja_strzalki and self.game.strzalka_z == 1:
            strzalka = pygame.image.load("assest/szczalka.png").convert_alpha(self.game.okno)
            strzalka = pygame.transform.scale(strzalka, (int(self.game.szer_okna / 5), int(self.game.wys_okna / 5)))
            START = pygame.Rect(0, ((self.game.wys_okna / dzielnik_wys) - (strzalka.get_height() / 2)), 100, strzalka.get_height())
            self.game.okno.blit(strzalka, (
                (self.game.szer_okna * 0.55) - (self.game.wys_okna / 1.2),
                ((self.game.wys_okna / dzielnik_wys) - (strzalka.get_height() / 2))))
            pygame.draw.rect(self.game.okno, (0, 252, 0), START)
            E = self.czciaka70.render("E", False, (255, 255, 255))
            self.game.okno.blit(E, (20, ((self.game.wys_okna / dzielnik_wys - (strzalka.get_height()/2) + 70))))


    def pobieranie_okno(self):
        Ramka = pygame.Rect(470, 950, 335, 35)
        pygame.draw.rect(self.game.okno, (255, 0, 0), Ramka)
        self.czciaka20 = pygame.font.SysFont(self.game.czciakapod, 20)
        pobgry = self.czciaka20.render("Pobieranie gry zostało rozpoczęte", False, (255, 255, 255)).convert_alpha(self.game.okno)
        self.game.okno.blit(pobgry, (480, 950))



