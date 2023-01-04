from tkinter import *
from Circle import Circle


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def calculate(event):
    # print('Clicked!')  # Test
    radius = user_input.get()  # Radius is a string
    # print(radius)  # Test
    if is_float(radius):  # Radius is now float
        user_input.delete(0, END)
        radius = float(radius)
        circle = Circle(radius)
        txt_field['state'] = 'normal'  # can change field
        txt_field.delete('1.0', END)  # Clear text field from top to bottom
        txt_field.insert(END, 'Radius: ' + str(circle.radius) + '\n')
        txt_field.insert(END, 'Diameter: ' + str(circle.get_diameter()) + '\n')
        txt_field.insert(END, 'Perimeter:' + str(circle.get_perimeter()) + '\n')
        txt_field.insert(END, 'Area:' + str(circle.get_area()) + '\n')
        txt_field['state'] = 'disabled'  # user can't change
    #    print('Number.')  # Test
    # else:
    #    print('Error!')  # Test


# Main window properties
window = Tk()
window.title('Photomath')  # Title text
window.geometry('500x400')  # Wigth = 400, height = 500
window.resizable(False, False)  # True, false = laiust saab muuta, pikkust mitte, False, False = ei saa üldse muuta

# Frames
frame_top = Frame(window, bg='#949AD0', height=20)
frame_top.pack(fill='both')

frame_bottom = Frame(window, bg='#D7DFFD', height=13)
frame_bottom.pack(fill='both')

# First line in frame top
lbl = Label(frame_top, text='Circle radius:', bg='#949AD0')
lbl.pack(side='left')  # Left'i võib kirjutada ka suurte tähtedega, ss ei pea ülakomasid panna

user_input = Entry(frame_top)
user_input.pack(side='left')
user_input.focus()

btn_calc = Button(frame_top, text='Calculate', command=lambda: calculate(0))  # commandil taga ei tohi olla sulge
btn_calc.pack(side='left', padx=6, pady=4)


# Seconf line, big textfield
txt_field = Text(frame_bottom, state=DISABLED)
txt_field.pack(side='left', padx=6, pady=6)

# Bind Entry key
window.bind('<Return>', lambda event: calculate(event))  # event võib olla mis iganes

# No MVC last line
window.mainloop()
