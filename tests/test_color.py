import unittest

from src.color import Color


class TestColor(unittest.TestCase):

    def test_valid_hex_initialization(self):
        color = Color("#FFFFFF")
        self.assertEqual(color.red, 255)
        self.assertEqual(color.green, 255)
        self.assertEqual(color.blue, 255)

    def test_invalid_hex_initialization(self):
        with self.assertRaises(ValueError):
            Color("ZZZZZZ")
        with self.assertRaises(ValueError):
            Color("#12345")
        with self.assertRaises(ValueError):
            Color("123456")

    def test_brightness_calculation(self):
        color = Color("#000000")
        self.assertEqual(color.brightness_value, 0.0)

        color = Color("#FFFFFF")
        self.assertAlmostEqual(color.brightness_value, 255.0, delta=0.1)

        color = Color("#808080")
        self.assertAlmostEqual(color.brightness_value, 128.0, delta=0.1)

    def test_comparison_operators(self):
        color1 = Color("#000000")
        color2 = Color("#FFFFFF")
        color3 = Color("#808080")

        self.assertTrue(color1 < color2)
        self.assertTrue(color1 <= color3)
        self.assertTrue(color2 > color3)
        self.assertTrue(color2 >= color1)
        self.assertFalse(color1 > color2)
        self.assertFalse(color3 < color1)

    def test_hex_to_rgb(self):
        color = Color("#123456")
        self.assertEqual(color.hex_to_rgb("#123456"), (18, 52, 86))

    def test_is_valid_hex(self):
        color = Color("#FFFFFF")
        self.assertTrue(color.is_valid_hex("#FFFFFF"))
        self.assertTrue(color.is_valid_hex("#000000"))
        self.assertFalse(color.is_valid_hex("ZZZZZZ"))
        self.assertFalse(color.is_valid_hex("#12345"))
        self.assertFalse(color.is_valid_hex("123456"))

if __name__ == "__main__":
    unittest.main()