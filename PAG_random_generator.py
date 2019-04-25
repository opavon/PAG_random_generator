cd D:\
python 
import random
date = input("Enter today's date: (YYMMDD)")

# Create a txt file
file = open("Patch_Order_" + str(date) + ".txt", "w")
file.write("This is the order to follow for patching today " + str(date) + ":\n")
file.close()

# Generate a list containing the PAG areas.
PAG_areas = [". Patch dmPAG (right)", ". Patch dlPAG (right)", ". Patch lPAG (right)", ". Patch vlPAG (right)", ". Patch dmPAG (left)", ". Patch dlPAG (left)", ". Patch lPAG (left)", ". Patch vlPAG (left)"]

# Randomly shuffle the areas
random.shuffle(PAG_areas)

# Add list of randomized areas to the txt file
file = open("Patch_Order_" + str(date) + ".txt", "a")
for Cell in range(8):
	file.write("\n	Cell " + str(Cell+1) + str(PAG_areas[Cell]))
	print(PAG_areas[Cell])

file.close()