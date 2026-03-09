import random
from simpleai.search import SearchProblem
from simpleai.search.local import genetic

N = 8


class NQueensGenetic(SearchProblem):
    def generate_random_state(self):
        """
        Tạo 1 cá thể (chromosome) ngẫu nhiên.
        Ví dụ: (2, 0, 3, 1, 5, 4, 7, 6)
        """
        return tuple(random.randint(0, N - 1) for _ in range(N))

    def value(self, state):
        """
        Hàm Fitness (Chấm điểm):
        - GA luôn thích điểm CAO (khác với Hill Climbing ban nãy ta dùng điểm âm).
        - Tổng số cặp quân hậu trên bàn cờ 8x8 là: (8 * 7) / 2 = 28 cặp.
        - Ta đếm số cặp KHÔNG CẮN NHAU. Điểm tối đa là 28.
        """
        attacking_pairs = 0
        for i in range(N):
            for j in range(i + 1, N):
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    attacking_pairs += 1

        return 28 - attacking_pairs  # Điểm càng cao cá thể càng khỏe

    def crossover(self, state1, state2):
        """
        Lai ghép (Crossover):
        Chọn ngẫu nhiên 1 điểm cắt. Lấy nửa đầu của cha ghép với nửa sau của mẹ.
        Ví dụ: Cha (0,0,0,0 | 0,0,0,0) lai Mẹ (1,1,1,1 | 1,1,1,1) -> Con (0,0,0,0, 1,1,1,1)
        """
        cut_point = random.randint(1, N - 1)
        child = state1[:cut_point] + state2[cut_point:]
        return child

    def mutate(self, state):
        """
        Đột biến (Mutation):
        Chọn ngẫu nhiên 1 cột, và dời quân hậu ở cột đó sang 1 hàng ngẫu nhiên khác.
        """
        mutated_state = list(state)
        random_col = random.randint(0, N - 1)
        random_row = random.randint(0, N - 1)

        mutated_state[random_col] = random_row
        return tuple(mutated_state)


# --- THIẾT LẬP THAM SỐ (Giống trong ảnh lý thuyết của bạn) ---

# SimpleAI yêu cầu truyền initial_state cho có lệ (dù GA sẽ tự tạo quần thể mới)
dummy_state = tuple([0] * N)
problem = NQueensGenetic(initial_state=dummy_state)

print("Đang chạy Thuật toán Di truyền (Tiến hóa thế hệ)...")

# Map các tham số trong ảnh của bạn vào hàm của simpleai:
# 1. n (population_size): Số lượng cá thể trong 1 thế hệ (VD: 100)
# 2. r_mu (mutation_chance): Tỉ lệ đột biến (VD: 0.1 tương đương 10%)
# 3. theta (fitness_threshold): Ngưỡng điểm dừng lại (Với N=8, điểm hoàn hảo là 28)
# 4. iterations_limit: Số thế hệ tiến hóa tối đa trước khi bỏ cuộc (VD: 500)

result_ga = genetic(
    problem,
    population_size=100,
    mutation_chance=0.1,
    iterations_limit=500
)

print("\n--- KẾT QUẢ TIẾN HÓA ---")
print(f"Trạng thái tốt nhất: {result_ga.state}")
print(f"Điểm Fitness: {problem.value(result_ga.state)} / 28")

if problem.value(result_ga.state) == 28:
    print("-> TUYỆT VỜI! Đã tiến hóa thành công ra đáp án hoàn hảo!")
else:
    print("-> Tiến hóa chưa tới đích. Cần tăng số thế hệ (iterations) hoặc quần thể (population) lên.")