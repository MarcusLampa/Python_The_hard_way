then_tings = "apples Orages Crows Telepone Light Sugar"
print("Wait tere are not 10 tings in that list, Lets's fix it.")

stuff = then_tings.split(" ")
more_stuff = ["day", "nighat", "Song", "frisbee", 
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some more tings with stuff.")

print(stuff[1])
print(stuff[-1])
print("" .join(stuff))
print(' ' .join(stuff))
print('#' .join(stuff[3:5]))