import os
from tkinter import messagebox
import json
from pathlib import Path
from global_variable import *
# Explicit imports to satisfy Flake8
from tkinter import*
#Tk, Canvas, Entry, Text, Button, PhotoImage
import random 
import array 
MAX_LEN = 12
global response
global logged_in
logged_in = False
global strongPassword
strongPassword = None
response = None



def generatePassword():
    # maximum length of password needed 
    # this can be changed to suit your password length 
    global MAX_LEN  
    # declare arrays of the character that we need in out password 
    # Represented as chars to enable easy string concatenation 
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                        'z'] 
    
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                        'Z'] 
    
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
            '*', '(', ')', '<'] 
    
    # combines all the character arrays above to form one array 
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS 
    
    # randomly select at least one character from each character set above 
    rand_digit = random.choice(DIGITS) 
    rand_upper = random.choice(UPCASE_CHARACTERS) 
    rand_lower = random.choice(LOCASE_CHARACTERS) 
    rand_symbol = random.choice(SYMBOLS) 
    
    # combine the character randomly selected above 
    # at this stage, the password contains only 4 characters but  
    # we want a 12-character password 
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 
    
    
    # now that we are sure we have at least one character from each 
    # set of characters, we fill the rest of 
    # the password length by selecting randomly from the combined  
    # list of character above. 
    for x in range(MAX_LEN - 4): 
        temp_pass = temp_pass + random.choice(COMBINED_LIST) 
    
        # convert temporary password into array and shuffle to  
        # prevent it from having a consistent pattern 
        # where the beginning of the password is predictable 
        temp_pass_list = array.array('u', temp_pass) 
        random.shuffle(temp_pass_list) 
    
    # traverse the temporary password array and append the chars 
    # to form the password 
    password = "" 
    for x in temp_pass_list: 
            password = password + x 
            
    # print out password 
    return password

############################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Lấy đường dẫn thư mục chứa file mã nguồn
SOURCE_PATH = Path(__file__).parent

# Xây dựng đường dẫn tương đối cho thư mục assets
ASSETS_PATH = SOURCE_PATH/"build"/ "assets" / "frame0" #signupform
ASSETS_PATH1 = SOURCE_PATH /"build"/ "assets" / "frame1" #loginform

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def relative_to_assets1(path: str) -> Path:
    return ASSETS_PATH1 / Path(path)

# Các hàm khác bạn có thể giữ nguyên

def load_image_login():
    global image_image_1_1, image_image_2_2, image_image_3_3, image_image_4_4
    global entry_image_1_1, entry_image_2_2
    global button_image_1_1, button_image_2_2

    button_image_1_1 = PhotoImage(file=relative_to_assets1("button_1.png")) 
    button_image_2_2 = PhotoImage(file=relative_to_assets1("button_2.png"))

    entry_image_1_1 = PhotoImage(file=relative_to_assets1("entry_1.png"))
    entry_image_2_2 = PhotoImage(file=relative_to_assets1("entry_2.png"))

    image_image_1_1 = PhotoImage(file=relative_to_assets1("image_1.png"))
    image_image_2_2 = PhotoImage(file=relative_to_assets1("image_2.png"))
    image_image_3_3 = PhotoImage(file=relative_to_assets1("image_3.png"))
    image_image_4_4 = PhotoImage(file=relative_to_assets1("image_4.png"))
def load_image_signup():
    global image_image_2, image_image_1, image_image_3, image_image_4, image_image_5
    global entry_image_1, entry_image_2, entry_image_3
    global button_image_1, button_image_2 

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png")) #loginmini
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))  #signup

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"build\assets\frame0")
def relative_to_assets1(path: str) -> Path:
    return ASSETS_PATH1 / Path(path)
