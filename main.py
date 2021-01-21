from tkinter import *
from tkinter import messagebox
import random
import string
import json




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    s1 = string.ascii_uppercase
    #print(s1)
    s2 = string.ascii_lowercase
    #print(s2)
    s3 = string.digits
    #print(s3)
    s4 = string.punctuation
    #print(s4)

    pass_len = int(12)

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)

    random.shuffle(s)
    #print(s)
    gen_pass = ("".join(s[0:pass_len]))
    #print(gen_pass)
    password_entry.insert(0, gen_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have filled the feilds")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                #save data if no data found
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #save updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text= "Email")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "fillemail@gmail.com")

password_entry = Entry(width=21, text=" ")
password_entry.grid(row=3, column=1)

#Button

search_button = Button(text="Search", width=14 , command=gen_password)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", command=gen_password)
generate_button.grid(row=3, column=2)

add_button = Button(width=36, text="Add", command=add_password)
add_button.grid(row=4, column=1, columnspan=2)






window.mainloop()





