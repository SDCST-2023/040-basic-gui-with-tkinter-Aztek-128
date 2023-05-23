import tkinter as tk
from tkinter.constants import LEFT, RIGHT


window = tk.Tk()
window.title("example")
window.geometry("250x150")


dog = tk.PhotoImage(file="dog.png")
labeldog = tk.Label(window, image = dog)
label1 = tk.Label(window,text="pochacco")
label2 = tk.Label(window,text="a cuddly little puppy! This is from the same \ncreators who brouht you Keropi and Kero Kero", bg="#ADD8E6")




labeldog.place(x = 40, y =0)
label1.place(x = 110, y = 40)
label2.place(x = 0, y = 100)


window.mainloop()
exit()
