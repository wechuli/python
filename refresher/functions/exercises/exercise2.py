

def yell(what):
    try:
        what = str(what)
    except:
        print('Invalid entry')
        exit()

    return f'{what.upper()}!'


myyell = yell('This is so stupid or am done')

print(myyell)
