import multiprocessing
def sum_of_squares(start, end):
    return sum(x**2 for x in range(start, end + 1))
start = 1
end = 100
num_processes = 4
step = (end - start + 1)
with multiprocessing.Pool(processes=num_processes) as pool  :
    results = pool.starmap(sum_of_squares, [(i, i + step - 1) for i in range(start, end, step)])
total_sum = sum(results)
print(f"Sum of squares from {start} to {end} is {total_sum}")
