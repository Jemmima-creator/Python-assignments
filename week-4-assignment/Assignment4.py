

def main():
    filename = input("Enter the filename you want to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Create a new output filename
        output_file = "modified_" + filename

        # Write modified content to new file
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print("Success! Modified content saved in", output_file)

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()
