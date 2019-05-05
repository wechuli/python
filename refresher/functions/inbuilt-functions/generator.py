import sys

list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print(f'{list_comp} bytes')
print(f'{gen_exp} bytes')
