import segno
import tkinter as tk
from tkinter import messagebox, filedialog

def create_QR():
    try:
        entry = Text_field.get()  # Access the text field entry
        link = segno.make(entry)
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
            messagebox.showinfo("Success", "QR Code generated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

#User Interface
root = tk.Tk()
root.title('QR maker')
root.geometry("1100x800+300+200")
root.resizable(False, False)
root.iconbitmap('icon22.ico')


# Import elements
search_bar = tk.PhotoImage(file='S.png')
search_bar_label = tk.Label(root, image=search_bar)
search_bar_label.pack(padx=20, pady=10, side=tk.TOP)

# Text field
Text_field = tk.Entry(root, justify='center', width=18, font=('calibri', 40, 'bold'),
                      bg="white", fg='black', border=0)
Text_field.place(x=280, y=70)


btn = tk.Button(root, text='Create QR', width=20, fg='white', font=('calibri', 40, 'bold'), bg='black', command=create_QR)
btn.pack(side='top')


root.mainloop()

