import requests


def test_get():
    print()
    print('begin testing [GET] reqest to /controllers/coffehouse')
    response = requests.get(
        'http://thefir.ddns.net:5050/controllers/coffehouse')
    try:
        if response.status_code == 200 and len(response.json()) != 0:
            print(':     testing success ['+u'\u2713'+']')
        else:
            print(f'     test failure [X] error code {response.status_code}')
    except:
        print('     test failure [X]')


def test_put():
    print()
    print('begin testing [PUT] reqest to /controllers/coffehouse')

    data = {'address': 'Воронеж, ул. Старых Коней, д.15а', 'email': 'example@mail.ru',
            'id': 1, 'name': '#thefir', 'phone': '89003334455', 'description': '1', 'photos': ['http']}
    response = requests.put(
        'http://thefir.ddns.net:5050/controllers/coffehouse', json=data)
    try:
        if response.status_code == 204:
            print(':     testing success ['+u'\u2713'+']')
        else:
            print(f'     test failure [X] error code {response.status_code}')
    except:
        print('     test failure [X]')


if __name__ == '__main__':
    test_get()
    test_put()
