#!/usr/bin/python3
import sys
import pip
import requests
import os

class csomagkezelo:
    def fuggosegTelepites(self, fuggosegek):
        for csomagnev in fuggosegek:
            if hasattr(pip, 'main'):
                pip.main(['install', csomagnev])
            else:
                pip._internal.main(['install', csomagnev])
    def fuggosegLetorles(self, fuggosegek):
        for csomagnev in fuggosegek:
            if hasattr(pip, 'main'):
                pip.main(['uninstall', csomagnev])
            else:
                pip._internal.main(['uninstall', csomagnev])
    def telepites(self, csomagnev):
        baseURL = f"https://raw.githubusercontent.com/PiciAkk/ROBIN5-Csomagok/main/{csomagnev}"
        modulFajl = open(f"csomagok/{csomagnev}.py", "w+")
        modulFajl.write(requests.get(f"{baseURL}/modul.py").text)
        modulFajl.close()
        fuggosegek = (requests.get(f"{baseURL}/fuggosegek.txt").text).split()
        self.fuggosegTelepites(fuggosegek)
        print("Csomag sikeresen telepítve")
    def letorles(self, csomagnev):
        fuggosegek = (requests.get(f"https://raw.githubusercontent.com/PiciAkk/ROBIN5-Csomagok/main/{csomagnev}/fuggosegek.txt").text).split()
        try:
            os.remove(f"csomagok/{csomagnev}.py")
        except:
            raise Exception("Csomag nincs telepítve!")
        self.fuggosegLetorles(fuggosegek)
        print("Csomag sikeresen törölve!")
    def parameterTeszt(self, args):
        if len(args) < 3:
            raise Exception("Csomagnév nincs specifikálva!")
        elif len(args) > 3:
            raise Exception("Túl sok paraméter")
class ROBIN:
    def hangFelismeres(self):
        return "Szia"
    def csomagBetoltes(self):
        modulok = os.listdir("./csomagok")
        for modul in modulok:
            exec(open(f"csomagok/{modul}", "r").read())
    def __init__(self):
        self.parancs = self.hangFelismeres()
        self.csomagBetoltes()

def main():
    csomagok = csomagkezelo()
    args = sys.argv
    if len(args) == 1:
        ROBIN()
        quit()
    elif args[1] == "telepites":
        csomagok.parameterTeszt(args)
        csomagok.telepites(args[2])
    elif args[1] == "letorles":
        csomagok.parameterTeszt(args)
        csomagok.letorles(args[2])

if __name__ == "__main__":
    main()