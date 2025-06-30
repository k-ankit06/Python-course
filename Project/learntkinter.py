# Tkinter
#       ------> pyhton GUI library

# tkinter ----> design ----> desktop applications



import tkinter as tk

app = tk.Tk()

app.geometry("900x500")
app.title("My Fisrt GUI App")
app.config(bg="#2596be")

# Widegts
# text ---> label()
# input_box ---> entry()
# button ---> button()
# font = (font_family, font_size, font_style)

lbl = tk.Label(app, text= "Hello World", font=("Arial Bold",30,"underline"), bg ="#02181e", fg = "White")
lbl.pack(fill="x",pady = 20, padx= 20)

inpx = tk.Entry(app, font=("Arial", 20), bg="White", fg="Black", bd=5, relief="groove")
inpx.pack(fill="x", padx=20, pady=10,)

btn= tk.Button(app, text="Click Me", font=("roboto", 20, "bold"), bg="White", fg="Black", bd=5, relief="groove",)
btn.pack(pady=20, padx=20)
app.mainloop()



# Methos to put widgets
# pack() ----> Centre
# grid ----> Row and column
# place ----> Absolute position

