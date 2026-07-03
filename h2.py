class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    # Add a vehicle to the queue (Enqueue)
    def enqueue(self, vehicle):
        # Condition to check if the queue is full
        if (self.rear + 1) % self.capacity == self.front:
            print(f"Toll Plaza is FULL! Vehicle '{vehicle}' must wait.")
            return

        # If queue is completely empty
        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = vehicle
        print(f"Vehicle '{vehicle}' entered the toll plaza line.")

    # Remove a vehicle after they pay toll (Dequeue)
    def dequeue(self):
        # Condition to check if the queue is empty
        if self.front == -1:
            print("Toll Plaza is empty! No vehicles to process.")
            return None

        removed_vehicle = self.queue[self.front]
        
        # If there was only one vehicle left
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
            
        print(f"Vehicle '{removed_vehicle}' paid the toll and left.")
        return removed_vehicle


# --- Testing the implementation ---
toll_plaza = CircularQueue()
toll_plaza.enqueue("Car A")
toll_plaza.enqueue("SUV B")
toll_plaza.enqueue("Truck C")
toll_plaza.enqueue("Bike D")
toll_plaza.enqueue("Bus E")
toll_plaza.enqueue("Car F")  # Should show Full/Must wait

toll_plaza.dequeue()          # Car A leaves, creating an empty slot
toll_plaza.enqueue("Car F")  # Reuses the empty slot without wasting memory
