import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(file_in, file_out, from_lang, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    f_in = open(file_in, 'r')
    f_out = open(file_out, 'w')
    
    params = {
        'key': API_KEY,
        'text': f_in.read(),
        'lang': '{}-{}'.format(from_lang, to_lang),
    }
    
    response = requests.get(URL, params=params)
    json_ = response.json()

    f_out.write(''.join(json_['text']))

    f_in.close()
    f_out.close()
    return 



translate_it('ES.txt', 'res.txt', 'es', 'ru')


#requests.post('http://requestb.in/10vc0zh1', json=dict(a='goo', b='foo'))
