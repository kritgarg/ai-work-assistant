import json
from .utils import parse_json_safely

def grade_email_triage(prediction: str, expected: str) -> float:
    """Simple exact match for category."""
    if prediction.strip().lower() == expected.lower():
        return 1.0
    return 0.0

def grade_data_cleaning(prediction: str, expected: any) -> float:
    """Grades JSON data cleaning. Handles both list and single object outputs."""
    pred = parse_json_safely(prediction)
    if not pred:
        return 0.0
    
    # Fix 4: If output is a list, take the first object
    if isinstance(pred, list) and len(pred) > 0:
        pred = pred[0]
    
    # Handle case where expected might be a list too
    if isinstance(expected, list) and len(expected) > 0:
        expected = expected[0]

    correct_fields = 0
    total_fields = 3 # name, email, age
    
    for key in ["name", "email", "age"]:
        if key in pred and pred[key] == expected.get(key):
            correct_fields += 1
                
    return round(correct_fields / total_fields, 2)

def grade_code_review(prediction: str, expected_issues: list) -> float:
    """Grades code review based on finding the right issues."""
    prediction_lower = prediction.lower()
    found_count = 0
    
    # We check if the core concepts are mentioned in the prediction
    keywords = [
        ["assignment", "=", "comparison", "=="],
        ["semicolon", "missing"],
        ["semicolon", "return"]
    ]
    
    for issue_keywords in keywords:
        if all(kw in prediction_lower for kw in issue_keywords):
            found_count += 1
            
    return round(found_count / len(expected_issues), 2)

def get_task_score(task_id: str, prediction: str, expected: any) -> float:
    if task_id == "email_triage":
        return grade_email_triage(prediction, expected)
    elif task_id == "data_cleaning":
        return grade_data_cleaning(prediction, expected)
    elif task_id == "code_review":
        return grade_code_review(prediction, expected)
    return 0.0
