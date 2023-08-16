def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

def print_centered_pascals_triangle(num_rows):
    max_width = len(str(binomial_coefficient(num_rows - 1, num_rows // 2)))

    for i in range(num_rows):
        spaces_before = (max_width + 1) * (num_rows - i - 1)
        print(" " * spaces_before, end="")

        for j in range(i + 1):
            value = binomial_coefficient(i, j)
            print(f"{value:>{max_width}}", end=" ")

        print()

num_rows = int(input("Enter the number of rows for Pascal's triangle: "))
print_centered_pascals_triangle(num_rows)

'''
Output: Enter the number of rows for Pascal's triangle: 6
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
   1 5 10 10 5 1
'''