#####################################################
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#---------------------------------------
#------------------------------------------
def login():
    root = Tk()
    root.title("Log In")
    root.geometry("640x528")
    root.configure(bg = "#FFFFFF")
    root.resizable(False, False)
    def signup_command():
        #global image_image_1, image_image_2, image_image_3, image_image_4, image_image_5
        #global entry_image_1, entry_image_2, entry_image_3
        #global button_1, button_2

        window = Toplevel(root)
        window.title("Sign Up")
        #window.geometry("669x528")
        window.geometry(f"{root.winfo_width()}x{root.winfo_height()}+{root.winfo_x()}+{root.winfo_y()}")
        window.configure(bg = "#FFFFFF")
        global response
        response = messagebox.askquestion("Password", "Sử dụng mật khẩu do hệ thống đề xuất ?")
        window.lift()
        if response == 'yes':
            global strongPassword
            strongPassword = generatePassword()
            messagebox.showinfo('New Password','Mật khẩu của bạn là '+ strongPassword +', hãy ghi nhớ!')
            window.lift()

        def signup():
            username = user.get()
            password = code.get()
            confirm_password = confirm_pw.get()
            strength = check_password_strength(password)
            if strength != "Strong password.":
                messagebox.showwarning("Password Strength", strength)
                window.lift()
                return 
            if len(username) > 15:
                messagebox.showerror('Invalid', 'Username should not exceed 15 characters')
                window.lift()
                return
            if username == 'Username':
                messagebox.showerror('Invalid', 'Username should not be empty or distinguished from "Username"')
                window.lift()
                return
            if password == confirm_password:
                with open('database.json', 'r') as data:
                        accounts = json.load(data)
                        is_new_user = 1
                        for acc in accounts:
                            if username in acc:
                                messagebox.showerror('Invalid', 'This username has existed, try again')
                                window.lift()
                                is_new_user=0
                                break
                        if is_new_user:
                            new_accounts = {username: password}
                            accounts.append(new_accounts)
                            messagebox.showinfo('valid', 'sign up successfully')
                            with open('database.json','w') as save:
                                json.dump(accounts, save, indent = 4)
                            window.destroy()
            else:
                messagebox.showerror('Invalid', 'Both password should match')
                window.lift()
        def sign():
            window.destroy()
    #---------------------------------------------------
        load_image_signup()
        canvas1 = Canvas(
            window,
            bg = "#FFFFFF",
            height = 528,
            width = 669,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        # nút sign up lớn
        button_2 = Button(window,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command= signup, # hàm sign up
            relief="flat"
        )
        button_2.place(
            x=231.0,
            y=379.0,
            width=185.0,
            height=63.0
        )
        window.resizable(False, False)
        canvas1.place(x=0, y=0)
        # image decor
        # ảnh nền
        image_1 = canvas1.create_image(
            334.0,
            264.0,
            image=image_image_1
        )
        entry_bg_1 = canvas1.create_image(
            312.0386657714844,
            170.5,
            image=entry_image_1
        )
        entry_bg_2 = canvas1.create_image(
            312.0386657714844,
            259.5,
            image=entry_image_2
        )
        entry_bg_3 = canvas1.create_image(
            312.0386657714844,
            351.5,
            image=entry_image_3
        )
        image_2 = canvas1.create_image(
            180.0,
            120.0,
            image=image_image_2
        )
        image_3 = canvas1.create_image(
            187.0,
            215.0,
            image=image_image_3
        )

        image_4 = canvas1.create_image(
            197.0,
            305.0,
            image=image_image_4
        )
        image_5 = canvas1.create_image(
            249.0,
            465.0,
            image=image_image_5
        )
    #----------------------------------------------------------
        # user
        user = Entry(window,
            bd=0,
            bg="#EAECF2",
            fg="#000716",
            highlightthickness=0
        )
        user.place(
            x=167.0,
            y=150.0,
            width=300.0,
            height=24.0
        )
        def on_enter(e):
            name = user.get()
            if name == 'Username':
                user.delete(0, 'end')
        def on_leave(e):
                name = user.get()
                if name == '':
                    user.insert(0,'Username')    
        user.insert(0, 'Username')
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)
        # password
        def toggle_password_visibility():
            if show_password.get():
                code.config(show="")
                confirm_pw.config(show="")
            else:
                code.config(show="*")
                confirm_pw.config(show="*")
        def toggle_password_visibility1():
            if show_password.get():
                code.config(show="")
            else:
                code.config(show="*")
        def toggle_password_visibility2():
            if show_password.get():
                confirm_pw.config(show="")
            else:
                confirm_pw.config(show="*")

        # Create a BooleanVar to control password visibility
        show_password = BooleanVar(value = False) 
        code = Entry(window,
            bd=0,
            bg="#EAECF2",
            fg="#000716",
            highlightthickness=0
        )
        code.place(
            x=165.0,
            y=242.0,
            width=300.0,
            height=24.0
        )
        def on_enter(e):
            name = code.get()
            if name == 'Password':
                code.delete(0, 'end')
                toggle_password_visibility1()
        def on_leave(e):
            name = code.get()
            if name == '':
                code.insert(0, 'Password')
        if response == 'yes':
            code.insert(0, strongPassword)
        else:
            code.insert(0, 'Password')
        
        code.bind("<FocusIn>", on_enter)
        code.bind("<FocusOut>", on_leave)
        # confirm password
        confirm_pw = Entry(window,
            bd=0,
            bg="#EAECF2",
            fg="#000716",
            highlightthickness=0
        )
        confirm_pw.place(
            x=165.0,
            y=332.0,
            width=300.0,
            height=24.0
        )
        def on_enter(e):
            name = confirm_pw.get()
            if name == 'Confirm Password':
                confirm_pw.delete(0, 'end')
                toggle_password_visibility2()
        def on_leave(e):
            name = confirm_pw.get()
            if name == '':
                confirm_pw.insert(0, 'Confirm Password')
        if response == 'yes':
            confirm_pw.insert(0, strongPassword)
        else:
            confirm_pw.insert(0, 'Confirm Password')
        confirm_pw.bind("<FocusIn>", on_enter)
        confirm_pw.bind("<FocusOut>", on_leave)
    #--------------------------------------------------------------------
        # nút login trong cửa sổ sign up
        button_1 = Button(window,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=sign,
            relief="flat"
        )
        button_1.place(
            x=413.0,
            y=453.0,
            width=103.0,
            height=32.0
        )
    #--------------------------------------------------
        def check_password_strength(password):
            # Check the length of the password
            if len(password) < 8:
                return "Password must be at least 8 characters long."
            # Check if the password contains at least one uppercase and one lowercase letter
            if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
                return "Password must contain both uppercase and lowercase letters."
            # Check if the password contains at least one digit
            if not any(char.isdigit() for char in password):
                return "Password must contain at least one digit."
            # Password is considered strong
            return "Strong password."
        
        # Define a function to toggle password visibility
        # Define a function to toggle password visibility
        
        # Create a checkbox to toggle password visibility
        show_password_checkbox = Checkbutton(
        window,
        text= None,
        variable=show_password,
        command=toggle_password_visibility
        )
        show_password_checkbox.place(x=450, y=240)
        window.resizable(False, False)
        window.bind('<Return>', lambda event: signup())
        window.mainloop()
    global User_name
    def sign_in():
        global logged_in
        global User_name
        flag = False
        username = user.get()
        password = code.get()
        if len(username) > 15:
            messagebox.showerror('Invalid', 'Username should not exceed 15 characters')
            return
        with open('database.json', 'r') as data:
            accounts = json.load(data)
            for account in accounts:
                if username in account and account[username] == password:
                    messagebox.showinfo('Valid', 'Sign in successfully')
                    User_name = username
                    flag = True
                    logged_in = True
                    root.destroy() 
                    break
        if not flag: messagebox.showerror('Invalid','The username or password is invalid, try again')
