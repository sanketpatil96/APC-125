"""3.	Create a list of colors. Replace the third color with another color and display the updated list."""
colors = ["red","blue","green","yellow","orange"]
print("Initial list of colors:", colors)
new_color = input("Enter new color to replace the third color with :")
colors[2] = new_color
print("Updated list of colors:", colors)