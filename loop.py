def process_packet(packet):
    # STEP 1: Get the middle 4 characters. 
    # Because the packet is exactly 10 characters long, 
    # you want to start at index 3 and stop at index 7.
    
    
    # STEP 2: YOUR TASK
    # Reverse 'middle_chunk' using a negative slicing step.
    reversed_chunk = packet[6:2:-1]
    
    return reversed_chunk

# --- TEST CASES ---
# Total length is 10. Middle 4 characters are "GOLD"
print(process_packet("abcGOLDxyz"))  
# Expected Output: DLOG (GOLD spelled backward)

# Total length is 10. Middle 4 characters are "9876"
print(process_packet("1239876000"))  
# Expected Output: 6789 (9876 spelled backward)