import re
profanity_regex = re.compile(r'\bfrack\b|frack[a-z-]+', re.IGNORECASE)


def censor(raw_string):
    return profanity_regex.sub('CENSORED', raw_string)


print(censor("This is some clean stuff, no censoring should happen"))
print(censor("Frack you"))
print(censor("I hope you fracking die"))
print(censor("you fracking Frack"))
