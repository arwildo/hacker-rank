#arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0],
#       [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
#
#[print(i) for i in arr]
#print()
#print()


def maxHGSum(arr):
    row, col = 0, 0
    total_sum = []

    for row in range(0, 4):
        for col in range(0, 4):
            sum = 0
            sum += (arr[row][col])
            sum += (arr[row][col + 1])
            sum += (arr[row][col + 2])
            sum += (arr[row + 1][col + 1])
            sum += (arr[row + 2][col])
            sum += (arr[row + 2][col + 1])
            sum += (arr[row + 2][col + 2])

            total_sum.append(sum)

    return max(total_sum)


if __name__ == "__main__":
    arr = []
        for arr_i in range(6):
        arr_temp = list(map(int,input().strip().split(' ')))
        arr.append(arr_temp)
    print(maxHGSum(arr))
