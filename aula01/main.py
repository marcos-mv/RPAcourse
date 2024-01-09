import pyautogui
import pandas as pd
import numpy
import openpyxl

import time

# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar varias teclas -> pyautogui.hotkey
# scroll -> pyautogui.scroll


link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 0.5

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

pyautogui.write(link)

pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=467, y=402)

pyautogui.write("email@email.com.br")

# pyautogui.click("tab")

pyautogui.click(x=460, y=498)

pyautogui.write("passwor9888**CVFDGd")

pyautogui.click(x=681, y=557)

time.sleep(3)


file = pd.read_csv("produtos.csv")

print(file)



for linha in file.index:
    
    pyautogui.click(x=509, y=287)

    codigo = file.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")

    marca = file.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")

    tipo = file.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")

    categoria = file.loc[linha, "categoria"]
    pyautogui.write(str(categoria))

    pyautogui.press("tab")

    preco = file.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))

    pyautogui.press("tab")

    custo = file.loc[linha, "custo"]
    pyautogui.write(str(custo))

    pyautogui.press("tab")

    obs = file.loc[linha, "obs"]
    
    if not pd.isna(obs):
    
        pyautogui.write("obs")

    pyautogui.press("tab")
    
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)
    
    



