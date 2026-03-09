import heapq

# Khai báo đồ thị: Node -> {Hàng xóm: Chi phí}
graph = {
    'S': {'A': 2, 'B': 5},
    'A': {'C': 2, 'D': 4},
    'B': {'D': 1, 'G': 6},
    'C': {'G': 3},
    'D': {'G': 1},
    'G': {}
}


def bfs(graph, start, goal):
    queue = [(start, [start])]  # Lưu tuple: (Node hiện tại, Đường đã đi)
    visited = set()

    while queue:
        node, path = queue.pop(0)  # Lấy phần tử đầu tiên ra (FIFO)

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))
    return None


def ucs(graph, start, goal):
    # Lưu tuple: (Tổng chi phí, Node hiện tại, Đường đã đi)
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)  # Luôn lấy đường có cost NHỎ NHẤT

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')


def dfs(graph, start, goal):
    stack = [(start, [start])]  # Lưu tuple giống BFS
    visited = set()

    while stack:
        node, path = stack.pop()  # Lấy phần tử CUỐI CÙNG ra (LIFO)

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append((neighbor, path + [neighbor]))
    return None
def dls(graph, node, goal, depth, path):
    if depth == 0 and node == goal:
        return path
    if depth > 0:
        for neighbor in graph[node]:
            # Đệ quy xuống tầng dưới, giảm độ sâu đi 1
            result = dls(graph, neighbor, goal, depth - 1, path + [neighbor])
            if result:
                return result
    return None

def ids(graph, start, goal, max_depth):
    # Thử dần từng độ sâu từ 0 đến max_depth
    for limit in range(max_depth):
        result = dls(graph, start, goal, limit, [start])
        if result:
            return result
    return None
start_node = 'S'
goal_node = 'G'

print(f"Bản đồ từ {start_node} đến {goal_node}:")

# BFS tìm ít chặng nhất
print("1. BFS (Ít trạm dừng nhất):", bfs(graph, start_node, goal_node))

# UCS tìm đường đi rẻ nhất (chi phí thấp nhất)
path, cost = ucs(graph, start_node, goal_node)
print(f"2. UCS (Đường ngắn nhất thực tế): {path} với chi phí {cost}")

# DFS sẽ tìm thấy bất kỳ đường nào nó đụng đầu tiên
print("3. DFS (Đi mù):", dfs(graph, start_node, goal_node))

# IDS giới hạn tìm kiếm
print("4. IDS (Độ sâu tối đa 4):", ids(graph, start_node, goal_node, 4))