def rec_dict(_dict, search_key, deep):
    if deep == 0:
        return
    for key in _dict:
        if key == search_key:
            print(_dict[key])
        elif isinstance(_dict[key], dict):
            rec_dict(_dict[key], search_key, deep - 1)


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

print(rec_dict(site, "div", 3))