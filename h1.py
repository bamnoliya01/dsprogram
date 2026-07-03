class ConveyorBelt:
    def __init__(self):
        # Initialize a fixed conveyor belt with exactly 8 slots (0-7)
        self.slots = [None] * 8

    # 1. Check what's at a specific slot
    def check_slot(self, slot_num):
        if 0 <= slot_num < 8:
            return self.slots[slot_num]
        return "Invalid slot number!"

    # 2. Find a product on the belt
    def find_product(self, product_name):
        for i in range(8):
            if self.slots[i] == product_name:
                return f"Product '{product_name}' found at slot {i}."
        return f"Product '{product_name}' not found on the conveyor belt."

    # 3. Update a specific slot with a product
    def update_slot(self, slot_num, product_name):
        if 0 <= slot_num < 8:
            self.slots[slot_num] = product_name
            print(f"Slot {slot_num} updated with: {product_name}")
        else:
            print("Invalid slot number!")

    # 4. Check if the belt is full (no empty slots)
    def is_full(self):
        return None not in self.slots


# --- Testing the implementation ---
amazon_belt = ConveyorBelt()
amazon_belt.update_slot(2, "Smartphone")
amazon_belt.update_slot(5, "Headphones")

print("At slot 2:", amazon_belt.check_slot(2))
print(amazon_belt.find_product("Headphones"))
print("Is the conveyor belt full?", amazon_belt.is_full())
