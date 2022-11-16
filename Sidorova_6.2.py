def sequential_search(array):  # последовательный поиск
    count = 0
    for i in range(0, len(array)):
        count += sequential_search_for_elem(array, array[i])
    return count / len(array)


def sequential_search_for_elem(array, curr_elem):
    count = 0
    for i in range(0, len(array)):
        count += 1
        if array[i] == curr_elem:
            return count


def binary_search(array):  # двоичный поиск
    count = 0
    for i in range(0, len(array)):
        count += binary_search_for_elem(array, array[i])
    return count / len(array)


def binary_search_for_elem(array, curr_elem):
    left = 1
    right = len(array) - 1
    count = 0
    while left <= right:
        count += 1
        middle = (left + right) // 2
        if arr[middle] == curr_elem:
            return count
        if arr[middle] < curr_elem:
            left = middle + 1
        if arr[middle] > curr_elem:
            right = middle - 1
    return count


def interpolation_search(array):  # интерполяционный поиск
    count = 0
    for i in range(0, len(array)):
        count += interpolation_search_for_elem(array, array[i])
    return count / len(array)


def interpolation_search_for_elem(array, curr_elem):
    left = 0
    right = len(array) - 1
    count = 0
    while left <= right:
        count += 1
        next_elem = left + int(((right - left) / (array[right] - array[left])) * (curr_elem - array[left]))
        if arr[next_elem] == curr_elem:
            return count
        if arr[next_elem] < curr_elem:
            left = next_elem + 1
        if arr[next_elem] > curr_elem:
            right = next_elem - 1
    return count


fileInput = open('input.txt')
arr = []
line = fileInput.readline()
arr.extend([int(x) for x in line.split()])

# avg_count = sequential_search(arr)
# avg_count = binary_search(arr)
avg_count = interpolation_search(arr)

fileOutput = open('output.txt', 'w')
fileOutput.write("%s\n" % avg_count)

fileOutput.close()
fileInput.close()
