from tkinter import *
from tkinter import messagebox
from password import PasswordGenerator  # Import the PasswordGenerator class
import pyperclip
import json

BACKGROUND_COLOR = "#ffffff"

# Create an instance of PasswordGenerator class
password = PasswordGenerator()


# Function to generate a password and copy it to the clipboard
def generate_password():
    pword = password.generate()
    pyperclip.copy(pword)  # Copy generated password to clipboard
    password_entry.delete(0, END)  # Clear the password entry field
    password_entry.insert(0, pword)  # Insert generated password into the entry field


# Function to save login details to a JSON file
def save_details(details):
    try:
        # Attempt to read existing data from "details.json"
        with open("details.json", "r") as file_data:
            data = json.load(file_data)

    except FileNotFoundError:
        # Create a new "details.json" file if not found and save the details
        with open("details.json", "w") as file_data:
            json.dump(details, file_data, indent=4)

    else:
        # Update existing data with new details and save to "details.json"
        data.update(details)
        with open("details.json", "w") as file_data:
            json.dump(data, file_data, indent=4)


# Function to handle saving login details entered by the user
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(message="Website and Password fields cannot be empty", title="Error")
    else:
        save_details(new_data)  # Save the new login details to "details.json"
        web_entry.delete(0, END)  # Clear the website entry field
        password_entry.delete(0, END)  # Clear the password entry field
        web_entry.focus()  # Set focus back to the website entry field


# Function to search and display stored login details
def search_contact():
    website = web_entry.get()
    if len(website) > 0:
        try:
            with open("details.json") as file_data:
                data = json.load(file_data)
                result = data[website]
                messagebox.showinfo(title=website, message=f"Email: {result['email']}\nPassword: {result['password']}")
        except KeyError:
            messagebox.showinfo(title="Missing record", message=f"Details for {website} not found.")
        except FileNotFoundError:
            messagebox.showinfo(title="Missing record", message="No records found.")
    else:
        messagebox.showerror(message="Please provide a website to search", title="Error")


# User Interface Setup
window = Tk()
window.title("Password Manager")
window.minsize(240, 240)
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

# Load the logo image
img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(100, 100, image=img)
canvas.grid(row=1, column=2)

# Labels and entry fields for website, email, and password
web_label = Label(text="Website:", bg=BACKGROUND_COLOR)
web_label.grid(row=2, column=1)
web_entry = Entry(width=32)
web_entry.grid(row=2, column=2)
web_entry.focus()

email_label = Label(text="Email/Username:", bg=BACKGROUND_COLOR)
email_label.grid(row=3, column=1)
email_entry = Entry(width=50)
email_entry.grid(row=3, column=2, columnspan=2)
email_entry.insert(0, "h@gmail.com")

password_label = Label(text="Password:", bg=BACKGROUND_COLOR)
password_label.grid(row=4, column=1)
password_entry = Entry(width=32)
password_entry.grid(row=4, column=2, columnspan=1)

# Buttons for generating password, adding, and searching details
password_generate_btn = Button(text="Generate Password", command=generate_password)
password_generate_btn.grid(row=4, column=3)
add_btn = Button(text="Add", width=42, command=save)
add_btn.grid(row=5, column=2, columnspan=2)
search_btn = Button(text="Search", command=search_contact, width=15)
search_btn.grid(row=2, column=3, columnspan=1)

window.mainloop()
