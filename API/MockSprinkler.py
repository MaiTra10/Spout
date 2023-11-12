import time

class MockSprinkler:

    def __init__(self, sid, name, period, seed_type):

        self.sprinkler_id = sid
        self.sprinkler_name = name
        self.sprinkler_timer_mode = 'Manual'
        self.period = period
        self.seed_type = seed_type
        self.status = False
        self.previous_run_time = None
        self.previous_start_time = None

    def set_sprinkler_name(self, name):
        self.sprinkler_name = name

    def set_sprinkler_timer_mode(self, mode):
        self.sprinkler_timer_mode = mode

    def set_period(self, period):
        self.period = period

    def set_seed_type(self, seed_type):
        self.seed_type = seed_type

    def set_status(self, status):
        self.status = status

    def set_previous_run_time(self, run_time):
        self.previous_run_time = run_time

    def set_previous_start_time(self, start_time):
        self.previous_start_time = start_time

    def get_id(self):

        return self.sprinkler_id

    def get_name(self):

        return self.sprinkler_name
    
    def get_mode(self):

        return self.sprinkler_timer_mode
    
    def get_period(self):

        return self.period
    
    def get_seed_type(self):

        return self.seed_type
    
    def get_status(self):

        return self.status
    
    def get_previous_run(self):

        return self.previous_run_time
    
    def get_previous_start(self):

        return self.previous_start_time

"""     def turn_on(self):

        if not self.is_on:

            self.is_on = True
            self.start_time = time.time()
            return(f"{self.sprinkler_type} Sprinkler Status: ON")

        else:

            return(f"{self.sprinkler_type} Sprinkler is already ON!")

    def turn_off(self):

        if self.is_on:

            elapsed_time = round(time.time() - self.start_time)
            self.is_on = False
            self.run_time += elapsed_time // 60
            self.start_time = None

            return(f"{self.sprinkler_type} Sprinkler Status: OFF")

        else:

            return(f"{self.sprinkler_type} Sprinkler is already OFF!")

    def set_run_time(self, minutes):

        if minutes < 0:

            return("Run time must be a non-negative value.")

        else:

            self.run_time = minutes

    def get_run_time(self):

        return f"Run time for {self.sprinkler_type} sprinkler is set to {self.run_time} minutes."

    def status(self):

        if self.is_on:

            elapsed_time = round(time.time() - self.start_time)
            return f"{self.sprinkler_type} sprinkler is ON. Elapsed time: {elapsed_time} seconds."
        
        else:

            return f"{self.sprinkler_type} sprinkler is OFF." """

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