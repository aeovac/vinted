import requests

with requests.Session() as session:
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0' })

    response = session.post(
        url='https://vinted.ca/en/login',
        data={
            'username': '',
            'password': ''
        },
        allow_redirects=True,
        headers=headers
    )

    print(response.ok)
