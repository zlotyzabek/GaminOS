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


class Game:

    def __init__(self):
        # Config
        self.wys_okna = 540
        self.szer_okna = 1280
        self.wys_okna = 776
        self.szer_okna = 1366
        self.szer_okna, self.wys_okna = pyautogui.size()
        self.max_tps = 60
        self.prendkosc = 1.0
        self.skok = 10.0
        self.grawitacja = 2.0
        self.czciakapod = "Comic Sans MS"

        #os.system("Taskkill /IM explorer.exe /F")
        pygame.init()
        pygame.font.init()
        mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
        self.start = pygame.mixer.Sound("assest/xkill.wav")
        self.musicclick = pygame.mixer.Sound("assest/select.wav")
        self.musicrun = pygame.mixer.Sound("assest/error.wav")
        self.tick = 0
        self.sekundy = 0
        self.czciaka = pygame.font.SysFont(self.czciakapod, 30)
        self.gracz = Gracz(self)
        self.delta = 0.0
        self.okno = pygame.display.set_mode((self.szer_okna, self.wys_okna))
        self.clock = pygame.time.Clock()
        self.czashajsu = 0
        self.strzalka = 3
        self.zajente = 0

        self.musicrun.play(0,2600,0)
        pygame.display.set_caption("GaminOS")

        for licz in range(1, 6):
            save.init(f"assest/CmdRunIco/Ico{licz}.cmd")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #os.system("start explorer.exe")
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if not self.strzalka == 5:
                            self.strzalka += 1
                            self.musicclick.play(0, 1000, 0)

                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if not self.strzalka == 1:
                            self.strzalka -= 1
                            self.musicclick.play(0, 1000, 0)

                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        if self.strzalka == 1:
                            self.wykonanie("assest/CmdRunIco/Ico1.cmd")
                            self.musicclick.play(0, 1000, 0)

                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        if self.strzalka == 2:
                            self.wykonanie("assest/CmdRunIco/Ico2.cmd")
                            self.musicclick.play(0, 1000, 0)

                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        if self.strzalka == 3:
                            self.wykonanie("assest/CmdRunIco/Ico3.cmd")
                            self.musicclick.play(0, 1000, 0)

                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        if self.strzalka == 4:
                            self.wykonanie("assest/CmdRunIco/Ico4.cmd")
                            self.musicclick.play(0, 1000, 0)

                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        if self.strzalka == 5:
                            self.wykonanie("assest/CmdRunIco/Ico5.cmd")
                            self.musicclick.play(0, 1000, 0)

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

    def formatowanie(self):
        for licz in range(1,5):
            save.clear(f"assest/CmdRunIco/Ico{licz}.cmd")

    def tps(self):
        self.gracz.tps()

    def obiekty(self):
        self.gracz.obiekty()


if __name__ == "__main__" and sys.platform == "win32":
    Game()
