import unittest
import logging
from .post_crawler import Post, PostCrawler

logging.basicConfig(level=logging.DEBUG)

class TestPostCrawler(unittest.TestCase):
    def setUp(self):
        self.content = ""
        
    def test_fun(self):
        logging.debug("Execute unit test")
        self.assertEqual(4, 4)

  

if __name__ == '__main__':
    unittest.main()