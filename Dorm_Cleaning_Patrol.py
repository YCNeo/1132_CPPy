def bfs(dorms, cur, visited):
    queue = [cur]
    visited.add(cur)
    while queue:
        x, y = queue.pop(0)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(dorms)
                and 0 <= ny < len(dorms)
                and dorms[nx][ny] == "#"
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                queue.append((nx, ny))


N = int(input())

for _ in range(N):
    n = int(input())
    dorms = []
    group = 0
    visited = set()
    for i in range(n):
        dorm = list(input().strip())
        dorms.append(dorm)

    for i, j in [(x, y) for x in range(n) for y in range(n)]:
        if dorms[i][j] == "#" and (i, j) not in visited:
            bfs(dorms, (i, j), visited)
            group += 1
        else:
            continue

    print(group)
