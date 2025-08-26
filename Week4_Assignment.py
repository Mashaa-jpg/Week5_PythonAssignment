#
# File Read, Write, and Error Handling Program
#
# This program demonstrates:
# 1. Reading content from a specified input file.
# 2. Modifying the content (in this case, converting it to uppercase).
# 3. Writing the modified content to a new output file.
# 4. Implementing robust error handling for common issues like `FileNotFoundError`.
#

# Define a function to encapsulate the main logic. This makes the code reusable and clean.
def process_file_with_error_handling():
    """
    Reads a file, modifies its content, and writes the result to a new file.
    Includes a try-except block to handle file-related errors.
    """
    input_filename = input("Please enter the name of the input file: ")
    output_filename = "modified_output.txt"

    try:
        # Step 1: Read the content from the input file using a 'with' statement.
        # The 'with' statement automatically closes the file, even if errors occur.
        with open(input_filename, 'r') as file:
            original_content = file.read()
        
        print(f"\nSuccessfully read content from '{input_filename}'.")
        print("-" * 30)
        print("Original Content:")
        print(original_content)
        print("-" * 30)

        # Step 2: Modify the content. Here, we convert all text to uppercase.
        modified_content = original_content.upper()
        
        # We also add a header and footer to the modified content for clarity.
        final_content = (
            "*** MODIFIED CONTENT (TO UPPERCASE) ***\n\n"
            f"{modified_content}\n\n"
            "****************************************\n"
        )
        
        # Step 3: Write the modified content to the new output file.
        with open(output_filename, 'w') as file:
            file.write(final_content)
            
        print(f"Successfully wrote modified content to '{output_filename}'.")
        print("Program finished successfully.")

    except FileNotFoundError:
        # Step 4: Handle the error if the user-specified file doesn't exist.
        print(f"\nError: The file '{input_filename}' was not found.")
        print("Please check the filename and try again.")
    
    except Exception as e:
        # Catch any other potential errors that might occur.
        print(f"\nAn unexpected error occurred: {e}")

# Call the function to run the program.
if __name__ == "__main__":
    process_file_with_error_handling()

