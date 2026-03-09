import math

# Khởi tạo bàn cờ 3x3 dưới dạng mảng 1 chiều (9 ô từ 0 đến 8)
# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8
board = [' ' for _ in range(9)]

# AI là 'X' (Max), Người là 'O' (Min)
AI = 'X'
HUMAN = 'O'


def print_board(b):
    print(f"\n {b[0]} | {b[1]} | {b[2]} ")
    print("---+---+---")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("---+---+---")
    print(f" {b[6]} | {b[7]} | {b[8]} \n")


def check_winner(b):
    """Kiểm tra xem ai chiến thắng, hoặc hòa"""
    win_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Hàng ngang
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Hàng dọc
        [0, 4, 8], [2, 4, 6]  # Đường chéo
    ]
    for line in win_lines:
        if b[line[0]] == b[line[1]] == b[line[2]] and b[line[0]] != ' ':
            return b[line[0]]  # Trả về 'X' hoặc 'O'

    if ' ' not in b:
        return 'Tie'  # Hòa

    return None  # Trò chơi chưa kết thúc


def minimax(b, is_maximizing):
    """
    Thuật toán Minimax: Đệ quy vét cạn mọi kịch bản để chấm điểm.
    - AI (X) muốn điểm cao nhất (+1)
    - Người (O) muốn điểm thấp nhất (-1)
    - Hòa được 0 điểm
    """
    winner = check_winner(b)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif winner == 'Tie':
        return 0

    if is_maximizing:
        best_score = -math.inf  # Khởi tạo điểm thấp nhất có thể
        for i in range(9):
            if b[i] == ' ':
                b[i] = AI  # Đánh thử
                score = minimax(b, False)  # Gọi đệ quy lượt của Min (Người)
                b[i] = ' '  # QUAY LUI (Backtrack) - Rút cờ lại
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf  # Khởi tạo điểm cao nhất có thể
        for i in range(9):
            if b[i] == ' ':
                b[i] = HUMAN  # Đánh thử
                score = minimax(b, True)  # Gọi đệ quy lượt của Max (AI)
                b[i] = ' '  # QUAY LUI (Backtrack) - Rút cờ lại
                best_score = min(score, best_score)
        return best_score


def get_best_move(b):
    """AI tìm nước đi tốt nhất hiện tại"""
    best_score = -math.inf
    best_move = -1
    for i in range(9):
        if b[i] == ' ':
            b[i] = AI  # AI đánh thử
            # Chấm điểm nước đi này bằng cách cho Minimax mô phỏng phần còn lại của ván cờ
            score = minimax(b, False)
            b[i] = ' '  # Quay lui
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


# --- VÒNG LẶP TRÒ CHƠI ---
print("Chào mừng đến với Caro 3x3!")
print("Các ô được đánh số từ 0 đến 8 như sau:")
print(" 0 | 1 | 2 \n---+---+---\n 3 | 4 | 5 \n---+---+---\n 6 | 7 | 8 ")
print("Bạn là 'O', AI là 'X'. Bạn đi trước!")

while True:
    # Lượt của người chơi
    while True:
        try:
            move = int(input("Chọn ô bạn muốn đánh (0-8): "))
            if board[move] == ' ':
                board[move] = HUMAN
                break
            else:
                print("Ô này đã có người đánh! Chọn lại.")
        except (ValueError, IndexError):
            print("Vui lòng nhập số hợp lệ từ 0 đến 8.")

    print_board(board)

    # Kiểm tra kết thúc trò chơi
    result = check_winner(board)
    if result: break

    # Lượt của AI
    print("AI đang suy nghĩ...")
    ai_move = get_best_move(board)
    board[ai_move] = AI
    print(f"AI đã đánh vào ô {ai_move}:")
    print_board(board)

    # Kiểm tra kết thúc trò chơi
    result = check_winner(board)
    if result: break

# Thông báo kết quả
if result == 'Tie':
    print("Hòa rồi! Bạn chơi rất tốt.")
else:
    print(f"Người chiến thắng là: {result}! (AI không bao giờ thua đâu)")