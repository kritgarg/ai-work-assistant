from typing import Tuple, Optional, Any, List, Dict
from pydantic import BaseModel
from .tasks import TASKS, get_task_by_id, TaskDefinition
from .graders import get_task_score
from .rewards import calculate_reward

class Action(BaseModel):
    task_id: str
    output: str

class Observation(BaseModel):
    task_id: str
    instruction: str
    data: Any

class Reward(BaseModel):
    value: float
    info: Dict[str, Any]

class WorkEnv:
    def __init__(self):
        self.current_task_idx = 0
        self.action_history = []
        self.done = False

    def reset(self) -> Observation:
        """Resets the environment and returns the first task."""
        self.current_task_idx = 0
        self.action_history = []
        self.done = False
        return self._get_observation()

    def _get_observation(self) -> Observation:
        task = TASKS[self.current_task_idx]
        return Observation(
            task_id=task.id,
            instruction=task.description,
            data=task.input_data
        )

    def step(self, action: Action) -> Tuple[Observation, float, bool, Dict[str, Any]]:
        """
        Processes an action and returns (observation, reward, done, info).
        """
        if self.done:
            raise Exception("Environment is already done. Call reset().")

        task = get_task_by_id(action.task_id)
        
        # Grade the output
        score = get_task_score(task.id, action.output, task.expected_output)
        
        # Calculate reward
        self.action_history.append(action.output)
        reward_val = calculate_reward(score, self.action_history)
        
        # Info dictionary
        info = {
            "task_id": task.id,
            "score": score,
            "raw_output": action.output
        }

        # Progress to next task if score is high enough or after 1 attempt
        self.current_task_idx += 1
        if self.current_task_idx >= len(TASKS):
            self.done = True
            obs = Observation(task_id="finish", instruction="All tasks completed", data=None)
        else:
            obs = self._get_observation()

        return obs, reward_val, self.done, info

    def state(self) -> Dict[str, Any]:
        """Returns current environment state."""
        return {
            "current_task_idx": self.current_task_idx,
            "done": self.done,
            "tasks_total": len(TASKS)
        }
