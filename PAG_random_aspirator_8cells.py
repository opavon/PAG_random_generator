cd D:\
python 
import random
date = input("Enter today's date: (YYMMDD)")

# Create a txt file
file = open("Aspiration_Order_" + str(date) + ".txt", "w")
file.write("This is the order to follow for aspiration today " + str(date) + ":\n")
file.close()

# Generate a list containing the PAG areas
PAG_areas = [". Aspirate dmPAG (right)", ". Aspirate dlPAG (right)", ". Aspirate lPAG (right)", ". Aspirate vlPAG (right)", ". Aspirate dmPAG (left)", ". Aspirate dlPAG (left)", ". Aspirate lPAG (left)", ". Aspirate vlPAG (left)"]

# Randomly shuffle the areas
random.shuffle(PAG_areas)

# Add list of randomized areas to the txt file
file = open("Aspiration_Order_" + str(date) + ".txt", "a")
for Cell in range(8):
	file.write("\n	Cell " + str(Cell+1) + str(PAG_areas[Cell]))
	print(PAG_areas[Cell])

file.close()