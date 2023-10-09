def unicode_to_character():
    while True:
        user_input = input("Enter a Unicode number (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break

        try:
            unicode_num = int(user_input)

            unicode_char = chr(unicode_num)

            print(f"Unicode character for the number {unicode_num} is: {unicode_char}")
        except ValueError:
            print("Invalid input. Please enter a valid Unicode number or 'exit' to quit.")

if __name__ == "__main__":
    unicode_to_character()
