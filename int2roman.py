roman_symbols = {
    0: "",
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

def Int2Roman(the_int):

    if not isinstance(the_int, int):
        raise TypeError("Int2Roman takes only integers"
                        " as input parameters.")

    elif the_int < 0 or the_int > 3999:
        raise ValueError("Int2Roman takes only integers between "
                         "zero and 3999 as input parameters.")

    return _make_roman(the_int)

def _make_roman(the_int):
    larger_decade = _get_larger_decade(the_int)
    running_roman = _make_roman_from_decade(larger_decade)
    remaining_int = the_int - larger_decade

    while remaining_int:

        larger_decade = _get_larger_decade(remaining_int)
        remaining_int -= larger_decade

        running_roman += _make_roman_from_decade(larger_decade)

    return running_roman

def _make_roman_from_decade(decade):
    if decade in roman_symbols:
        return roman_symbols[decade]
    elif _is_9_decade(decade):
        return _make_9_decade_roman(decade)
    elif _is_4_decade(decade):
        return _make_4_decade_roman(decade)
    else:
        return _make_added_decade_roman(decade)

def _get_larger_decade(the_int):
    if the_int == 0:
        return 0
    unit_decade = _get_unit_decade(the_int)
    return (the_int//unit_decade)*unit_decade

def _get_unit_decade(the_int):
    if the_int == 0:
        return 0
    return 10**(len(str(the_int))-1) #  Alternatively could use: math.floor(math.log10(the_int))

def _is_9_decade(decade):
    return 9 == decade // _get_unit_decade(decade)

def _is_4_decade(decade):
    return 4 == decade // _get_unit_decade(decade)

def _make_9_decade_roman(decade):
    unit_decade = _get_unit_decade(decade)
    return roman_symbols[unit_decade] + roman_symbols[10 * unit_decade]

def _make_4_decade_roman(decade):
    unit_decade = _get_unit_decade(decade)
    return roman_symbols[unit_decade] + roman_symbols[5 * unit_decade]

def _make_added_decade_roman(decade):
    unit_decade = _get_unit_decade(decade)

    added_roman_unit_deacdes = ""
    remaining_decade = decade

    while remaining_decade not in roman_symbols:
        remaining_decade -= unit_decade
        added_roman_unit_deacdes += roman_symbols[unit_decade]

    return roman_symbols[remaining_decade] + added_roman_unit_deacdes
