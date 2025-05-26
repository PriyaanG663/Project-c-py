import tkinter as tk
from PIL import Image, ImageTk
import csv
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


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


def ranking(name,filename="session.csv"):
    try:
        with open(filename, "r") as f:
            l=[]
            reader = csv.reader(f)
            lines = list(reader)
            for line in lines:
                s=0
                for i in range(1,4):
                    s+=int(line[i])*i
                l.append((line[0],s))
                if line[0]==name:
                     p=s
            l.sort(key=lambda x: x[1], reverse=True)
            return [l[0:3],l.index((name,p))+1]
    except Exception as e:
        print(f"Error reading file: {e}")
    return []


def overall(filename="session.csv"):
    try:
        with open(filename, "r") as f:
            l=[0,0,0]
            reader = csv.reader(f)
            lines = list(reader)
            for line in lines:
                l[0] += int(line[1])
                l[1] += int(line[2])
                l[2] += int(line[3])    
            return l
    except Exception as e:
        print(f"Error reading file: {e}")
    return []


name = input("Enter the name of the person: ")
print(name)
building_count = read_building_count(name)
ranks=ranking(name)
print(building_count)

root = tk.Tk()
root.title("House Images") 
canvas = tk.Canvas(root, width=800, height=400, bg="white")
canvas.pack()
box_width = 50
box_height = 50
spacing = 20
start_x = 100
start_y = 100

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

canvas.create_text(400, 50, text="Your Progress!", font=("Arial", 20))
canvas.create_text(30, 100, text="Easy:", font=("Arial", 10))

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

canvas.create_text(30, start_y, text="Medium:", font=("Arial", 10))
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

canvas.create_text(30, start_y, text="Hard:", font=("Arial", 10))
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

start_y= start_y + box_height + spacing
canvas.create_text(100, start_y, text="Ranking Top 3:", font=("Arial", 10))
i=0
print(ranks)
for player, score in ranks[0]:
    canvas.create_text(100, start_y + (i+1) * 20, text=f"{i + 1}. {player} - {score}", font=("Arial", 15))
    i += 1

canvas.create_text(100, start_y + 4*20 , text=f"Your Rank: {ranks[1]}", font=("Arial", 15))


fig = plt.Figure(figsize=(4, 3), dpi=100) # Adjust figsize as needed
ax = fig.add_subplot(111)
x_values = []
y_values = []
ax.bar(x_values, y_values)
canvas_widget = FigureCanvasTkAgg(fig, master=root)
canvas_widget_canvas = canvas_widget.get_tk_widget()
canvas_widget_canvas.pack()

fig = plt.Figure(figsize=(4, 3), dpi=100) # Adjust figsize as needed
ax = fig.add_subplot(111)
x_values = ["Easy", "Medium", "Hard"]
y_values = [int(building_count[0]), int(building_count[1]), int(building_count[2])]
ax.bar(x_values, y_values)
ax.set_title('Bar graph of Your Records')
canvas_widget = FigureCanvasTkAgg(fig, master=root)
canvas_widget_canvas = canvas_widget.get_tk_widget()
canvas_widget_canvas.place(x=10,y=400)

lp=overall()
fig = plt.Figure(figsize=(4, 3), dpi=100) # Adjust figsize as needed
ax = fig.add_subplot(111)
x_values = ["Easy", "Medium", "Hard"]
y_values = lp
ax.bar(x_values, y_values)
ax.set_title('Bar graph of All Records')
canvas_widget = FigureCanvasTkAgg(fig, master=root)
canvas_widget_canvas = canvas_widget.get_tk_widget()
canvas_widget_canvas.place(x=400,y=400)


root.mainloop()