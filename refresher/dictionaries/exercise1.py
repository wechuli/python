donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5,
                 stan=150.0, lisa=50.25, harrison=10.0)


print(donations)

total_donations = 0

for donation in donations.values():
    total_donations += donation

print(total_donations)

# or using a list comprehension

total_donations2 = sum(donation for donation in donations.values())
print(f"Donations2: {total_donations2}")

# or even better

total_donations3 = sum(donations.values())
print(f'Donations3: {total_donations3}')
