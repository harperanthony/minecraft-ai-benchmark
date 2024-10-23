# Minecraft AI Benchmark

This repository contains a setup for running MineRL tasks in a headless environment.

## Setup Instructions

1. Clone this repository:
git clone https://github.com/olafhappy/minecraft-ai-benchmark.git cd minecraft-ai-benchmark

2. Run the setup script:
chmod +x setup.sh ./setup.sh


3. Run the MineRL task:
python3 run_task.py

## Notes

- The environment runs in headless mode using Xvfb.
- Frame skip is set to 4 in the `run_task.py` script.
- If you encounter any issues, please check the MineRL documentation or open an issue in this repository.


# Research on MineRL: Action Space and Observable Space

## Overview of MineRL

MineRL is a research environmentdesigned for developing AI agents in the Minecraft game. It provides a platform for training and evaluating agents on various tasks, leveraging the righ, interactive world of Minecraft.

## Action Space

The action space in MineRL consists of a variety of actions that an agent can perform within the game. These actions can be categorized into:

### 1. Movement Actions:

- **Walk**: Move forward, backword, left or right.
- **Jump**: Leap upward.
- **Sprint**: Move faster than normal walking speed.

### 2. Interaction Actions:

- **Use Item**: Use an item from the inventory.
- **Attack**: Damage a target entity.
- **Place Block**: Place a block in the world.

### 3. Inventory Actions:

- **Pick Up Item**: Collect items from the environment.
- **Craft Item**: Combine items to create new ones.

These actions allow agents to navigate the environment, interact with objects, and perform tasks suchas gathering resources or building structures.

## Observable 

Thhe observable space consists of the information that the agent can perceive from the environment, which is crucial for decision making. Examples of observable elements include:

### 1. Agent's State:

- **Position**: The current coordinates of the agent in the world.
- **Health**: The health points of the agent.

### 2. Environment State:

- **Nearby Entities**: Information about nearby entities, such as mobs, players and animals.
- **Block Types**: The types of blocks in the agent's vicinity(for example, dirt, stone, wood)

### 3. Inventory State:

- **Items Held**: A list of itmes currently in the agent's inventory.
- **Crafting Recipes**: Available recipes based on the items in the inventory

### Examples of Observable Space

- **Position**: An agent at coordinats (s: 100, y: 64, z: -200) can perceive its surroundings.
- **Nearby Entities**: The agent can see a cow and a zombie within a radius of 10 blocks.
- **Inventory**: The agent holds 5 apples and 2 wooden planks, allowing it to decide whether to eat or craft.

## Conclusion

Understanding the action and observable spaces in MineRL is essential for developing effective AI agents. By leveraging this knowledge, we can create agents that perform complex tasks and interact intelligently with the Minecraft world.


  
