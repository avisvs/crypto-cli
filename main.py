import csv
import datetime
import requests
from optparse import OptionParser


CRYPTOCOMPARE_API_URL = 'https://www.cryptocompare.com/api/data/coinsnapshot/'


def endpoint(base, quote):
    '''
    Return dictionary with api data.
    '''
    try:
        data = requests.get(
            CRYPTOCOMPARE_API_URL,
            params={'fsym': base, 'tsym': quote}
        )
        return data.json()
    except:
        return {}


def extract_exchanges_data(data):
    '''
    Return list of dictionaries.
    Each dictionary has info about an exchange.
    '''

    return data.get('Data', {}).get('Exchanges', [])


def write_csv(exchanges_data):
    '''
    Write csv file using exchanges data.
    Exchanges data is a list of dictionaries.
    '''

    if len(exchanges_data) == 0:
        print('No exchanges data')
        return

    filename = '{}.csv'.format(
        datetime.datetime.now().strftime("%Y-%m-%d--%H:%M:%S")
    )

    cleaned_data = []
    for exchange in exchanges_data:
        cleaned_data.append({
            'Exchange': exchange.get('MARKET'),
            'Base': exchange.get('FROMSYMBOL'),
            'Quote': exchange.get('TOSYMBOL'),
            'Price': exchange.get('PRICE'),
            'High': exchange.get('HIGH24HOUR'),
            'Low': exchange.get('LOW24HOUR'),
            'Volume': exchange.get('VOLUME24HOUR')
        })

    with open(filename, 'w', newline='') as new_file:
        fieldnames = [
            'Exchange',
            'Base',
            'Quote',
            'Price',
            'High',
            'Low',
            'Volume'
        ]
        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_data)


def main():

    parser = OptionParser()
    parser.add_option(
        "-b",
        "--base",
        action="store",
        dest="base",
        help="The base cryptocurrency"
    )
    parser.add_option(
        "-q",
        "--quote",
        action="store",
        dest="quote",
        help="The quote cryptocurrency"
    )
    (options, args) = parser.parse_args()

    data = endpoint(
        base=options.base,
        quote=options.quote
    )
    exchanges = extract_exchanges_data(data)
    write_csv(exchanges)


if __name__ == '__main__':
    main()
