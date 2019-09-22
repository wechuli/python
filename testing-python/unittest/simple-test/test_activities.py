import unittest
from activities import eat, nap, is_funny, laugh


class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """Testing for eating healthy, should have healthy message"""
        self.assertEqual(eat("broccoli", is_healthy=True),
                         "I'm eating broccoli, its healthy")

    def test_eat_unhealthy(self):
        """Testing for eating un healthy, should have an unhealthy message"""
        self.assertEqual(eat("pizza", is_healthy=False),
                         "I'm eating pizza, because YOLO!")

    def test_eat_healthy_boolean(self):
        """is_healthy must be a boolean"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares?")

    def test_short_nap(self):
        """Testing for short nap, should feel refreshed"""
        self.assertEqual(nap(1), "I'm feeling refreshed after my 1 hour nap")

    def test_long_nap(self):
        """Testing for long nap, should feel grouchy"""
        self.assertEqual(
            nap(3), "Ugh I overslept. I didn't mean to nap for 3 hours")

    def test_is_funny(self):
        "Test if someone is funny"
        self.assertFalse(is_funny("tim"), "tim should not be funny")
        # assertFalse checks the for it to be False

    def test_is_funny_anyone_else(self):
        """ Anyone else but tim should be funny"""
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")

    def test_laugh(self):
        """Check if result of laugh is in a tuple"""
        self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))


if __name__ == "__main__":
    unittest.main()
