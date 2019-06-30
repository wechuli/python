import time

gen_start_time = time.time()
print(sum(n for n in range(100000000)))
timespan_gen = time.time() - gen_start_time
print(f"Timespan for generator: {timespan_gen}")


list_start_time = time.time()
print(sum([n for n in range(100000000)]))
timespan_list = time.time() - list_start_time
print(f"Timespan for list: {timespan_list}")
