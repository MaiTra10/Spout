import time

class MockSprinkler:
    def __init__(self, sprinkler_type):
        self.sprinkler_type = sprinkler_type
        self.is_on = False
        self.run_time = 0  # Default run time is set to 0 minutes
        self.start_time = None

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            self.start_time = time.time()
            print(f"{self.sprinkler_type} Sprinkler Status: ON")
        else:
            print(f"{self.sprinkler_type} Sprinkler is already ON!")

    def turn_off(self):
        if self.is_on:
            elapsed_time = round(time.time() - self.start_time)  # Calculate elapsed time in seconds
            self.is_on = False
            self.run_time += elapsed_time // 60  # Convert elapsed time to minutes and add to total run time
            self.start_time = None
            print(f"{self.sprinkler_type} Sprinkler Status: OFF")
        else:
            print(f"{self.sprinkler_type} Sprinkler is already OFF!")

    def set_run_time(self, minutes):
        if minutes < 0:
            print("Run time must be a non-negative value.")
        else:
            self.run_time = minutes

    def get_run_time(self):
        return f"Run time for {self.sprinkler_type} sprinkler is set to {self.run_time} minutes."

    def status(self):
        if self.is_on:
            elapsed_time = round(time.time() - self.start_time)
            return f"{self.sprinkler_type} sprinkler is ON. Elapsed time: {elapsed_time} seconds."
        else:
            return f"{self.sprinkler_type} sprinkler is OFF."

# Example usage:
""" if __name__ == "__main__":
    grass_sprinkler = MockSprinkler("Grass")

    print(grass_sprinkler.status())
    grass_sprinkler.turn_on()
    grass_sprinkler.set_run_time(0.5)  # Set run time to 30sec
    print(grass_sprinkler.get_run_time())
    time.sleep(30)  # Simulate 30 seconds of run time
    print(grass_sprinkler.status())
    grass_sprinkler.turn_off()
    print(grass_sprinkler.get_run_time()) """