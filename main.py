#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import sys
import os
from pathlib import Path
import tkinter
from tkinter import filedialog
import threading

import pygame
from pygame import *
import pyautogui
import gdown

from gracz import Gracz
import save


class Game():

    def __init__(self):
        # Config
        self.szer_okna, self.wys_okna = pyautogui.size()
        self.max_tps = 30
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

        #threading.Thread(target=self.download_fn).start()

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

                    if event.key == pygame.K_e and self.strzalka_z == 2:
                        for licz in range(1,6):
                            self.uruchamianieprogramu(licz)

                    elif event.key == pygame.K_e and self.strzalka_z == 1:
                        for licz in range(1,6):
                            self.pobieranie_gier(licz)
                            #tkinter.Tk().withdraw()
                            #print(filedialog.askopenfilename())

                    if event.key == pygame.K_r and self.strzalka_z == 2:
                        self.formatowanie(self.strzalka_y)
                        self.musicclick.play(0, 1000, 0)

            self.delta += self.clock.tick() / 1000.0
            while self.delta > 1 / self.max_tps:
                        self.tps()
                        self.delta -= 1 / self.max_tps

            self.obiekty()

    def uruchamianieprogramu(self, number):
        if self.strzalka_y == number:
            self.wykonanie(f"assest/CmdRunIco/Ico{number}.cmd")
            self.musicclick.play(0, 1000, 0)


    def wykonanie(self, file):
        if self.save.read(file, 1) == " " or self.save.read(file, 1) == "":
            tkinter.Tk().withdraw()
            self.save.clear_and_write(file, str("\"" + filedialog.askopenfilename() + "\""))
            self.save.write(file, str("exit"))

        elif self.save.number_lines(file) == 2 and not self.save.read(file, 1) == f"\"\"":
            current_absolute_path = Path().absolute()
            os.system(f"start {current_absolute_path}/{file}")

        else:
            tkinter.Tk().withdraw()
            self.save.clear_and_write(file, str("\"" + filedialog.askopenfilename() + "\""))
            self.save.write(file, str("exit"))


    def formatowanie(self, numerplikuico):
            self.save.clear(f"assest/CmdRunIco/Ico{numerplikuico}.cmd")

    def tps(self):
        pygame.display.update()
        self.gracz.tps()


    def obiekty(self):
        self.gracz.obiekty()


    def download_fn(self):
        url = 'https://drive.google.com/uc?id=1ITBf078EI4Fa7_jChzg5LOPV2eC96Gdp'
        output = 'assest/Programs/Cyberpunk unloked by zlotyzabek.zip'
        gdown.download(url, output, quiet=False)

    def pobieranie_gier(self, number):
        if self.strzalka_y == number:
            grydopobrania = {
                "Among Us": "trochę bug",
                "CyberPunk 2077": "bug",
                f"No man\"s sky": "No",
                "Raft": "rekin!",
                "Astroneer": "Kosmos to kosmos"
            }
            print(grydopobrania[self.save_e.read("assest/Zapisane_Gry.windowsFile", number)])

            #self.save_e.read("assest/Zapisane_Gry.windowsFile")

if __name__ == "__main__" and sys.platform == "win32":
    Game()

