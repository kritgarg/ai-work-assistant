---
title: AI Work Assistant Env
emoji: 💼
colorFrom: indigo
colorTo: blue
sdk: docker
pinned: false
---

# AI Work Assistant Environment (AI-Work-Assistant-Env)

## 🎯 Project Overview
This project provides a simulation environment for evaluating AI agents on common workplace automation tasks. It follows the OpenEnv standard, enabling standardized evaluation of LLMs on their ability to perform structured tasks like email triaging, data cleaning, and code reviews.

### Real-world Motivation
In a modern workspace, AI agents are increasingly tasked with handling repetitive operations. This environment simulates these interactions, providing a sandbox where agents can be tested for accuracy, reliability, and their ability to follow complex instructions while managing environment state.

---

## 🛠 Tasks

### 1. Email Triage (Easy)
*   **Input**: A raw email text.
*   **Goal**: Categorize as "Work", "Spam", or "Updates".
*   **Success Criteria**: Exact match with the ground truth category.

### 2. Data Cleaning (Medium)
*   **Input**: Messy JSON string containing user details (name, email, age).
*   **Goal**: Return a cleaned JSON array with proper casing, trimmed whitespace, lowercase emails, and integer ages.
*   **Success Criteria**: Correctness of individual fields (Partial scoring supported).

### 3. Code Review (Hard)
*   **Input**: A JavaScript function snippet with intentional bugs (e.g., `=` vs `==`).
*   **Goal**: Identify and list the specific issues in the code.
*   **Success Criteria**: Detection of key logical and syntax errors (Partial scoring supported).

---

## 📊 Environment Schema

### Observation
```python
{
  "task_id": "string",
  "instruction": "string",
  "data": "any"
}
```

### Action
```python
{
  "task_id": "string",
  "output": "string"
}
```

### Reward Function
The environment provides continuous feedback based on agent performance:
*   **Correct (+1.0)**: Output matches expected criteria perfectly.
*   **Partial (Proportional)**: For multi-field tasks, rewards are scaled by the percentage of correct segments.
*   **Wrong (-0.2)**: Penalty for incorrect or nonsensical outputs.
*   **Repetition Penalty (-0.1)**: Penalizes agents that fall into "repetition loops" by providing the same incorrect answer multiple times.

---

## 🚀 Setup & Usage

### Local Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Set your Hugging Face token:
   ```bash
   export HF_TOKEN="your_token_here"
   ```

### Running with Docker
Build and run the environment check:
```bash
docker build -t ai-work-env .
docker run ai-work-env
```

### Running Inference
The `inference.py` script drives the evaluation using the Hugging Face Router:
```bash
python inference.py
```

---

## 📝 Example Output (Log Format)
```text
[START] task=all_tasks env=work-env model=meta-llama/Meta-Llama-3-8B-Instruct
[STEP] step=1 action="Work" reward=1.0 done=false
[STEP] step=2 action='[{"name": "John Doe", "email": "john@example.com", "age": 25}, ...]' reward=1.0 done=false
[STEP] step=3 action="The code uses '=' instead of '==' in the if statement. Missing semicolons..." reward=1.0 done=true
[END] success=true steps=3 score=1.0 rewards=[1.0, 1.0, 1.0]
```

---

**Developed for OpenEnv Hackathon 2024**
