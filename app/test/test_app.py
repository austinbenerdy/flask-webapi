import unittest
import random

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.seq = list(range(10))

    def test_app(self):
        print('Begin test for test_app.')
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))

if __name__ == '__main__':
    unittest.main()