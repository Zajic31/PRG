# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dpC-6FuPcyLrWHO3ssxApO0fJVfefttO
"""

print("Zdravíčko! >_<")
print("-" * 30)
print("Zahrajme si takovou hru O_O, vygeneruji ti 4-místné číslo a ty ho uhádni >.<")
print("-" * 30)
print("Začínáme!")

import random

def unikatni_4_mistne_cislo():
    prvni_cislice = random.randint(1, 9)
    druha_cislice = random.randint(0, 9)
    while druha_cislice == prvni_cislice:
        druha_cislice = random.randint(0, 9)

    treti_cislice = random.randint(0, 9)
    while treti_cislice == prvni_cislice or treti_cislice == druha_cislice:
        treti_cislice = random.randint(0, 9)

    ctvrta_cislice = random.randint(0, 9)
    while ctvrta_cislice == prvni_cislice or ctvrta_cislice == druha_cislice or ctvrta_cislice == treti_cislice:
        ctvrta_cislice = random.randint(0, 9)

    return int(f"{prvni_cislice}{druha_cislice}{treti_cislice}{ctvrta_cislice}")

def bulls_and_cows(secret, guess):
    secret_str = str(secret)
    bulls = sum(1 for i in range(4) if secret_str[i] == guess[i])
    cows = sum(1 for x in guess if x in secret_str) - bulls
    return bulls, cows

gen_cislo = unikatni_4_mistne_cislo()

while True:
  pokus = input("Zadej 4-místné číslo: ")

  if len(pokus) != 4 or not pokus.isdigit() or len(set(pokus)) != 4 or pokus[0] == "0":
    print("Chyba: Zadej platné 4-místné číslo s unikátními ciframi a první číslice nesmí být 0.")
    continue

  bulls, cows = bulls_and_cows(gen_cislo, pokus)
  print(f"Bulls: {bulls}, Cows: {cows}")

  if bulls == 4:
    print("Hezky pěkně! Uhádl si číslo <^_^/")
    break
  else:
    print("Pokračuj! To zvládneš ;)")