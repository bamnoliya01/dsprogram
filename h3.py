class GPSNavigation:
    def __init__(self):
        self.current_place = None
        self.back_stack = []
        self.forward_stack = []

    # 1. visit(place) -> Move to a new place
    def visit(self, place):
        if self.current_place:
            self.back_stack.append(self.current_place)
        self.current_place = place
        self.forward_stack.clear()  # New visit clears the forward history
        print(f"Visited: {self.current_place}")

    # 2. back() -> Go to the previous place
    def back(self):
        if not self.back_stack:
            print("No previous checkpoint to go back to!")
            return

        self.forward_stack.append(self.current_place)
        self.current_place = self.back_stack.pop()
        print(f"Went Back -> Current Position: {self.current_place}")

    # 3. forward() -> Go forward if available
    def forward(self):
        if not self.forward_stack:
            print("No forward path available!")
            return

        self.back_stack.append(self.current_place)
        self.current_place = self.forward_stack.pop()
        print(f"Went Forward -> Current Position: {self.current_place}")


# --- Testing the implementation ---
gps = GPSNavigation()
gps.visit("Checkpoint 1")
gps.visit("Checkpoint 2")
gps.visit("Wrong Turn Checkpoint 3")

gps.back()     # Takes you back to Checkpoint 2
gps.forward()  # Changes mind, takes you forward to Wrong Turn Checkpoint 3 again
