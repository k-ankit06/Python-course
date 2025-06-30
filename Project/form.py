import tkinter as tk

def submit_form():
    name = ent1.get()
    age = ent2.get()
    phone = ent3.get()
    email_val = ent4.get()
    message_val = ent5.get("1.0", tk.END)
    print("Name:", name)
    print("Age:", age)
    print("Phone:", phone)
    print("Email:", email_val)
    print("Message:", message_val)


main = tk.Tk()
main.geometry("700x750")
main.title("Registration Form")

x = tk.Label(main, text = "")

First_name = tk.Label(main, text= "Full Name", font=("roboto",15,"bold"))
age = tk.Label(main, text= "Age", font=("roboto",15,"bold"))
p_number = tk.Label(main, text= "Phone Number", font=("roboto",15,"bold"))
email = tk.Label(main, text= "E-mail", font=("roboto",15,"bold"))
message = tk.Label(main, text = "Message", font=("roboto",15,"bold"))

lbl6 = tk.Label(main, text= ":")
lbl7 = tk.Label(main, text= ":")
lbl8 = tk.Label(main, text= ":")
lbl9 = tk.Label(main, text= ":")
lbl10 = tk.Label(main, text= ":")

ent1 = tk.Entry(main, font=("roboto", 23, "bold"))
ent2 = tk.Entry(main, font=("roboto", 23, "bold"))
ent3 = tk.Entry(main, font=("roboto", 23, "bold"))
ent4 = tk.Entry(main, font=("roboto", 23, "bold"))
ent5 = tk.Text(main, font=("roboto", 23, "bold"), height=5, width= 20)

x.grid(row=0, column=1, padx=10, pady=10)
First_name.grid(row=1, column=1, padx = 10, pady= 10)
age.grid(row=2, column=1, padx= 10, pady=10)
p_number.grid(row=3, column=1, padx= 10, pady=10)
email.grid(row=4, column=1, padx= 10, pady=10)
message.grid(row=5, column=1, padx= 10, pady=10)

lbl6.grid(row=1, column=2, padx=10, pady=10)
lbl7.grid(row=2, column=2, padx=10, pady=10)
lbl8.grid(row=3, column=2, padx=10, pady=10)
lbl9.grid(row=4, column=2, padx=10, pady=10)
lbl10.grid(row=5, column=2, padx=10, pady=10)

ent1.grid(row=1, column=3, padx=10, pady=10)
ent2.grid(row=2, column=3, padx=10, pady=10)
ent3.grid(row=3, column=3, padx=10, pady=10)
ent4.grid(row=4, column=3, padx=10, pady=10)
ent5.grid(row=5, column=3, padx=10, pady=10)


submit_btn = tk.Button(main, text="Submit", font=("roboto", 18, "bold"), bg="#2596be", fg="white", command=submit_form)
submit_btn.grid(row=6, column=3, pady=30)

main.mainloop()