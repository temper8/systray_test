import tkinter as tk

def show_tk_win():
    root = tk.Tk()     
    root.title("Tkinter app")
    root.geometry("300x250")    
    
    label = tk.Label(text="Hello", 
                     width=20, height=5,
                     bg="lightgreen") 
    label.pack(expand=1)    
 
    root.mainloop()

if __name__ == '__main__':
    show_tk_win()
