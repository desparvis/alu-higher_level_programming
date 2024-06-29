#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    result = 0
    n = len(roman_string)
    
    for i in range(n):
        value = roman_dict.get(roman_string[i], 0)
        if i < n - 1:
            next_value = roman_dict.get(roman_string[i + 1], 0)
            if value < next_value:
                result -= value
            else:
                result += value
        else:
            result += value
    
    return result

