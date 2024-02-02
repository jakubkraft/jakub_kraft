class RomanConverter:
    def __init__(self):
        self.roman_to_num = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        }
        self.num_to_roman = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }

    def to_roman(self, num):
        roman = ''
        for value in sorted(self.num_to_roman.keys(), reverse=True):
            while num >= value:
                roman += self.num_to_roman[value]
                num -= value
        return roman

    def from_roman(self, roman):
        num = 0
        i = 0
        while i < len(roman):
            if i+1 < len(roman) and roman[i:i+2] in self.roman_to_num:
                num += self.roman_to_num[roman[i:i+2]]
                i += 2
            else:
                num += self.roman_to_num[roman[i]]
                i += 1
        return num

def main():
    converter = RomanConverter()
    try:
        user_input = int(input("Zadejte celé číslo v desítkové soustavě: "))
        roman_numeral = converter.to_roman(user_input)
        converted_back = converter.from_roman(roman_numeral)

        print(f"Zde je jeho reprezentace římskými číslicemi: {roman_numeral}")
        print(f"Číslo zpět převedeno do desítkové soustavy: {converted_back}")
    except ValueError:
        print("Nezadali jste celé číslo v desítkové soustavě.")

main()

