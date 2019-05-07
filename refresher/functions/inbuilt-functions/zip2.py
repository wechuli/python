midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']


# using dict comprehension
final_grades = [max(pair) for pair in zip(midterms, finals)]
finals_for_real = dict(zip(students, final_grades))
print(final_grades)
print(finals_for_real)


# or using a dictionary comprehension

final_grades_d = {t[0]: max(t[1], t[2])
                  for t in zip(students, midterms, finals)}

print(final_grades_d)

# using lambda
scores = zip(students, map(lambda pair: max(pair), zip(midterms, finals)))

print(dict(scores))
# get average instead
scores_avg = zip(students, map(lambda pair: (
    (pair[0] + pair[1])/2), zip(midterms, finals)))
print(dict(scores_avg))
