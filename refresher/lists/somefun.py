
a = ['jess', 'mercy', 'brian', 'john', 'doe','jane','phil','brody','kevin','cathy']
b = ['paul', 'brian', 'johny', 'jess','phil','jane']


def findunique(a, b):
    unique = list()
    for item in a:
        for anoitem in b:
            if item == anoitem:
                unique.append(item)

    return unique


print(findunique(a, b))
