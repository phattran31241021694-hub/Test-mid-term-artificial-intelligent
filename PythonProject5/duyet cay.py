#cai dat thu cong
#tim kiem theo chieu rong(BFS)

#tim kiem voi chi phi cuc tieu(UCS)
#tim kiem theo chieu sau(DFS)
#tim kiem gioi han do sau(DLS)
#tim kiem sau dan(IDS)
#giai voi bai toan puzzle 8
from simpleai.search import (
        SearchProblem,
        breadth_first,
        depth_first,
        astar,
    )
GOAL= ((1,2,3),(4,5,6),(7,8,0))
class Puzzle8(SearchProblem):
    def __init__(self, initial_state, heuristic_func=None):
        # Hàm khởi tạo nhận thêm tham số heuristic_func để linh hoạt thay đổi h1, h2
        super().__init__(initial_state=initial_state)
        self.my_heuristic = heuristic_func
    def actions(self, state):
        actions = []
        line, col = self.find_zero(state)
        if line > 0: actions.append("Up")
        if line < 2: actions.append("Down")
        if col > 0: actions.append("Left")
        if col < 2: actions.append("Right")
        return actions
    def result(self, state, action):
        line, col = self.find_zero(state)
        new_state = [list(row) for row in state]
        x, y = 0, 0
        if action == "Up":
            x, y = line - 1, col
        elif action == "Down":
            x, y = line + 1, col
        elif action == "Left":
            x, y = line, col - 1
        elif action == "Right":
            x, y = line, col + 1
        new_state[line][col], new_state[x][y] = new_state[x][y], new_state[line][col]
        return tuple(tuple(row) for row in new_state)

    def is_goal(self, state):
        return state == GOAL
    def heuristic(self,state):
        if self.my_heuristic:
            return self.my_heuristic(state)
        return 0
    def find_zero(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
def h1(state):
    count=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=0 and state[i][j]!=GOAL[i][j]:
                count+=1
    return count
def h2(state):
    dis=0
    goal_pos = {}
    for i in range(3):
        for j in range(3):
            goal_pos[GOAL[i][j]] = (i, j)
    for i in range(3):
        for j in range(3):
            obj=state[i][j]
            x,y=goal_pos[obj]
            dis+=abs(x-i)+abs(y-j)
    return dis
problem_8=((1,2,3),(4,5,6),(0,7,8))
prob=Puzzle8(initial_state=problem_8)
prob_h1=Puzzle8(initial_state=problem_8,heuristic_func=h1)
result_h1=astar(prob_h1)
prob_h2=Puzzle8(initial_state=problem_8,heuristic_func=h2)
result_h2=astar(prob_h2)
print("Heu_1:", result_h1.path())
print("Heu_2:", result_h2.path())
