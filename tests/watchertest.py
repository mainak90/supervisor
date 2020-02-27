import unittest
from src.watcher import Watcher

class WatcherTest(unittest.TestCase):
    def test_watcher(self):
        self.assertEqual(Watcher(['sleep 20'], '5', '2').__dict__.items(), { 'commandlist': ['sleep 20'], 'wait': '5', 'interval': '2' }.items())

if __name__ == '__main__':
    unittest.main()