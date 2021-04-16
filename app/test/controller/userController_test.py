import unittest
import random

class TestUserController(unittest.TestCase):
    
    def setUp(self):
        self.seq = list(range(10))

    def test_read(self):
        print('Calling test_read.')
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))

if __name__ == '__main__':
    unittest.main()