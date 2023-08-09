import requests
from bs4 import BeautifulSoup
import time

for guess in range(1,10000):

    formatted_guess = f'{guess:04}'
    print(f'attempting pin of {formatted_guess}')
    new_data = {
        'guess': formatted_guess
    }

    url_post = 'https://www.guessthepin.com/prg.php'

    post_response = requests.post(url_post, new_data)
    html_content = post_response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    element_by_id=soup.find("label",{"for":"pin"})

    result = str(element_by_id)
    time.sleep(1)
    if result.find('is not the PIN') == -1:
        print(f'Pin was {formatted_guess}')
        break
