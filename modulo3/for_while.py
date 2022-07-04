import time

# With for loop
start = time.time()
acc = 0
for index in range(int(1e5)):
    acc += index

end = time.time()
print('Time spent with for loop {:.6f}'.format(end - start))


# With while loop
start = time.time()
i = 0
acc = 0
while i <= 1e5:
    acc += i
    i = i + 1

end = time.time()
print('Time spent with while loop {:.6f}'.format(end - start))

