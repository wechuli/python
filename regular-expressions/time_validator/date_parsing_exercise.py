# Define a function called parse_date that accepts a single string. Your code should check to see if the string matches a date format. We're goind to use the BMY format of dd/mm/yyy but it should also work with dd.mm.yyyy and dd,mm,yyyy.Rather than simply returning True or False if the string matches.. you should instead return a dictionary conatining three parts of the date with keys d,m and yes
import re

date_regex = re.compile(
    "^(?P<d>[0-3][0-9])(,|/|-|.)(?P<m>[0-1][0-9])(,|/|-|.)(?P<y>[0-9]{4})$")


def parse_date(date):
    match = date_regex.search(date)
    if match == None:
        return None
    return{
        'd': match.group('d'),
        'm': match.group('m'),
        'y': match.group('y')
    }


print(parse_date("12,04,2003"))
print(parse_date("12.11.2003"))
print(parse_date("12.11.200312"))
print(parse_date("13/22/1999"))
