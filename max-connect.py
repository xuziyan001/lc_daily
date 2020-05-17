
def dfs(matrix, i, j, stack=set()):
    m = len(matrix)
    if m == 0:
        return 0
    n = len(matrix[0])
    if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] != 1 or (i, j) in stack:
        return 0
    # use stack to eliminate replication, here needs to be shared
    stack.add((i, j))
    down = dfs(matrix, i+1, j, stack)
    up = dfs(matrix, i-1, j, stack)
    right = dfs(matrix, i, j+1, stack)
    left = dfs(matrix, i, j-1, stack)
    return 1 + down + up + right + left


def max_connect(input_matrix):
    output = 0
    for i, j in enumerate(input_matrix):
        for k, l in enumerate(j):
            s = set()
            output = max(dfs(input_matrix, i, k, s), output)
    return output


if __name__ == "__main__":
    matrix = [
        [1,0,0,1,0,1],
        [0,1,1,1,0,1],
        [1,1,0,1,0,0],
        [0,1,0,1,0,0],
        [1,1,0,1,0,1]]
    assert (max_connect(matrix) == 12)

    matrix = [[0]]
    assert (max_connect(matrix) == 0)

    matrix = [[0,0],[0,0]]
    assert (max_connect(matrix) == 0)

    matrix = []
    assert (max_connect(matrix) == 0)

