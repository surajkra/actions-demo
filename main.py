import requests
import os

def send_request(stock_ticker: str, date: str, api_key: str, base_url: str = 'https://api.polygon.io/v1/open-close/',
                 adjusted_flag: str = 'true'):
    """
    Function to send API request to polygon API

    :param stock_ticker: str abbreviation of company name
    :param date: str date of stock info
    :param api_key: str API-key for polygon API
    :param base_url: str base url format
    :param adjusted_flag: str whether to get adjusted value or not. Default: true

    :return: dict containing result

    """
    url = f'{base_url}{stock_ticker}/{date}'
    params = {'adjusted': adjusted_flag,
              'apiKey': api_key}

    api_request = requests.get(url=url, params=params)
    if api_request.status_code == 200:
        output = api_request.json()
    else:
        raise AssertionError(f"API request not successful: status code {api_request.status_code}")

    return output


if __name__ == "__main__":
    POLYGON_API_KEY = os.environ["POLYGON_API_KEY"]
    #api_key = p7ch9DdAkyYJbuSzxAm94NRFj6TUrWfa
    api_call = send_request(stock_ticker='AAPL', date='2022-01-05', api_key=POLYGON_API_KEY)
    print(api_call)
    
