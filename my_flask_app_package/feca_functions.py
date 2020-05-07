import requests


def get_price_from_frankfurt(Currency_quantity, Currency_from, Currency_to):
    """
    :param Currency_quantity:
    :param Currency_from:
    :param Currency_to:
    params : does not matter if lower or uppercase
    :return: dict
    """
    try:
        result_from_frankfurt = requests.get(f'https://api.frankfurter.app/latest?amount={ Currency_quantity }&from={ Currency_from }&to={ Currency_to }').json()
        return result_from_frankfurt
    except:
        pass
        #return redirect(url_for('home'))


def check_availability(element, collection: iter):
    '''
    sub_function for check_if_curreny_is_valid_on_frankfurt_list
    :return: True or False
    '''
    return element in collection


def check_if_curreny_is_valid_on_frankfurt_list(my_input):
    """
    :param my_input:
    :return: True or False if my_input is in the list_of_currencies
    """
    list_of_currencies = requests.get('https://api.frankfurter.app/currencies').json()

    list_cur = []
    for i in list_of_currencies:
        list_cur.append(i)

    my_input = my_input.upper()
    return(check_availability(my_input, list_cur))
