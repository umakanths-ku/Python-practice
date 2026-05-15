def validate_key(product_key):
    # YOUR TASK: Write a single-line ternary operator.
    # It must check TWO things using 'and':
    # 1. Is the character at index 0 equal to "A"? (product_key[0] == "A")
    # 2. Is the whole key alphanumeric? (product_key.isalnum())
    
    result = "Valid" if product_key.isalnum()== True and product_key[0] == "A" else "Invalid"
    
    return result

# --- TEST CASES ---
print(validate_key("A123B"))  # Starts with A, no symbols -> Should print: Valid
print(validate_key("B123A"))  # No symbols, but doesn't start with A -> Should print: Invalid
print(validate_key("A12#B"))  # Starts with A, but contains a '#' symbol -> Should print: Invalid