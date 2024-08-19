import segno
import customtkinter 
from PIL import Image
from tkinter import messagebox, filedialog
from win10toast import ToastNotifier

def create_QR():
    try:
        entry = Text_field.get()  # Access the text field entry
        link = segno.make(entry)
        toaster=ToastNotifier()
        root.withdraw()  # Hiding main window
        file_path = filedialog.asksaveasfilename(
            initialdir='/path/to/Documents', 
            title='Save As', 
            filetypes=(('PNG Files', '*.png'), ('All files', '*.*'))
        )
        if file_path:
            if not file_path.endswith('.png'):
                file_path += '.png'
            link.save(file_path, dark='black', light='blue', scale=10)  # Save the QR code to the selected path
            toaster.show_toast("QR Maker", "Your QR Code Generated Successfully!", duration=5)
    except:
        pass


Image=Image.open('E:/My python projects/QR maker/o.png')

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
root = customtkinter.CTk()
root.title('QR Code Generator')
root.geometry("1100x800+300+200")
root.resizable(False, False)

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=20, pady=60, fill='both', expand=True)

label = customtkinter.CTkLabel(master=frame, text='QR Maker', font=('calibri', 24, 'bold'), text_color='#005abe')
label.pack(padx=20, pady=60)

link_entry= customtkinter.CTkEntry(master=frame, placeholder_text='Enter your Link...', width=300 , corner_radius=12)
link_entry.pack(padx=137, pady=10)

create_Button=customtkinter.CTkButton(master=frame, text="Create QR",text_color='black',width=200,command=create_QR ,corner_radius=12,hover_color="white", image=customtkinter.CTkImage(dark_image=Image),font=('calibri',28,'bold'))
create_Button.pack(padx=137, pady=20)

root.mainloop()