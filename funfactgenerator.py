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
    
    #'text' from the data 
    useless_fact = data['text']
    
    # Put the fact in blue color and increase the font size
    style(put_text(useless_fact), 'color:blue; font-size: 30px')
    
    #"Click me" button
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )
    
    # Driver Function
    if __name__ == '__main__':
        #Heading "Func Fact Generator"
        put_html(
            '<p align="left">'
            '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
            '</p>'    
        )
