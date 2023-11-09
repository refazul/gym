# https://gymnasium.farama.org/content/migration-guide/

import gymnasium as gym
from tqdm import tqdm

from blackjack_tutorial import BlackjackAgent

#env = gym.make("LunarLander-v2", render_mode="human")
env = gym.make('Blackjack-v1', natural=False, sab=False, render_mode="human")
observation, info = env.reset(seed=123, options={})

learning_rate = 0.01
n_episodes = 100
start_epsilon = 1.0
epsilon_decay = start_epsilon / (n_episodes / 2)  # reduce the exploration over time
final_epsilon = 0.1

agent = BlackjackAgent(
    learning_rate=learning_rate,
    initial_epsilon=start_epsilon,
    epsilon_decay=epsilon_decay,
    final_epsilon=final_epsilon,
)
env = gym.wrappers.RecordEpisodeStatistics(env, deque_size=n_episodes)
for episode in tqdm(range(n_episodes)):
    obs, info = env.reset()
    done = False
    while not done:
        #action = env.action_space.sample()  # agent policy that uses the observation and info
        action = agent.get_action(obs)
        next_obs, reward, terminated, truncated, info = env.step(action)

        agent.update(obs, action, reward, terminated, next_obs)
        obs = next_obs

        done = terminated or truncated
    agent.decay_epsilon()
env.close()