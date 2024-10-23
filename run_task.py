import minerl
import gym
import numpy as np

# Create the MineRL environment
env = gym.make('MineRLNavigateDense-v0')

# Reset the environment
obs = env.reset()

# Set frame skip
frame_skip = 4

done = False
total_reward = 0
step_count = 0

while not done:
    # Take a random action
    action = env.action_space.sample()
    
    # Apply frame skip
    for _ in range(frame_skip):
        obs, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            break
    
    step_count += 1
    if step_count % 100 == 0:
        print(f"Step: {step_count}, Total Reward: {total_reward}")

print(f"Episode finished. Total Reward: {total_reward}")
env.close()
