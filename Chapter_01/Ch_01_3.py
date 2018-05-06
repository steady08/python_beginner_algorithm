# Erastosthenes's sieve

MAX_RANGE = 9999

numbers = []
for i in range(MAX_RANGE+1):
    numbers.append(0)

for i in range(2, MAX_RANGE+1):
    # If value is '1', it was deleted
    if numbers[i] == 1:
        continue
    for j in range(i+i, MAX_RANGE+1, i):
        # Delete values which are multiple i. Value '1' means, it was deleted.
        numbers[j] = 1

for i in range(2, MAX_RANGE+1):
    if numbers[i] != 1:
        # To print one line, use 'end=" "'
        print(i, end=" "),
print()

