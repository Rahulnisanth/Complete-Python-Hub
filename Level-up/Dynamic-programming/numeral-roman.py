# This function converts an integer to a Roman numeral.
def NumtoRoman(num)->int:
# Dictionary 'numerals' stores the Roman numeral symbols and their corresponding values.
    numerals = {
        1: "I",
        5: "V", 4: "IV",
        10: "X", 9: "IX",
        50: "L", 40: "XL",
        100: "C", 90: "XC",
        500: "D", 400: "CD",
        1000: "M", 900: "CM",
    }
    # Initialize an empty string 'roman' to store the Roman numeral representation.
    roman = ''
    # Loop through the numerals in descending order to build the Roman numeral.
    for k in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        while k <= num:
            roman += numerals[k]
            num -= k
    # Return the resulting Roman numeral string.
    return roman


