import unittest
from unittest.mock import patch, MagicMock

from src.css_colors import CSS_Colors

class TestCSSColors(unittest.TestCase):
    @patch('src.css_colors.requests.get')
    def setUp(self, mock_get):
        # Mock API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "colors": [
                {"name": "red", "rgb": "255,0,0"},
                {"name": "green", "rgb": "0,255,0"},
                {"name": "blue", "rgb": "0,0,255"},
                {"name": "black", "rgb": "0,0,0"},
                {"name": "white", "rgb": "255,255,255"}
            ]
        }
        mock_get.return_value = mock_response
        self.css_colors = CSS_Colors()

    def test_get_colors(self):
        self.assertEqual(len(self.css_colors.colors), 5)
        self.assertEqual(self.css_colors.colors[0]['name'], 'red')

    def test_euclidean_distance(self):
        distance = CSS_Colors.euclidean_distance((255, 0, 0), (0, 255, 0))
        self.assertAlmostEqual(distance, 360.624, places=3)

    def test_get_matching_color_name_exact_match(self):
        color_name = self.css_colors.get_matching_color_name(255, 0, 0)
        self.assertEqual(color_name, 'red')

    def test_get_matching_color_name_closest_match(self):
        color_name = self.css_colors.get_matching_color_name(250, 10, 10)
        self.assertEqual(color_name, 'red')

    @patch('src.css_colors.requests.get')
    def test_get_colors_api_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            CSS_Colors()
        self.assertIn("Failed to fetch colors", str(context.exception))

    def test_invalid_rgb_length_in_distance(self):
        with self.assertRaises(ValueError):
            CSS_Colors.euclidean_distance((255, 0), (0, 255, 0))

if __name__ == '__main__':
    unittest.main()