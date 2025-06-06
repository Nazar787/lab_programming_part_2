def zigzag(matrix):
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    new_matrix = []

    for i in range(m):
        if i % 2 == 0:
            new_matrix.extend(matrix[i])
        else:
            new_matrix.extend(matrix[i][::-1])

    return new_matrix



