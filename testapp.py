import main as m
import unittest

class TestProgramme(unittest.TestCase):

    def testlogin(self):
        u = m.user("consultant","Nouveau123","Lecture")
        self.assertEqual(u.login(), "consultant")

if __name__ == "__main__":
    unittest.main()