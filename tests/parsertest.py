import unittest
from src.parser import Parser

class ParserTest(unittest.TestCase):
    def test_parse_json(self):
        a, b, c, d  = Parser(jsonpath='test-supervisor.json').parseJson
        self.assertEqual(a, ["sleep 10 && exit 1", "sleep 5 && exit 0"])
        self.assertEqual(b, '10')
        self.assertEqual(c, '5')
        self.assertEqual(d, '3')

if __name__ == '__main__':
    unittest.main()
