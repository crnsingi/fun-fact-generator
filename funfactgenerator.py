import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
    # Clear the screen
    clear()
    
    #HTML content for the fun fact generator header
    put_html(
        '<p align="left">'
        '<h2><img src="https://cdn-icons-png.flaticon.com/512/157/157776.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )
    
    #URL fetch data
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    #Get request
    response = requests.get(url)
    
    # Load the request in json file
    data = json.loads(response.text)
    
