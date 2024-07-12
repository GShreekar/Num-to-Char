def unicode_to_character():
    while True:
        user_input = input("Enter a Unicode number (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        try:
            unicode_num = int(user_input)
            if unicode_num < 0 or unicode_num > 0x10FFFF:
                raise ValueError("Unicode number must be in the range [0, 1114111].")
            unicode_char = chr(unicode_num)
            if not unicode_char.isprintable():
                raise ValueError("Unicode number does not represent a printable character.")
            print(f"Unicode character for the number {unicode_num} is: {unicode_char}")
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid Unicode number or 'exit' to quit.")
        except OverflowError:
            print("Error: Unicode number is too large. Please enter a valid Unicode number or 'exit' to quit.")
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")

if __name__ == "__main__":
    unicode_to_character()
