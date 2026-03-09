import random
from simpleai.search import SearchProblem
from simpleai.search.local import hill_climbing, hill_climbing_stochastic, hill_climbing_random_restarts

# Đặt số lượng quân hậu (và kích thước bàn cờ)
N = 8

class NQueensProblem(SearchProblem):
    def generate_random_state(self):
        """
        Hàm này bắt buộc phải có cho thuật toán Random Restarts.
        Tạo một trạng thái ngẫu nhiên: Trả về một tuple N phần tử.
        Ví dụ: (0, 3, 1, 4, ...) nghĩa là cột 0 hậu ở hàng 0, cột 1 hậu ở hàng 3...
        """
        return tuple(random.randint(0, N - 1) for _ in range(N))

    def actions(self, state):
        """
        Sinh ra các bước đi (trạng thái kề cận).
        Từ vị trí hiện tại, ta thử di chuyển từng quân hậu trong cột của nó sang các hàng khác.
        """
        possible_actions = []
        for col in range(N):
            current_row = state[col]
            for new_row in range(N):
                # Nếu khác hàng hiện tại thì mới là một bước di chuyển hợp lệ
                if new_row != current_row:
                    # Hành động được biểu diễn bằng tuple (cột_sẽ_đổi, hàng_mới)
                    possible_actions.append((col, new_row))
        return possible_actions

    def result(self, state, action):
        """
        Trạng thái mới sau khi thực hiện hành động.
        """
        col, new_row = action
        # Chuyển tuple thành list để có thể thay đổi giá trị
        new_state = list(state)
        new_state[col] = new_row
        return tuple(new_state) # Trả về tuple (yêu cầu của simpleai để hash state)

    def value(self, state):
        """
        Hàm đánh giá điểm số. Điểm càng cao càng tốt.
        Ta đếm số cặp quân hậu đang ăn nhau.
        Điểm = Âm của số cặp ăn nhau. (Tối ưu nhất là 0 cặp ăn nhau -> điểm 0).
        """
        attacking_pairs = 0
        for i in range(N):
            for j in range(i + 1, N):
                # Kiểm tra xem có ăn ngang (cùng hàng) hoặc ăn chéo không
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    attacking_pairs += 1
        return -attacking_pairs

# --- CHẠY THỬ NGHIỆM ---

# 1. Khởi tạo trạng thái ban đầu ngẫu nhiên
initial_state = tuple(random.randint(0, N - 1) for _ in range(N))
problem = NQueensProblem(initial_state=initial_state)

print(f"Trạng thái ban đầu: {initial_state}")
print(f"Điểm ban đầu: {problem.value(initial_state)} (Số âm biểu thị số cặp đang cắn nhau)\n")
print("-" * 50)

# 2. Chạy Hill Climbing truyền thống
result_hc = hill_climbing(problem)
print("1. Hill Climbing Truyền thống:")
print(f"   Trạng thái: {result_hc.state}")
print(f"   Điểm: {problem.value(result_hc.state)}")
print("   -> (Thường sẽ bị kẹt ở điểm âm, không đạt được 0)\n")

# 3. Chạy Stochastic Hill Climbing (Leo đồi ngẫu nhiên)
result_shc = hill_climbing_stochastic(problem)
print("2. Stochastic Hill Climbing:")
print(f"   Trạng thái: {result_shc.state}")
print(f"   Điểm: {problem.value(result_shc.state)}\n")

# 4. Chạy Random Restarts Hill Climbing (Khởi động lại ngẫu nhiên)
# Cho phép thuật toán "đập đi xây lại" tối đa 20 lần nếu bị kẹt
result_rr = hill_climbing_random_restarts(problem, restarts_limit=20)