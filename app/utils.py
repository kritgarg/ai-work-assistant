import json
import re

def clean_json_string(s: str) -> str:
    """Helper to extract JSON from model output if it's wrapped in markers."""
    match = re.search(r'\{.*\}', s, re.DOTALL)
    if match:
        return match.group(0)
    return s

def parse_json_safely(s: str):
    """Safely parse JSON string."""
    try:
        return json.loads(clean_json_string(s))
    except (json.JSONDecodeError, AttributeError):
        return None
