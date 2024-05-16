def decode_matrix_script(matrix, n, m):
    import re

    # Read the matrix column by column
    columns = [''.join([matrix[row][col] for row in range(n)]) for col in range(m)]

    # Join columns into a single string
    combined = ''.join(columns)

    # Replace non-alphanumeric sequences between alphanumeric characters with a single space
    decoded = re.sub(r'(?<=\w)(\W+)(?=\w)', ' ', combined)

    return decoded

# Input example
input_data = """
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
"""

# Parse the input
input_lines = input_data.strip().split('\n')
n, m = map(int, input_lines[0].split())
matrix = input_lines[1:]

# Decode the matrix script
result = decode_matrix_script(matrix, n, m)

# Output the result
print(result)