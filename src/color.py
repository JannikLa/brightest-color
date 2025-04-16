from typing import Tuple
import math
import requests

class Color:
    def __init__(self, hex_value: str):
        if not self.is_valid_hex(hex_value):
            raise ValueError(f"Invalid hex color value: {hex_value}")
        
        self.hex_value: str = hex_value
        self.red, self.green, self.blue = self.hex_to_rgb(hex_value)
        self.brightness_value: float = self.brightness()

    def __lt__(self, other: 'Color') -> bool:
        """Compare colors based on brightness (less than)."""
        return self.brightness_value < other.brightness_value

    def __le__(self, other: 'Color') -> bool:
        """Compare colors based on brightness (less than or equal)."""
        return self.brightness_value <= other.brightness_value

    def __gt__(self, other: 'Color') -> bool:
        """Compare colors based on brightness (greater than)."""
        return self.brightness_value > other.brightness_value

    def __ge__(self, other: 'Color') -> bool:
        """Compare colors based on brightness (greater than or equal)."""
        return self.brightness_value >= other.brightness_value

    def hex_to_rgb(self, hex_value: str) -> Tuple[int, int, int]:
        """Convert a hex color string to an RGB tuple."""
        hex_value = hex_value.lstrip('#')
        return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))

    def is_valid_hex(self, hex_value: str) -> bool:
        """Validate the hex color string."""
        if not hex_value or not isinstance(hex_value, str):
            return False
        hex_value = hex_value.lstrip('#')
        is_hex = (len(hex_value) == 6 and 
                  all(c in '0123456789ABCDEFabcdef' for c in hex_value))
        return is_hex
    
    def brightness(self) -> float:
        """Calculate brightness using the furmular: 
            sqrt(0.241 R^2 + 0.691 G^2 + 0.068 B^2)."""
        return math.sqrt(
            0.241 * (self.red ** 2) + 
            0.691 * (self.green ** 2) + 
            0.068 * (self.blue ** 2)
        )