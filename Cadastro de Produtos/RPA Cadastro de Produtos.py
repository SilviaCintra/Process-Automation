# -*- codinCEAhttps://dlp.hashtagtreinamentos.com/python/intensivao/loginhttps://dlp.hashtagtreinamentos.com/python/intensivao/loginhttps
"""https://dlp.hashtagtreinamentos.com/python/intensivao/login
2
Created on Tue Jan  9 15:11:17 2024

@author: silvi
"""

# Passo a passo do projeto RPA - automação bot

import pyautogui
import time

# Etapa 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

#lembrete chttps://dlp.hashtagtreinamentos.com/python/intensivao/login
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.7

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)   

# entrar no link 
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(site)
pyautogui.press("enter")
time.sleep(3)

# Etapa 2: Fazer login
# selecionar o campo de email
pyautogui.press("tab")
time.sleep(2)
# escrever o seu email
pyautogui.write("silvia.cintra93@gmail.com")
time.sleep(1    )
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("12345")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("enter") # clique no botao de login
time.sleep(3)

# Etapa 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

# Etapa 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=3061, y=722)
    time.sleep(1)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "precounitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)