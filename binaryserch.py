def find_lower_bound_price(prices, target_price):
    """
    Finds the index of the first product price >= target_price using Binary Search.
    """
    low = 0
    high = len(prices) - 1
    ans = -1  # Default if no product matches the condition

    while low <= high:
        mid = (low + high) // 2
        
        if prices[mid] >= target_price:
            ans = mid       # Potential answer found, but look for a smaller index to the left
            high = mid - 1
        else:
            low = mid + 1   # Price is too low, move to the right half
            
    return ans

# Example Usage (Sorted prices of laptops)
laptop_prices = [35000, 42000, 48000, 50000, 55000, 62000, 75000]
target = 50000

print("\n--- 2. E-Commerce Price Filter ---")
index = find_lower_bound_price(laptop_prices, target)

if index != -1:
    print(f"First product matching ₹{target} or above is at index {index} with price: ₹{laptop_prices[index]}")
    print(f"Filtered products: {laptop_prices[index:]}")
else:
    print(f"No products found priced at ₹{target} or above.")
