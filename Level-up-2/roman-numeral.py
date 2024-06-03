# This function converts a Roman numeral to an integer.
def RomantoNum(prompt)->str:
# Dictionary 'romans' stores the Roman numeral symbols and their corresponding values.
    romans = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    # Initialize 'numeral' to 0, which will store the final integer value.
    numeral = 0
    # Iterate through each character in the input 'prompt' to process the Roman numeral.
    for i in range(len(prompt)):
        # Check if the current Roman numeral is smaller than the next one.
        if i + 1 < len(prompt) and (romans[prompt[i]] < romans[prompt[i+1]]):
            # Subtract the current numeral from 'numeral'.
            numeral -= romans[prompt[i]]
        else:
            # Add the current numeral to 'numeral'.
            numeral += romans[prompt[i]]
    # Return the resulting integer value.
    return numeral

