def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall? "))
            if num > 0:
                return num
        except ValueError:
            pass
        print("Please enter a valid number greater than 0.")

def sing(starting_bottles):
    i = starting_bottles
    keep_singing = True
    while keep_singing:
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottle{'s' if i-1 > 1 else ''} of beer on the wall.\n")
        elif i == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
            keep_singing = False
        i -= 1