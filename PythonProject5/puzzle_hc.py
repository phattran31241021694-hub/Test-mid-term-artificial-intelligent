
from simpleai.search import (
        SearchProblem,
        hill_climbing,
hill_climbing_random_restarts
    )
GOAL= ((1,2,3),(4,5,6),(7,8,0))
class Puzzle8_hc(SearchProblem):
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

    def value(self, state):
        dis = 0
        goal_pos = {}
        for i in range(3):
            for j in range(3):
                goal_pos[GOAL[i][j]] = (i, j)
        for i in range(3):
            for j in range(3):
                obj = state[i][j]
                x, y = goal_pos[obj]
                dis += abs(x - i) + abs(y - j)
        return -dis
    def find_zero(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
problem_8=((1,2,3),(4,5,6),(7,0,8))
problem_hc=Puzzle8_hc(initial_state=problem_8)
result_hc=hill_climbing(problem_hc)
print(f"State: {result_hc.path()},point:{result_hc.value}")
