def parse(query: str) -> dict:
    find_symbol = query.rfind('/')
    string_to_check = query[find_symbol + 1:]
    fix_symbol = string_to_check.rfind('?')
    slice_to_check_final = string_to_check[fix_symbol + 1:]
    replace_str = slice_to_check_final.replace('&', ' ')
    list_to_compare = replace_str.split()
    dict_final = {}
    for i in list_to_compare:
        position = i.rfind('=')
        key = i[0:position]
        value = (i[position + 1:])
        dict_final[key] = value
    return dict_final

    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/&name=ferret') == {'name': 'ferret'}
    assert parse('https://example.com/path/to/=ferret') == {'': 'ferret'}
    assert parse('https://example.com/path/to/page?') == {}
    assert parse('https://example.com/path/to/&') == {}
    assert parse('https://example.com/path/to/page?{name}=ferret&color==purple&') == {'{name}': 'ferret', 'color=': 'purple'}
    assert parse('http://example.com/name=') == {'name': ''}
    assert parse('http://example.com/?colour=None') == {'colour': 'None'}
    assert parse('https://example.com/path/to/&name=ferret&') == {'name': 'ferret'}
    assert parse('https://example.com/path/to/name=Dima age=28 city=Kiev') == {'name': 'Dima', 'age': '28', 'city': 'Kiev'}

    

def parse_cookie(query: str) -> dict:
    replace_str = query.replace(';', ' ')
    lst_to_compare = replace_str.split()
    dict_final = {}
    for i in lst_to_compare:
        position_of_equality_symbol = i.find('=')
        key = i[0:position_of_equality_symbol]
        value = (i[position_of_equality_symbol + 1:])
        dict_final[key] = value
    return dict_final

    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User') == {'name': 'Dima=User'}
    assert parse_cookie(';name=Dima=User') == {'name': 'Dima=User'}
    assert parse_cookie(';name=Dima&') == {'name': 'Dima=User'}
    assert parse_cookie(';name=124356') == {'name': '124356'}
    assert parse_cookie('name=124356;age= ') == {'name': '124356', 'age': ''}
    assert parse_cookie('name=124356% age=full=15') == {'name': '124356%', 'age': 'full=15'}
    assert parse_cookie('name=[Kateryna] age=full=15') == {'name': '[Kateryna]', 'age': 'full=15'}
    assert parse_cookie('name="Katya";age=full=15') == {'name': '"Katya"', 'age': 'full=15'}
    assert parse_cookie('=Dima;age=28') == {'': 'Dima', 'age': '28'}
    assert parse_cookie('=Dima age=28') == {'': 'Dima', 'age': '28'}
