# The locale module accesses a database of culture specific data formats. 
# The grouping attribute of locale’s format function provides a direct way of formatting numbers with group separators:

import locale

print(locale.locale_alias)
print()
# print(locale.setlocale(locale.LC_ALL, 'english_united-states.437'))
print(locale.setlocale(locale.LC_ALL, 'en_US.utf8'))
conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
print(locale.format("%d", x, grouping=True))
print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))