#--------------------------------------------------------------------------------------------------------------
#@@@@@@@@@ LOGIN @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    load_image_login()
    canvas = Canvas(
    root,
    bg = "#FFFFFF",
    height = 528,
    width = 640,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )
    # nút login lớn
    button_2_2 = Button(root,
        image=button_image_2_2,
        borderwidth=0,
        highlightthickness=0,
        command= sign_in,
        relief="flat"
    )
    button_2_2.place(
        x=214.0,
        y=320.0,
        width=150.0,
        height=49.0
    )
    def confirm_close():
        response = messagebox.askquestion("Stop logging", "Ngừng đăng nhập sẽ đóng trò chơi, bạn vẫn muốn tiếp tục ?")
        if response=='yes':
            exit()
    root.protocol("WM_DELETE_WINDOW", confirm_close)
    root.resizable(False, False)
    canvas.place(x=0, y=0)
    # ảnh nền
    image_1_1 = canvas.create_image(
        320.0,
        264.0,
        image=image_image_1_1
    )
    entry_bg_1_1 = canvas.create_image(
        306.0,
        287.0,
        image=entry_image_1_1
    )
    entry_bg_2_2 = canvas.create_image(
        306.0,
        202.0,
        image=entry_image_2_2
    )
    image_2_2 = canvas.create_image(
        200.0,
        158.0,
        image=image_image_2_2
    )
    image_3_3 = canvas.create_image(
        209.0,
        248.0,
        image=image_image_3_3
    )

    image_4_4 = canvas.create_image(
        249.0,
        398.0,
        image=image_image_4_4
    )
