#importing module
import tkinter as tk
 
 #creating empty gui                            
root = tk.Tk()
#function
def test(event):
    button_text = event.widget.cget('text')
    print('Button', button_text,'is pressed')
    
   

#properties
root.geometry('200x200')
 
 #adding two button
button_1 = tk.Button(root, text='1', width=5, height=2)
#right click event.......> 'button-3'
# left click event........> 'Button-1'
# scroll button event......>'Button-2'
button_1.bind('<Button-3>',test)
button_1.pack()

# button_2 = tk.Button(root, text='2', width=5, height=2)
# button_2.pack
button_2 = tk.Button(root, text='1', width=5, height=2)
button_2.bind('<Button-3>',test)
button_2.pack()

#continues display
root.mainloop()
