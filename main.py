#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import sys
import os
from pathlib import Path
import tkinter
from tkinter import filedialog

import pygame
from pygame import *
import pyautogui

from gracz import Gracz
import save


class Game():

    def __init__(self):
        # Config
        self.szer_okna, self.wys_okna = pyautogui.size()
        self.max_tps = 15
        self.czciakapod = "Comic Sans MS"

        #os.system("Taskkill /IM explorer.exe /F")
        pygame.init()
        pygame.font.init()
        mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
        self.save = save.save()
        self.save_e = save.save_encrypted()

        self.start = pygame.mixer.Sound("assest/xkill.wav")
        self.musicclick = pygame.mixer.Sound("assest/select.wav")
        self.musicrun = pygame.mixer.Sound("assest/error.wav")

        self.czciaka = pygame.font.SysFont(self.czciakapod, 30)
        self.gracz = Gracz(self)
        self.delta = 0.0
        self.okno = pygame.display.set_mode((self.szer_okna, self.wys_okna))
        self.clock = pygame.time.Clock()
        self.strzalka_y = 3
        self.strzalka_z = 2


        self.musicrun.play(0,3000,0)
        pygame.display.set_caption("GaminOS")


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #os.system("start explorer.exe")
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if not self.strzalka_y == 5:
                            self.strzalka_y += 1
                            self.musicclick.play(0, 1000, 0)

                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if not self.strzalka_y == 1:
                            self.strzalka_y -= 1
                            self.musicclick.play(0, 1000, 0)

                    if event.key == pygame.K_d or event.key == pygame.K_UP:
                        if not self.strzalka_z == 2:
                            self.strzalka_z += 1
                            self.musicclick.play(0, 1000, 0)

                    if event.key == pygame.K_a or event.key == pygame.K_DOWN:
                        if not self.strzalka_z == 1:
                            self.strzalka_z -= 1
                            self.musicclick.play(0, 1000, 0)

                    if event.key == pygame.K_e:
                        for licz in range(1,6):
                            self.uruchamianieprogramu(licz)

                    if event.key == pygame.K_r:
                        self.formatowanie(self.strzalka_y)
                        self.musicclick.play(0, 1000, 0)

            self.okno.fill((0, 115, 255))
            self.obiekty()
            pygame.display.update()

    def uruchamianieprogramu(self, number):
        if self.strzalka_y == number:
            self.wykonanie(f"assest/CmdRunIco/Ico{number}.cmd")
            self.musicclick.play(0, 1000, 0)


    def wykonanie(self, file):
        if self.save.read(file, 1)== " ":
            tkinter.Tk().withdraw()
            self.save.clear(file)
            self.save.write(file, str("@echo off"))
            self.save.write(file, str("\"" + filedialog.askopenfilename() + "\""))
            self.save.write(file, str("exit"))
            self.zajente = 1

        elif self.save.number_lines(file) == 3 and not self.save.read(file, 2) == f"\"\"":
            current_absolute_path = Path().absolute()
            os.system(f"start {current_absolute_path}/{file}")

        else:
            tkinter.Tk().withdraw()
            self.save.clear(file)
            self.save.write(file, str("@echo off"))
            self.save.write(file, str("\"" + filedialog.askopenfilename() + "\""))
            self.save.write(file, str("exit"))
            self.zajente = 1


    def formatowanie(self, numerplikuico):
            self.save.clear(f"assest/CmdRunIco/Ico{numerplikuico}.cmd")
            self.save.write(f"assest/CmdRunIco/Ico{numerplikuico}.cmd"," ")
            self.save.write(f"assest/CmdRunIco/Ico{numerplikuico}.cmd"," ")
            self.save.write(f"assest/CmdRunIco/Ico{numerplikuico}.cmd"," ")


    def tps(self):
        self.gracz.tps()


    def obiekty(self):
        self.gracz.obiekty()


if __name__ == "__main__" and sys.platform == "win32":
    Game()
