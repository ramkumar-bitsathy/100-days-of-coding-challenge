def min_moves_to_reach_stair(X, Y):
    R = X % Y
    Q = X // Y
    if R == 0:
        return Q
    else:
        return Q + R
T = int(input().strip())
for _ in range(T):
    X, Y = map(int, input().split())
    min_moves = min_moves_to_reach_stair(X, Y)
    print(min_moves)
