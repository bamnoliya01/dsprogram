def merge_waitlists(app_list, counter_list):
    """
    Merges two sorted waitlists into a single sorted waitlist in one pass.
    """
    merged_list = []
    i = 0  # Pointer for app_list
    j = 0  # Pointer for counter_list

    # Compare elements from both lists and pick the smaller one
    while i < len(app_list) and j < len(counter_list):
        if app_list[i] <= counter_list[j]:
            merged_list.append(app_list[i])
            i += 1
        else:
            merged_list.append(counter_list[j])
            j += 1

    # Append remaining elements from app_list, if any
    while i < len(app_list):
        merged_list.append(app_list[i])
        i += 1

    # Append remaining elements from counter_list, if any
    while j < len(counter_list):
        merged_list.append(counter_list[j])
        j += 1

    return merged_list

# Example Usage (Both lists must be sorted)
mobile_app_waitlist = [2, 5, 9, 14]
railway_counter_waitlist = [1, 6, 8, 12, 15]

print("\n--- 3. IRCTC Waitlist Merger ---")
final_waitlist = merge_waitlists(mobile_app_waitlist, railway_counter_waitlist)
print("Unified Sorted Waitlist:", final_waitlist)
