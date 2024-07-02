import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    datapoints = [
      ('ABC', 120.48, 121.2, 120.84),
      ('DEF', 117.87, 121.68, 119.775)
    ]

    for quote, datapoint in zip(quotes, datapoints):
      self.assertEqual(getDataPoint(quote), datapoint)

    print("[Test passed on getDataPoint: Calculate Price Test]")

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    datapoints = [
      ('ABC', 120.48, 119.2, 119.84),
      ('DEF', 117.87, 121.68, 119.775)
    ]

    for quote, datapoint in zip(quotes, datapoints):
      self.assertEqual(getDataPoint(quote), datapoint)

    print("[Test passed on getDataPoint: Calculate Price Test Bid Greater Than Ask]")

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    prices = {
      'ABC': 127.89,
      'DEF': 120.84
    }
    datapoint = prices['ABC'] / prices['DEF']
    self.assertEqual(getRatio(prices['ABC'], prices['DEF']), datapoint)
    print("[Test passed on getRatio: Calculate Ratio Test]")

  def test_getRatio_calculateRatioZeroDivision(self):
    prices = {
      'ABC': 127.89,
      'DEF': 00.00
    }

    self.assertEqual(getRatio(prices['ABC'], prices['DEF']), None)
    print("[Test passed on getRatio: Calculate Ratio Test ZeroDivision]")

if __name__ == '__main__':
    unittest.main()
