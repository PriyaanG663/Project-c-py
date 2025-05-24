import tkinter as tk
from PIL import Image, ImageTk
import csv
def read_building_count(name,filename="session.csv"):
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            lines = list(reader)
            for line in lines:
                if line[0]==name:
                    return(line[1:])
                    break
        print("No data found for the given name.")
        print("Exiting the program.")
        exit(0)
    except Exception as e:
        print(f"Error reading file: {e}")
    return ["0","0","0"] 
name = input("Enter the name of the person: ")
print(name)
building_count = read_building_count(name)
print(building_count)
root = tk.Tk()
root.title("House Images") 
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()
box_width = 50
box_height = 50
spacing = 20
start_x = 50
start_y = 50

# Load the house image
house_image = Image.open("hut1.png")
house_image = house_image.resize((box_width, box_height), Image.LANCZOS)
hut_photo1 = ImageTk.PhotoImage(house_image)
house_image = Image.open("hut2.png")
house_image = house_image.resize((box_width, box_height), Image.LANCZOS)
hut_photo2 = ImageTk.PhotoImage(house_image)
house_image = Image.open("hut3.png")
house_image = house_image.resize((box_width, box_height), Image.LANCZOS)
hut_photo3 = ImageTk.PhotoImage(house_image)


house_image = Image.open("house1.png")
house_image = house_image.resize((box_width, box_height), Image.LANCZOS)
house_photo1 = ImageTk.PhotoImage(house_image)
house_image = Image.open("house2.png")
house_image = house_image.resize((box_width, box_height), Image.LANCZOS)
house_photo2 = ImageTk.PhotoImage(house_image)
house_image = Image.open("house3.png")
house_image = house_image.resize((box_width, box_height), Image.LANCZOS)
house_photo3 = ImageTk.PhotoImage(house_image)

house_image = Image.open("building1.png")
house_image = house_image.resize((box_width, box_height), Image.LANCZOS)
building_photo1 = ImageTk.PhotoImage(house_image)
house_image = Image.open("building2.png")
house_image = house_image.resize((box_width, box_height), Image.LANCZOS)
building_photo2 = ImageTk.PhotoImage(house_image)
house_image = Image.open("building3.png")
house_image = house_image.resize((box_width, box_height), Image.LANCZOS)
building_photo3 = ImageTk.PhotoImage(house_image)

for i in range(int(building_count[0])):
        x1 = start_x + i * (box_width + spacing)
        y1 = start_y
        if i % 3 == 0:
            house_photo = hut_photo1
        elif i % 3 == 1:
            house_photo = hut_photo2
        else:
            house_photo = hut_photo3
        canvas.create_image(x1, y1, anchor=tk.NW, image=house_photo)
start_y+=box_height + spacing
for i in range(int(building_count[1])):
        x1 = start_x + i * (box_width + spacing)
        y1 = start_y
        if i % 3 == 0:
            house_photo = house_photo1
        elif i % 3 == 1:
            house_photo = house_photo2
        else:
            house_photo = house_photo3
        canvas.create_image(x1, y1, anchor=tk.NW, image=house_photo)
start_y+=box_height + spacing
for i in range(int(building_count[2])):
        x1 = start_x + i * (box_width + spacing)
        y1 = start_y
        if i % 3 == 0:
            house_photo = building_photo1
        elif i % 3 == 1:
            house_photo = building_photo2
        else:
            house_photo = building_photo3
        canvas.create_image(x1, y1, anchor=tk.NW, image=house_photo)
root.mainloop()