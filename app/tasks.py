from typing import Dict, Any, List
from pydantic import BaseModel

class TaskDefinition(BaseModel):
    id: str
    name: str
    description: str
    difficulty: str
    input_data: Any
    expected_output: Any

TASKS: List[TaskDefinition] = [
    TaskDefinition(
        id="email_triage",
        name="Email Triage",
        description="Categorize the given email text into 'Work', 'Spam', or 'Updates'.",
        difficulty="Easy",
        input_data="Subject: Urgent: Q3 Project Review\n\nHi Team, please find the attached slides for the Q3 review meeting scheduled for tomorrow at 10 AM. Best, Sarah.",
        expected_output="Work"
    ),
    TaskDefinition(
        id="data_cleaning",
        name="Data Cleaning",
        description="Clean the messy JSON data. Requirements: Proper casing for names, trim spaces, lowercase emails, and integer age.",
        difficulty="Medium",
        input_data='{"name": "  jOhn dOE  ", "email": "John@EXAMPLE.com", "age": "25.5 "}',
        expected_output={"name": "John Doe", "email": "john@example.com", "age": 25}
    ),
    TaskDefinition(
        id="code_review",
        name="Code Review",
        description="Review the buggy JavaScript code and list issues. Detect: assignment (=) instead of comparison (==), missing semicolons, and basic syntax issues.",
        difficulty="Hard",
        input_data="""function checkStatus(value) {
    if (value = "active")
        console.log("Status is active")
    else
        console.log("Inactive")
    return value
}""",
        expected_output=[
            "Assignment '=' used inside 'if' condition instead of comparison '=='.",
            "Missing semicolon after console.log statement.",
            "Missing semicolon after return statement."
        ]
    )
]

def get_task_by_id(task_id: str) -> TaskDefinition:
    for task in TASKS:
        if task.id == task_id:
            return task
    raise ValueError(f"Task {task_id} not found")
