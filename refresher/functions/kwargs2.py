

def combine_words(word, **kwargs):
    if 'prefix' in kwargs.keys():
        prefix = kwargs['prefix']
        return f'{prefix}{word}'
    elif 'suffix' in kwargs.keys():
        suffix = kwargs['suffix']
        return f'{word}{suffix}'
    else:
        return word


print(combine_words('child'))
print(combine_words('child', prefix='man'))
print(combine_words('child', suffix='ish'))
