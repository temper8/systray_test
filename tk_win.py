import tkinter as tk

def show_tk_win():
    root = tk.Tk()     
    root.title("Tkinter app")
    root.geometry("300x250")    
    
    label = tk.Label(text="Hello") 
    label.pack()    
 
    root.mainloop()

if __name__ == '__main__':
    show_tk_win()
