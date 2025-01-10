import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# パラメータの設定
state_space = 21  # 数値線上の範囲（-10～10）
action_space = [-1, 1]  # 行動（左、右）
q_table = np.zeros((state_space, len(action_space)))  # Qテーブルの初期化
alpha = 0.1  # 学習率
gamma = 1.0  # 割引率
epsilon = 0.1  # ε-greedyの確率
episodes = 100  # エピソード数
goal_state = 10  # ゴールの位置

# 状態をインデックスに変換
def state_to_index(state):
    return state + (state_space // 2)

# 環境のステップ関数
def step(state, action):
    next_state = state + action
    reward = -3  # ペナルティ
    done = False
    if next_state == goal_state:
        reward = 10  # ゴールの報酬
        done = True
    elif next_state < -10 or next_state > 10:
        reward = -10  # 範囲外のペナルティ
        next_state = state  # 範囲外なら元の位置に戻る
    return next_state, reward, done

# エージェントの動きを記録するリスト
agent_positions = []

# 学習プロセス
for episode in range(episodes):
    state = 0  # 初期状態
    done = False
    episode_positions = [state]  # エピソードごとの動き
    while not done:
        # ε-greedyポリシー
        if random.uniform(0, 1) < epsilon:
            action = random.choice(action_space)
        else:
            action = action_space[np.argmax(q_table[state_to_index(state)])]

        # 環境とやり取り
        next_state, reward, done = step(state, action)

        # Q値の更新
        action_index = action_space.index(action)
        best_next_action = np.max(q_table[state_to_index(next_state)])
        q_table[state_to_index(state), action_index] += alpha * (
            reward + gamma * best_next_action - q_table[state_to_index(state), action_index]
        )

        # 状態を更新
        state = next_state
        episode_positions.append(state)
    agent_positions.append(episode_positions)

# アニメーションの作成
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-1, 1)
ax.axhline(0, color="black", linewidth=0.5)  # 数値線
ax.scatter(goal_state, 0, color="green", label="Goal", s=100)  # ゴール
agent_dot, = ax.plot([], [], "ro", label="Agent")  # エージェント
ax.legend()

def init():
    agent_dot.set_data([], [])
    return agent_dot,

def update(frame):
    x = frame  # エージェントの位置
    agent_dot.set_data(x, 0)  # 数値線上のエージェント
    return agent_dot,

# エージェントの全エピソードの動きをつなげる
flattened_positions = [pos for episode in agent_positions for pos in episode]

ani = FuncAnimation(
    fig, update, frames=flattened_positions, init_func=init, blit=True, interval=200
)

# 動画ファイルとして保存（MP4形式）
ani.save("path/aaa.mp4", writer="ffmpeg", fps=30)

plt.show()
