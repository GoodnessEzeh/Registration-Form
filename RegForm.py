from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

# Heading
Label(root, text="Goodness' Registration Form", font="ar 15 bold").grid(row=0, column=3)

# Field Name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
nationality = Label(root, text="Nationality")
paymentmode = Label(root, text="Payment Mode")

# Field Packing
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
nationality.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Variable for Storing Data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
nationalityvalue = StringVar
paymentmodevalue = StringVar
checkvalue = IntVar

# Creating Entry Field
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
nationalityentry = Entry(root, textvariable=nationalityvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

# Packing Entry Fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
nationalityentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

# Creating Checkbox
checkbtn = Checkbutton(text="Remember me?", variable_=checkvalue)
checkbtn.grid(row=6, column=3)

# Submit button
Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()