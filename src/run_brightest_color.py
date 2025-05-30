from color import Color
from typing import List

def main(hex_list: List[str] = ["#AABBCC", "#154331", 
                                "#A0B1C2", "#000000", "#FFFFFF"]):
    """Main function to return the brightest color from a list of hex colors.
       The function will return the first occurence of the brightest color"""
    
    if len(hex_list) < 1:
        print('Please provide two or more hex values.')
        return
    
    colors = [Color(hex_value) for hex_value in hex_list]

    brightest_color = max(colors)

    color_name = brightest_color.get_color_name()

    if color_name:
        print('\n --- Brightest Color (w/ Name) ---')
        print(f'The brightest color is: {color_name} ' \
              f'(r={brightest_color.red}, g={brightest_color.green}, ' \
              f'b={brightest_color.blue}), called {color_name}.')
        
    else:
        print('\n --- Brightest Color (w/o Name) ---')
        print(f'The brightest color is: {brightest_color.hex_value}' \
            f'(r={brightest_color.red}, g={brightest_color.green}, ' \
            f'b={brightest_color.blue})')



if __name__ == "__main__":
    main()