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

