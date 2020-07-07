import unittest

class Sample(unittest.TestCase):
      def test_fun(self):
        logging.debug("Execute unit test")
        self.assertEqual(4, 4)