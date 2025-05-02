import qrcode
import tkinter as tk
from tkinter import ttk , messagebox
from PIL import Image, ImageTk
import io

class Hotspotqrgenerator:
    def __init__(self , main_screen):
        self.main_screen = main_screen
        self.main_screen.title("personal hotspot password qr code generator") #change main title here
        self.main_screen.geometry("854x480") #change screen resolution here

        #defining network variables
        self.ssid_var = tk.StringVar() #variable for ssid
        self.passwd_var = tk.StringVar() #variable for passwaord
        self.encrypt_var = tk.StringVar(value='WPA') #default encryption
        self.create_widgets()

    def create_widgets(self):
        #main frame - to show the labels on the screen we create a main frame
        main_frame = tk.Frame(self.main_screen)
        main_frame.grid(padx=20,pady=20)

        #Title
        title = ttk.Label(main_frame , text="Personal Hotspot Generator") #change title here
        title.grid(row=0, column=1, padx=5, pady=5)

        #ssid
        ttk.Label(main_frame , text="Hotspot Name(SSID) : ").grid(row=1, column=0, padx=5 , pady=5)
        ssid_text_entry = ttk.Entry(main_frame , textvariable=self.ssid_var , width=30)
        ssid_text_entry.grid(row=1, column=1, padx=5 , pady=5)

        #password
        ttk.Label(main_frame , text="Password : ").grid(row=2, column=0, padx=5 , pady=5)
        password_text_entry = ttk.Entry(main_frame , textvariable=self.passwd_var , width=30 , show='*')
        password_text_entry.grid(row=2, column=1, padx=5 , pady=5)

        #encryption type : WPA , WEP WPA2 WPA3
        ttk.Label(main_frame , text="Encryption Mode : ").grid(row=3, column=0, padx=5 , pady=5)
        encryption_type = ttk.Combobox(main_frame , textvariable=self.encrypt_var , values=['WPA','WEP','WPA2','WPA3','None'] , state='readonly')
        encryption_type.grid(row=3, column=1, padx=5 , pady=5)

        #generate button
        generate_buttion = ttk.Button(main_frame , text="Generate QR Code", command=self.generate_qrcode)
        generate_buttion.grid(row=5, column=1, padx=5 , pady=5)

        #qr code display
        self.qr_label= ttk.Label(main_frame)
        self.qr_label.grid(row=6, column=1, padx=5 , pady=5)

    def generate_qrcode(self):
        ssid = self.ssid_var.get()
        password = self.passwd_var.get()
        encryption_val = self.encrypt_var.get()

        if not ssid:
            messagebox.showerror("SSID not found","Please enter a SSID")
            return

        if encryption_val != None and not password:
            messagebox.showerror("Password is required","Please enter a password")
            return

        #create qrcode string
        if encryption_val == 'None':
            wifi_string = f"WIFI:T:none;S:{ssid};;"
        else:
            wifi_string = f"WIFI:T:{encryption_val};S:{ssid};P:{password};;"

        #generate qr
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,)
        qr.add_data(wifi_string)
        qr.make(fit=True)

        qr_code_image = img = qr.make_image(fill_color="black", back_color="white")
        img_tk = ImageTk.PhotoImage(img)
        self.qr_label.config(image=img_tk)
        self.qr_label.image = img_tk

if __name__ == '__main__':
    root = tk.Tk()
    app = Hotspotqrgenerator(root)
    root.mainloop()
