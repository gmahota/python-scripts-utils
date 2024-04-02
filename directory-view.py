import os

# Directory you want to list
directory = r'C:\Users\YourName\Scripts'

# List of files in the directory
files = os.listdir(directory)

# Display the list of files
print("Files in the directory:")
for file in files:
    print(file)
