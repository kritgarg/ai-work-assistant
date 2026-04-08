import http.server
import socketserver
import threading
import time
from app.env import WorkEnv, Action

def run_health_check_server():
    """Starts a simple health check server on port 7860 to keep HF Space alive."""
    PORT = 7860
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Health check server running on port {PORT}")
        httpd.serve_forever()

def main():
    print("--- OpenEnv AI Workplace Automation ---")
    env = WorkEnv()
    obs = env.reset()
    
    print(f"Initial Observation: {obs.task_id}")
    print(f"Instruction: {obs.instruction}")
    
    # Simple manual run for smoke testing on startup
    print("\nRunning startup environment check...")
    action = Action(task_id=obs.task_id, output="Work")
    obs, reward, done, info = env.step(action)
    print(f"Task 1 Result: Reward={reward}, Done={done}")

    if not done:
        print(f"\nNext Observation: {obs.task_id}")
        print(f"Instruction: {obs.instruction}")
    
    print("\nEnvironment check complete. Starting persistent health-check server...")
    
    # Start health check server in a thread or as the main process
    run_health_check_server()

if __name__ == "__main__":
    main()
