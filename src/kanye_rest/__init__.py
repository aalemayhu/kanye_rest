import requests

KANYE_QUOTE_ENDPOINT = "https://api.kanye.rest/"


def get_kanye_quote():
    response = requests.get(KANYE_QUOTE_ENDPOINT)
    response.raise_for_status()

    content = response.json()
    assert "quote" in content
    quote = content["quote"]
    return quote
