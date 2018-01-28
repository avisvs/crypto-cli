import unittest

from .main import extract_exchanges_data


class TestDataMethods(unittest.TestCase):
    def setUp(self):
        self.api_data_1 = {
            'Response': 'Success',
            'Data': {
                'TotalCoinsMined': 16830437.0,
                'Algorithm': 'SHA256',
                'Exchanges': [
                    {
                        'MARKET': 'Poloniex',
                        'FROMSYMBOL': 'BTC',
                        'TOSYMBOL': 'USD',
                    },
                    {
                        'MARKET': 'Bitfinex',
                        'FROMSYMBOL': 'BTC',
                        'TOSYMBOL': 'USD',
                    }
                ]
            },
            'Type': 100
        }

        self.extracted = [
            {
                'MARKET': 'Poloniex',
                'FROMSYMBOL': 'BTC',
                'TOSYMBOL': 'USD',
            },
            {
                'MARKET': 'Bitfinex',
                'FROMSYMBOL': 'BTC',
                'TOSYMBOL': 'USD',
            }
        ]

        self.api_data_2 = {
            'Response': 'Success',
            'Data': {
                'TotalCoinsMined': 16830437.0,
                'Algorithm': 'SHA256'
            },
            'Type': 100
        }

    def test_extract_exchanges(self):
        self.assertEqual(
            extract_exchanges_data(self.api_data_1),
            self.extracted
        )

    def test_extract_exchanges_invalid(self):
        self.assertNotEqual(
            extract_exchanges_data(self.api_data_2),
            self.extracted
        )
