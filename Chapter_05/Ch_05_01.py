# Selection sort algorithm
def select_sort(elements):
    size = len(elements)
    for i in range(size - 1):
        min_index = i
        min_value = elements[i]
        for j in range(i+1, size):
            if min_value > elements[j]:
                min_index = j
                min_value = elements[j]
        elements[min_index] = elements[i]
        elements[i] = min_value


if __name__ == '__main__':
    a = ['T', 'O', 'L', 'E', 'A', 'R', 'N', 'S', 'O', 'R', 'T', 'A', 'L', 'G', 'O', 'R', 'I', 'T', 'H', 'M']
    print("Original : ", a)
    select_sort(a)
    print("Sorted : ", a)
