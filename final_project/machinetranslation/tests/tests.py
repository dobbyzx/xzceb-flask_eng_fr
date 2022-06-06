import unittest

from translator import frenchtoenglish, englishtofrench

class TestTranslator(unittest.TestCase):
    def test_frenchtoenglish(self):
        self.assertEqual(frenchtoenglish(' '),' ')
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')
        self.assertNotEqual(frenchtoenglish('Bonjour'),'Bonjour')
        self.assertNotEqual(frenchtoenglish(0),0)

    def test_englishtofrench(self):
        self.assertEqual(englishtofrench(' '),' ')
        self.assertEqual(englishtofrench('Hello'),'Bonjour')
        self.assertNotEqual(englishtofrench('Hello'),'Hello')
        self.assertNotEqual(englishtofrench(0),0)

unittest.main()