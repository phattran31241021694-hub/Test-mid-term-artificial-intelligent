from simpleai.search import CspProblem, backtrack

N = 8

# 1. KHAI BÁO BIẾN (Variables):
# Ta có N quân hậu, giả định mỗi quân chắc chắn nằm ở 1 hàng riêng biệt (từ 0 đến N-1)
variables = list(range(N))

# 2. KHAI BÁO MIỀN GIÁ TRỊ (Domains):
# Mỗi quân hậu (biến) có thể được đặt ở bất kỳ cột nào từ 0 đến N-1
domains = {var: list(range(N)) for var in variables}


# 3. KHAI BÁO RÀNG BUỘC (Constraints):
def queen_constraint(vars, values):
    """
    Hàm kiểm tra 2 quân hậu có cắn nhau không.
    vars: tuple chứa 2 hàng đang xét (ví dụ: hàng 0 và hàng 1)
    values: tuple chứa 2 cột đang thử đặt (ví dụ: cột 2 và cột 5)
    """
    row1, row2 = vars
    col1, col2 = values

    # Vi phạm 1: Trùng cột
    if col1 == col2:
        return False

    # Vi phạm 2: Nằm trên cùng đường chéo
    # (Khoảng cách giữa 2 hàng == khoảng cách giữa 2 cột)
    if abs(row1 - row2) == abs(col1 - col2):
        return False

    return True  # Hợp lệ


constraints = []
# Ép ràng buộc "queen_constraint" lên TẤT CẢ các cặp quân hậu trên bàn cờ
for i in range(N):
    for j in range(i + 1, N):
        # Mỗi ràng buộc là một tuple: ((biến_1, biến_2), hàm_kiểm_tra)
        constraints.append(((i, j), queen_constraint))

# --- TIẾN HÀNH CHẠY THUẬT TOÁN ---

print("Đang đóng gói bài toán CSP...")
problem = CspProblem(variables, domains, constraints)

print("Đang giải bằng SimpleAI Backtrack...")
# Hàm backtrack sẽ tự động thử -> sai -> quay lui cho đến khi thỏa mãn MỌI ràng buộc
result = backtrack(problem)

print("\n--- KẾT QUẢ ---")
if result:
    print("Đã tìm ra đáp án!")
    print("Vị trí cột của các quân hậu từ hàng 0 đến hàng 7 lần lượt là:")
    print(result)
else:
    print("Không tìm thấy đáp án hợp lệ.")