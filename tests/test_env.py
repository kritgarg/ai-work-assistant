import unittest
from app.env import WorkEnv, Action
from app.tasks import TASKS

class TestWorkEnv(unittest.TestCase):
    def setUp(self):
        self.env = WorkEnv()

    def test_reset(self):
        obs = self.env.reset()
        self.assertEqual(obs.task_id, "email_triage")
        self.assertFalse(self.env.done)

    def test_step_email_triage_correct(self):
        self.env.reset()
        action = Action(task_id="email_triage", output="Work")
        obs, reward, done, info = self.env.step(action)
        self.assertEqual(reward, 1.0)
        self.assertEqual(info["score"], 1.0)
        self.assertEqual(obs.task_id, "data_cleaning")

    def test_step_email_triage_incorrect(self):
        self.env.reset()
        action = Action(task_id="email_triage", output="Spam") # Expected Work
        obs, reward, done, info = self.env.step(action)
        self.assertEqual(reward, -0.2)
        self.assertEqual(info["score"], 0.0)

    def test_full_episode(self):
        obs = self.env.reset()
        # Step through all 3 tasks
        for _ in range(3):
            action = Action(task_id=obs.task_id, output="some output")
            obs, reward, done, info = self.env.step(action)
        
        self.assertTrue(done)
        self.assertTrue(self.env.done)

if __name__ == "__main__":
    unittest.main()