#-------------------------------------------------
    user = Entry(root,
    bd=0,
    bg="#EAECF2",
    fg="#000716",
    highlightthickness=0
    )
    user.place(
        x=170.0,
        y=184.0,
        width=290.0,
        height=22.0
    )
    def on_enter(e):
            name = user.get()
            if name == 'Username':
                user.delete(0, 'end')
    def on_leave(e):
            name = user.get()
            if name == '':
                user.insert(0,'Username')
    user.insert(0, 'Username')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)
    # password
    def toggle_password_visibility():
            if show_password.get():
                code.config(show="")
            else:
                code.config(show="*")

        # Create a BooleanVar to control password visibility
    show_password = BooleanVar(value = False)
    code = Entry(root,
        bd=0,
        bg="#EAECF2",
        fg="#000716",
        highlightthickness=0
    )
    code.place(
        x=170.0,
        y=270.0,
        width=290.0,
        height=22.0
    )
    def on_enter(e):
            name = code.get()
            if name == 'Password':
                code.delete(0, 'end')
                toggle_password_visibility()
            
                
    def on_leave(e):
            name = code.get()
            if name == '':
                code.insert(0, 'Password')
    if response == 'yes':
        code.insert(0, strongPassword)
    else:
        code.insert(0, 'Password')

    
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)
#-----------------------------------------------------
    # nút sign up trong cửa sổ login
    button_1_1 = Button(root,
        image=button_image_1_1,
        borderwidth=0,
        highlightthickness=0,
        command=signup_command,
        relief="flat"
    )
    button_1_1.place(
        x=393.0,
        y=385.0,
        width=106.0,
        height=33.0
    )
    
        # Create a checkbox to toggle password visibility

    show_password_checkbox = Checkbutton(
    root,
    text= None,
    variable=show_password,
    command=toggle_password_visibility,
    width=1,
    height=1
    )
    show_password_checkbox.place(x=425, y=270)
    root.bind('<Return>', lambda event: sign_in())
    root.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------
#@@@@@@@@@@@@@@@@@@@@@@@ SIGN UP @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
#############################################################################################
""""root = Tk()
root.title("Log In")
root.geometry("640x528")
root.configure(bg = "#FFFFFF")
#root.resizable(False, False)
login()

root.mainloop()"""