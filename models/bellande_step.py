import numpy as np


class LocalPredictionModel:
    """Simplified local version of the prediction model"""

    def __init__(self, model_path="bellande_step_model.h5", state_space=10):
        self.model_path = model_path
        self.state_space = state_space
        self.num_actions = 3

        # Initialize mock model weights for demonstration
        # In production, you would load actual model weights
        self.model_weights = self._initialize_mock_weights()

    def _initialize_mock_weights(self):
        """Initialize random weights to simulate a trained model"""
        return {
            "layer1": np.random.randn(self.state_space, 64) * 0.1,
            "layer2": np.random.randn(64, 32) * 0.1,
            "output": np.random.randn(32, self.num_actions) * 0.1,
        }

    def predict(self, state):
        """
        Predict Q-values for given state
        Returns: array of Q-values for each action
        """
        # Ensure state is 2D: (batch_size, state_space)
        if state.ndim == 1:
            state = state.reshape(1, -1)

        # Simple feedforward prediction (mock DQN)
        x = state
        x = np.tanh(x @ self.model_weights["layer1"])  # Hidden layer 1
        x = np.tanh(x @ self.model_weights["layer2"])  # Hidden layer 2
        q_values = x @ self.model_weights["output"]  # Output layer

        return q_values

    def get_q_values(self, state):
        """Get the best action based on Q-values"""
        q_values = self.predict(state)
        return np.argmax(q_values[0])

    def reset(self):
        """Reset environment to initial state"""
        return np.random.randn(self.state_space)

    def step(self, action):
        """
        Take a step in the environment
        Returns: (reward, next_state, done)
        """
        # Mock environment step
        reward = np.random.randn()
        next_state = np.random.randn(self.state_space)
        done = False
        return reward, next_state, done

    def predict_action_state(self, state):
        """
        Predict next action and state
        Returns: (next_state, action)
        """
        # Uncomment to use model predictions instead of random
        # action = self.get_q_values(state)
        action = np.random.randint(0, self.num_actions)
        _, next_state, _ = self.step(action)
        return next_state, action


class DisplayActionsState(LocalPredictionModel):
    """Display actions and states for visualization"""

    def __init__(self, state_space=10, num_steps=10):
        super().__init__(state_space=state_space)
        self.num_steps = num_steps
        self.starting_state = self.reset()
        self.run_demonstration()

    def run_demonstration(self):
        """Run and print predictions for demonstration"""
        state = self.starting_state

        print("=" * 80)
        print("Running Prediction Demonstration")
        print("=" * 80)

        for i in range(self.num_steps):
            # Get predictions
            state_reshaped = state.reshape(-1, *state.shape)
            q_values = self.predict(state_reshaped)[0]

            # Get next state and action
            next_state, action = self.predict_action_state(state)

            # Display results
            print(f"\nStep {i + 1}:")
            print(f"  Q-values: {q_values}")
            print(f"  Action: {action}")
            print(f"  Next State: {next_state[:5]}...")  # Show first 5 values

            # Update state for next iteration
            state = next_state

        print("\n" + "=" * 80)


# Example usage
if __name__ == "__main__":
    # Create and run the display system
    display_system = DisplayActionsState(state_space=10, num_steps=10)
