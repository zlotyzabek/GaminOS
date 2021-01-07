import pygame
import save
from pygame import *
import sys, os
import pyautogui
from gracz import Gracz
import tkinter
from tkinter import filedialog
from pathlib import Path
import datetime


class Game(object):

    def __init__(self):
        # Config
        self.wys_okna = 540
        self.szer_okna = 1280
        self.wys_okna = 776
        self.szer_okna = 1366
        self.szer_okna, self.wys_okna = pyautogui.size()
        self.max_tps = 120
        self.prendkosc = 1.0
        self.skok = 10.0
        self.grawitacja = 2.0
        self.czciaka = "Comic Sans MS"

        pygame.init()
        pygame.font.init()
        mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
        self.start = pygame.mixer.Sound("assest/xkill.wav")
        self.musicclick = pygame.mixer.Sound("assest/select.wav")
        self.musicrun = pygame.mixer.Sound("assest/error.wav")
        self.start.play()
        self.tick = 0
        self.sekundy = 0
        self.czciaka = pygame.font.SysFont(self.czciaka, 30)
        self.gracz = Gracz(self)
        self.delta = 0.0
        self.okno = pygame.display.set_mode((self.szer_okna, self.wys_okna))
        self.clock = pygame.time.Clock()
        self.czashajsu = 0
        self.strzalka = 3
        self.zajente = 0
        save.init("assest/Ico1.cmd")
        save.init("assest/Ico2.cmd")
        save.init("assest/Ico3.cmd")
        save.init("assest/Ico4.cmd")
        save.init("assest/Ico5.cmd")
        #save.clear("assest/Ico1.cmd")
        #save.clear("assest/Ico2.cmd")
        #save.clear("assest/Ico3.cmd")
        #save.clear("assest/Ico4.cmd")
        #save.clear("assest/Ico5.cmd")
        pygame.display.set_caption('Coś się wymiśli')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.strzalka += 1
                    if event.key == pygame.K_s:
                        self.strzalka -= 1
                    if event.key == pygame.K_d and self.strzalka == 1:
                        self.wykonanie("assest/Ico1.cmd")
                    if event.key == pygame.K_d and self.strzalka == 2:
                        self.wykonanie("assest/Ico2.cmd")
                    if event.key == pygame.K_d and self.strzalka == 3:
                        self.wykonanie("assest/Ico3.cmd")
                    if event.key == pygame.K_d and self.strzalka == 4:
                        self.wykonanie("assest/Ico4.cmd")
                    if event.key == pygame.K_d and self.strzalka == 5:
                        self.wykonanie("assest/Ico5.cmd")

                    ##elif event.key == pygame.K_d and self.strzalka == 3:
                            ##os.system("start Chrome.cmd")
                    ##elif event.key == pygame.K_d and self.strzalka == 1:
                            ##webbrowser.open_new_tab("https://discord.com/channels/@me")
                            ##print(webbrowser.get())


            self.delta += self.clock.tick() / 1000.0
            while self.delta > 1 / self.max_tps:
                self.tps()
                self.delta -= 1 / self.max_tps
            self.okno.fill((0, 115, 255))
            self.obiekty()
            pygame.display.update()


    def wykonanie(self, file):
        if save.number_lines(file) == 3:
            current_absolute_path = Path().absolute()
            os.system(f"start {current_absolute_path}/{file}")
        else:
            tkinter.Tk().withdraw()
            save.clear(file)
            save.write(file, str("@echo off"))
            save.write(file, str("\"" + filedialog.askopenfilename() + "\""))
            save.write(file, str("exit"))
            self.zajente = 1

    def tps(self):
        self.gracz.tps()


    def obiekty(self):
        self.gracz.obiekty()



if __name__ == "__main__":
    Game()





