from tkinter import *
import time

root = Tk()
root.title('Login Page')

given_user = 'Username'
given_password = 'Password1'

time.sleep(4)

print('Welcome user, please log in to authenticate')

time.sleep(2)

e = Entry(root, width=50, bg='black', fg='grey')
e.pack()
e.insert(0, 'Enter your username: ')

f = Entry(root, width=50, bg='black', fg='grey')
f.pack()
f.insert(0, 'Enter your password: ')

def login():
    fed_user = e.get()
    fed_name_strip = fed_user.replace('Enter your username: ', '')
    if fed_name_strip != given_user:
        print('Incorrect username')
        return
    if fed_name_strip == given_user:
        print('User Authenticated')

    time.sleep(2)
    
    fed_password = f.get()
    fed_pass_strip = fed_password.replace('Enter your password: ', '')
    if fed_pass_strip != given_password:
        print('Incorrect Password')
        return
    if fed_pass_strip == given_password:
        print('Password Accepted')

    time.sleep(2)
    print('Logging in')

my_button = Button(root, text='Login', command = login)
my_button.pack()

root.mainloop()