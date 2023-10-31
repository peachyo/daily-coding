# O(n*K^2) time O(n*k)
def build_houses(matrix):
    n = len(matrix)
    k = len(matrix[0])
    solution_matrix = [[0]*k]

    for r, row in enumerate(matrix):
        row_cost = []
        for c, val in enumerate(row):
            row_cost.append(
                min(solution_matrix[r][i]
                                for i in range(k) if i != c) + val)
        solution_matrix.append(row_cost)

    return min(solution_matrix[-1])


def build_houses2(matrix):
    k = len(matrix[0])
    solution_row = [0] * k
    for r, row in enumerate(matrix):
        new_row = []
        for c, val in enumerate(row):
            new_row.append(min(solution_row[i] for i in range(k) if i != c) + val)
        solution_row = new_row
    return min(solution_row)