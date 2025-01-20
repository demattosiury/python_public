from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from time import sleep
from datetime import datetime

import pandas as pd

# HTML elements
idLabelBusca = "filled-normal"
xPathCotacaoPapel = '//span[@class="chart-info-val ng-binding"]'

# variables
url = "https://economia.uol.com.br/cotacoes/bolsas/"
strftime = "%d/%m/%Y %H:%M:%S"
empresas = [
    {"symbol": "PETR3.SA", "close": 0, "datetime": ""},
    {"symbol": "MGLU3.SA", "close": 0, "datetime": ""},
    {"symbol": "VIVT3.SA", "close": 0, "datetime": ""},
]


# functions
def webRequest(url):
    driver.get(url)


def buscarEmpresa(empresa):
    input_busca = driver.find_element(By.ID, idLabelBusca)

    input_busca.send_keys(empresa["symbol"])
    sleep(3)
    input_busca.send_keys(Keys.ENTER)


def atualizarFechamentoEmpresa(empresa):
    span_cotacao_papel = driver.find_element(By.XPATH, xPathCotacaoPapel)
    empresa["close"] = span_cotacao_papel.text
    empresa["datetime"] = datetime.now().strftime(strftime)


def criarCSV():
    df_empresas = pd.DataFrame(empresas)
    df_empresas.to_csv("./empresas.csv")


# driver options
options = Options()
options.add_argument("--headless")

# Chrome driver installed in runtime to be used by selenium
driver = wd.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# process


webRequest(url)

for e in empresas:
    sleep(5)
    buscarEmpresa(e)
    sleep(5)
    atualizarFechamentoEmpresa(e)

criarCSV()
