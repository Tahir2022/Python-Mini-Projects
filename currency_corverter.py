''''
from requests import get 
from pprint import PrettyPrinter

BASE_URL = "https://api.exchangerate.host/"

printer = PrettyPrinter()

def get_currencies():
    url = BASE_URL + "symbols"
    response = get(url)
    data = response.json()
    printer.pprint(data)
 
get_currencies()

from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.frankfurter.app/"
printer = PrettyPrinter()

def get_currencies():
    data = get(BASE_URL + "currencies").json()
    printer.pprint(data)

get_currencies()'''