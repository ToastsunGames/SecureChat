import localchat
import time
import pygame
import sys
import keyboard

pygame.mixer.init()
pygame.mixer.music.load("startup.wav")
pygame.mixer.music.play()
localchat.initialize(port = 6666,format = 'utf-8', disconnect_msg = 'Déconecté')
IP = "127.0.0.1"
print(r" ____                            ____ _           _")
print(r"/ ___|  ___  ___ _   _ _ __ ___ / ___| |__   __ _| |_")
print(r"\___ \ / _ \/ __| | | | '__/ _ \ |   | '_ \ / _` | __|")
print(r" ___) |  __/ (__| |_| | | |  __/ |___| | | | (_| | |_")
print(r"|____/ \___|\___|\__,_|_|  \___|\____|_| |_|\__,_|\__|")
print("Votre logiciel de chat LAN")
print("")
IP = input("Veuillez entrer l'adresse IP de la salle de chat:")
if IP == (""):
    print("Veuillez Entrer une adresse IP")
    time.sleep(1)
else:
    pygame.mixer.music.load("connect.mp3")
    localchat.start_client(IP)
    pygame.mixer.music.play()
    time.sleep(1)
    pygame.mixer.music.load("send.mp3")
    while True:
        if keyboard.is_pressed("enter"):
            pygame.mixer.music.play()
            keyboard.wait("enter")
