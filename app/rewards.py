def calculate_reward(score: float, action_history: list) -> float:
    """
    Reward Logic:
    - Correct: +1.0 (if score is 1.0)
    - Partial: proportional score (e.g. 0.5 score -> 0.5 reward)
    - Wrong: -0.2 (if score is 0.0)
    - Repeated wrong actions: additional penalty
    """
    if score == 1.0:
        reward = 1.0
    elif score > 0:
        reward = score
    else:
        reward = -0.2
        
    # Check for repeated wrong actions (simple heuristic: if same action appears before)
    if len(action_history) > 1:
        current_action = action_history[-1]
        for past_action in action_history[:-1]:
            if current_action == past_action:
                reward -= 0.1 # Penalty for repeating the same action
                break
                
    return round(reward, 2)
