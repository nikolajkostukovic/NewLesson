import datetime
import requests
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
from Models import currency
from Controllers import connectDB

class GeneralScript:

    __private_url = "https://cbr.ru/scripts/XML_daily.asp?date_req="

    def __init__(self):
        pass

    def startScript(self):

        dateArray = reversed(str(datetime.date.today()).split("-"))
        delimiter = "/"
        dateFormat = delimiter.join(dateArray)

        r = requests.get(self.__private_url + dateFormat)
        valCurs = ET.fromstring(r.text)

        arrayCurrency = []

        for item in valCurs.findall('Valute'):
            numCode = item.find("NumCode").text  # 826
            charCode = item.find("CharCode").text  # GBP
            nominal = item.find("Nominal").text  # 1
            name = item.find("Name").text  # Фунт
            value = item.find("Value").text.replace(",", ".")  # 43, 8254
            vunitRate = item.find("VunitRate").text.replace(",", ".")  # 43, 8254

            currObject = currency.Currency(numCode, charCode, int(nominal), name, float(value), float(vunitRate))

            arrayCurrency.append(currObject)

        connect = connectDB.Connect()
        connect.saveDataCurrency(arrayCurrency)


    def getCurrency(self):
        pass