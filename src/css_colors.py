import math
import requests
from typing import Tuple

class CSS_Colors:
    def __init__(self, url: str = "https://csscolorsapi.com/api/colors"):
        self.url = url
        self.colors = self.get_colors()

    def get_colors(self) -> list:
        """Fetch colors from the API."""
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()['colors']
        else:
            raise Exception(f"Failed to fetch colors." \
                            f"Status code: {response.status_code}")
        
    @staticmethod
    def euclidean_distance(color1: Tuple[int, int, int], 
                           color2: Tuple[int, int, int]) -> float:
        """Calculate the Euclidean distance between two RGB colors."""
        if len(color1) != 3 or len(color2) != 3:
            raise ValueError("Both colors must be tuples of length 3.")
        
        return math.sqrt(sum((color1[i] - color2[i]) ** 2 for i in range(3)))
        
    def get_matching_color_name(self, red: int, green: int, blue: int) -> str:
        """
        Determines the name of the color that most closely matches the given 
        RGB values based on the euclidian distance between the RGB values.
        Args:
            red (int): The red component of the input color (0-255).
            green (int): The green component of the input color (0-255).
            blue (int): The blue component of the input color (0-255).
        Returns:
            str: The name of the closest CSS color match.
        """
        closest_color = None
        min_distance = float('inf')

        for color in self.colors:
            color_rgb = tuple(map(int, color['rgb'].split(',')))
            # Calculate the Euclidean distance
            distance = self.euclidean_distance((red, green, blue), color_rgb)
            if distance < min_distance:
                min_distance = distance
                closest_color = color['name']

        return closest_color