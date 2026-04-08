from app.env import WorkEnv, Action
import json

def main():
    print("--- OpenEnv AI Workplace Automation ---")
    env = WorkEnv()
    obs = env.reset()
    
    print(f"Initial Observation: {obs.task_id}")
    print(f"Instruction: {obs.instruction}")
    
    # Simple manual run for demonstration
    # In practice, inference.py will drive this.
    print("\nRunning basic environment check...")
    
    # Task 1
    action = Action(task_id=obs.task_id, output="Work")
    obs, reward, done, info = env.step(action)
    print(f"Task 1 Result: Reward={reward}, Done={done}")

    if not done:
        print(f"\nNext Observation: {obs.task_id}")
        print(f"Instruction: {obs.instruction}")

if __name__ == "__main__":
    main()
