import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
  for quotes in quotes:
      self.assertEqual(getDataPoint(quotes), (quotes['stock'], quotes['top_bid']['price'], quotes['top_ask']['price'], (quotes['top_bid']['price'] + quotes['top_ask']['price']) / 2))
  
 def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
for quotes in quotes:
      self.assertEqual(getDataPoint(quotes), (quotes['stock'], quotes['top_bid']['price'], quotes['top_ask']['price'], (quotes['top_bid']['price'] + quotes['top_ask']['price']) / 2))

  """ ------------ Add more unit tests ------------ """

  def test_getDataPoint_zeroPrices(self):
      quote = {
          'top_ask': {'price': 0.0, 'size': 36},
          'top_bid': {'price': 0.0, 'size': 109},
          'timestamp': '2019-02-11 22:06:30.572453',
          'id': '0.4', 'stock': 'LMN'
      }
      expected_price = 0.0
      self.assertEqual(getDataPoint(quote), ('LMN', 0.0, 0.0, expected_price))
    
def test_getDataPoint_missingAsk(self):
        quote = {
            'top_ask': {'size': 36},  # price missing
            'top_bid': {'price': 120.0, 'size': 109},
            'timestamp': '2019-02-11 22:06:30.572453',
            'id': '0.5', 'stock': 'ERR'
        }
        with self.assertRaises(KeyError):
            getDataPoint(quote)
  def test_getDataPoint_nonNumericPrices(self):
      quote = {
          'top_ask': {'price': 'abc', 'size': 36},
          'top_bid': {'price': 120.0, 'size': 109},
          'timestamp': '2019-02-11 22:06:30.572453',
          'id': '0.6', 'stock': 'BAD'
      }
      with self.assertRaises(ValueError):
          getDataPoint(quote)

if __name__ == '__main__':
    unittest.main()
