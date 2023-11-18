# Example vulnerable Python program
def vulnerable_function():
    data = [1, 2, 3]  # A simple list
    index = int(input("Enter an index: "))
    print(data[index])  # Potential index out of bounds error

vulnerable_function()
