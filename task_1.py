# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

numbers = []
for dec in range(16):
    bin_str = bin(dec)
    oct_str = oct(dec)
    hex_str = hex(dec)
    numbers.append({'dec': dec, 'bin': bin_str, 'oct': oct_str, 'hex': hex_str})

pprint(numbers)
