import pygame, os, sys
from pygame.math import Vector2
import pyautogui
import datetime


class Gracz(object):

    def __init__(self, game):
        self.przycisk = pygame.key.get_pressed()
        self.game = game
        self.pos = Vector2(0, 0)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.dataigodzina = datetime.datetime.now()
        #os.system("start cmd")

    def tps(self):

        self.vel *= 0.8
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0
        self.dataigodzina = datetime.datetime.now()


    def obiekty(self):
        tlo = pygame.image.load("assest/tloglowne.png")
        tlo = pygame.transform.scale(tlo, (self.game.szer_okna, self.game.wys_okna + 20))
        self.game.okno.blit(tlo, (self.pos.x,self.pos.y - 10))

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

        self.zdjencie("assest/IconaBrak.png", 216 * 2, 1)
        self.zdjencie("assest/IconaBrak.png", 216 * 1, 2)
        self.zdjencie("assest/IconaBrak.png", 0, 3)
        self.zdjencie("assest/IconaBrak.png", -216 * 1, 4)
        self.zdjencie("assest/IconaBrak.png", -216 * 2, 5)
        self.ruchstrzalki()


    def ruchstrzalki(self):

        if self.game.strzalka == 1 or self.game.strzalka == 6:
            strzalka = pygame.image.load("assest/szczalka.png")
            strzalka = pygame.transform.scale(strzalka, (int(self.game.szer_okna / 5), int(self.game.wys_okna / 6)))
            self.game.okno.blit(strzalka, (
                (self.game.szer_okna * 1.05) - (self.game.wys_okna / 1.2),
                ((self.game.wys_okna / 1.11) - (strzalka.get_height() / 2))))
            self.game.strzalka = 1
            self.pos = Vector2(0,10)
        elif self.game.strzalka == 2:
            strzalka = pygame.image.load("assest/szczalka.png")
            strzalka = pygame.transform.scale(strzalka, (int(self.game.szer_okna / 5), int(self.game.wys_okna / 6)))
            self.game.okno.blit(strzalka, (
                (self.game.szer_okna * 1.05) - (self.game.wys_okna / 1.2),
                ((self.game.wys_okna / 1.43) - (strzalka.get_height() / 2))))
            self.pos = Vector2(0, 5)
        elif self.game.strzalka == 3:
            strzalka = pygame.image.load("assest/szczalka.png")
            strzalka = pygame.transform.scale(strzalka, (int(self.game.szer_okna / 5), int(self.game.wys_okna / 6)))
            self.game.okno.blit(strzalka, (
                (self.game.szer_okna * 1.05) - (self.game.wys_okna / 1.2),
                ((self.game.wys_okna / 2) - (strzalka.get_height() / 2))))
            self.pos = Vector2(0, 0)
        elif self.game.strzalka == 4:
            strzalka = pygame.image.load("assest/szczalka.png")
            strzalka = pygame.transform.scale(strzalka, (int(self.game.szer_okna / 5), int(self.game.wys_okna / 6)))
            self.game.okno.blit(strzalka, (
                (self.game.szer_okna * 1.05) - (self.game.wys_okna / 1.2),
                ((self.game.wys_okna / 3.35) - (strzalka.get_height() / 2))))
            self.pos = Vector2(0, -5)
        elif self.game.strzalka == 5 or self.game.strzalka == 0:
            strzalka = pygame.image.load("assest/szczalka.png")
            strzalka = pygame.transform.scale(strzalka, (int(self.game.szer_okna / 5), int(self.game.wys_okna / 6)))
            self.game.okno.blit(strzalka, (
                (self.game.szer_okna * 1.05) - (self.game.wys_okna / 1.2),
                ((self.game.wys_okna / 10) - (strzalka.get_height() / 2))))
            self.game.strzalka = 5
            self.pos = Vector2(0, -10)



    def zdjencie(self, file, wys, nmr):
        ikona = pygame.image.load(file)
        ikona = pygame.transform.scale(ikona, (int(1920 / 5), int(1080 / 5)))
        if nmr == self.game.strzalka:
            self.game.okno.blit(ikona, (1535 - 100, int(self.game.wys_okna / 2 - ikona.get_height() / 2 + wys)))
        else:
            self.game.okno.blit(ikona, (1535 , int(self.game.wys_okna / 2 - ikona.get_height() / 2 + wys)))

    def sila(self, force):
        self.acc += force



