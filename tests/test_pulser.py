import unittest
from src.pulser import Pulser, lerp

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


class TestLerp(unittest.TestCase):

    def test_full_a(self):
        self.assertEqual(50, lerp(50, 150, 0))

    def test_full_b(self):
        self.assertEqual(150, lerp(50, 150, 1))

    def test_mid(self):
        self.assertEqual(100, lerp(50, 150, 0.5))

    def test_negative_slope(self):
        self.assertEqual(150, lerp(150, 50, 0))
        self.assertEqual(100, lerp(150, 50, 0.5))
        self.assertEqual(50, lerp(150, 50, 1))


class TestsStaticColor(unittest.TestCase):

    def test_always_at_primary(self):
        pulser = Pulser(primary=YELLOW)
        for i in range(100):
            s = i / 5
            self.assertEqual(YELLOW, pulser.seconds(s))


class TestsSinglePulsingColor(unittest.TestCase):

    def test_at_primary_to_start_with(self):
        pulser = Pulser(primary=YELLOW, hz=2)
        self.assertEqual(YELLOW, pulser.seconds(0))

    def test_at_black_in_half_time(self):
        pulser = Pulser(primary=YELLOW, hz=2)
        self.assertEqual(BLACK, pulser.seconds(0.25))

    def test_at_yellow_in_full_time(self):
        pulser = Pulser(primary=YELLOW, hz=2)
        self.assertEqual(YELLOW, pulser.seconds(0.5))


class TwoColorTests(unittest.TestCase):
    def setUp(self):
        # Pulse from YELLOW to RED with 1 Hz
        self.pulser = Pulser(hz=1, primary=YELLOW, secondary=RED)

    def test_starts_at_primary(self):
        self.assertEqual(YELLOW, self.pulser.seconds(0))

    def test_ends_at_primary(self):
        self.assertEqual(YELLOW, self.pulser.seconds(1))

    def test_inbetween_is_secondary(self):
        self.assertEqual(RED, self.pulser.seconds(0.5))
        self.assertEqual(RED, self.pulser.seconds(1.5))


if __name__ == '__main__':
    unittest.main()
