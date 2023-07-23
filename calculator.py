# importing tkinter
import tkinter as tk

#lets see what is inside tkinter module
# print(dir(tk))

#lets create the base GUI
root= tk.Tk()

#lets define all functions below this
# def insert7():
#     # print('7 button is press')
#     # #adding the text to the lebel
#     # label.config(text='7')
#     previous_value = label.cget('text')
#     if previous_value == '0':
#         label.config(text='7')
    
#     else:
#      label.config(text=previous_value +'7')
    
    
    
# def insert8():
#     #lets fetch what's already written on the lebel
#     previous_value = label.cget('text')
#     # print(previous_value)
    
#     #if privious value/ already written on label 0
#     if previous_value == '0':
#         label.config(text='8')
#     #if privious value/ already written on label 0
#     else:
#      label.config(text=previous_value +'8')
#     #   label.config(text='8')
# def insert9():
#     previous_value = label.cget('text')
#     if previous_value == '0':
#         label.config(text='9')
    
#     else:
#      label.config(text=previous_value +'9')
    
    
# def insert_multiply():
#         previous_value = label.cget('text')
#         if previous_value !='0':
#             label.config(text=previous_value +'*')

# def evalution():
#     expression = label.cget('text')
#     result = eval(expression)
#     label.config(text=result)
    
#     #for row 4
# def insert4():
#     previous_value = label.cget('text')
#     if previous_value == '0':
#         label.config(text='4')
    
#     else:
#      label.config(text=previous_value +'4')
     
# def insert5():
#     previous_value = label.cget('text')
#     if previous_value == '0':
#         label.config(text='5')
    
#     else:
#      label.config(text=previous_value +'5')
     
# def insert6():
#     previous_value = label.cget('text')
#     if previous_value == '0':
#         label.config(text='6')
    
#     else:
#      label.config(text=previous_value +'6')     
    
        
# def insert_minus():
#         previous_value = label.cget('text')
#         if previous_value !='0':
#             label.config(text=previous_value +'-')
            
#             #for row 3
# def insert1():
#     previous_value = label.cget('text')
#     if previous_value == '0':
#         label.config(text='1')
    
#     else:
#      label.config(text=previous_value +'1')    
     
# def insert2():
#     previous_value = label.cget('text')
#     if previous_value == '0':
#         label.config(text='2')
    
#     else:
#      label.config(text=previous_value +'2')     
     
# def insert3():
#     previous_value = label.cget('text')
#     if previous_value == '0':
#         label.config(text='3')
    
#     else:
#      label.config(text=previous_value +'3')   
     
# def insert_plus():
#         previous_value = label.cget('text')
#         if previous_value !='0':
#             label.config(text=previous_value +'+')
#             #for row 4
# def insert0():
#     previous_value = label.cget('text')
#     if previous_value == '0':
#         label.config(text='0')
    
    # else:
    #  label.config(text=previous_value +'0')  
        
# def insert_decimal():
#     previous_value = label.cget('text')
#     if previous_value == '0':
#         label.config(text='.')
    
#     else:
#      label.config(text=previous_value +'.')             
            
# def insert_decimal():
#     previous_value = label.cget('text')
#     if previous_value == '0':
#         label.config(text='.')
    
#     else:
#      label.config(text=previous_value +'.') 
     
# def insert_divide():
#         previous_value = label.cget('text')
#         if previous_value !='0':
#             label.config(text=previous_value +'/')

# #for row 0
# def insert_delete(first, last=None):
#         previous_value = label.cget('text')
#         if previous_value !='0':
#             label.config(text=previous_value +'DEL')
# def insert_delete():
#         previous_value = label.cget('text')
#         if previous_value !='0':
#             label.config(text=previous_value +'DEL')







#lets create the test function
def test(event):
    button_pressed = event.widget.cget('text')
    # print(button_pressed)
    if button_pressed == '=':
        expression = label.cget('text')
        result = eval(expression)
        label.config(text=result)
    elif button_pressed == "CE" or button_pressed == "c" or button_pressed == "DEL":
        label.config(text=' ')
    else:
        label_text = str(label.cget('text'))
        if label_text == '0':
            label.config(text=button_pressed)
        else:
            label_text += button_pressed
            label.config(text=label_text)
        
        
        
    
            
            


#gui prpperties
#size change
root.geometry('320x465')
root.resizable(width=False,height=False) #fixed size
root.title('calculator')  #title change
root.iconbitmap('calculator pic (1).ico')   # using this we can show icone on our calculator.....> for this firstly download normal icon pic then type on google png to ico converter and go for free link and conver png to ico or use this link https://www.freeconvert.com/png-to-ico ......> for easy use download that ico pic in the same folder and click right and copy relative  path and paste that path
#giving background color to root gui..............   for color use hex code,........  https://www.color-meanings.com/shades-of-yellow-color-names-html-hex-rgb-codes/
root.config(bg='#FFFDD0')

#adding widget now
# label widget to disply text
label = tk.Label(root, text='0',font=('Comic Sans MS',35,), anchor='e',padx=10)    #..........agr yaha padding dete h toh ye label ki wall aur txt kr bich me aati h
label.pack( pady=(65,10),fill='x')     #anchor north side ya dusri koi side ke kam aata h.......agr hum yaha padding dete h toh ye padding gui aur text ke bich aati h
#lets run mainloop......> continue open gui

#lets add a new container in root gui
frame= tk.Frame(root,bg='#FFFDD0')
frame.pack(fill='both')

# #variable for bg
# bg_color='#ffffff'......> so we can make changes using single variable



#add bottons...> row 0....>percentage,CE,C, delete
btn_percent=tk.Button(frame, text='%',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_ce=tk.Button(frame, text='CE',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_c=tk.Button(frame, text='C',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_Delete=tk.Button(frame, text='DEL',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))

btn_percent.grid(row=0,column=0,padx=3,pady=3)
btn_ce.grid(row=0,column=1,padx=3,pady=3)
btn_c.grid(row=0,column=2,padx=3,pady=3)
btn_Delete.grid(row=0,column=3,padx=3,pady=3  )

#lets bind the left click event
btn_percent.bind('<Button-1>',test)
btn_ce.bind('<Button-1>',test)
btn_c.bind('<Button-1>',test)
btn_Delete.bind('<Button-1>',test)




#add bottons...> row 1....>7,8,9,*
'''

btn_7=tk.Button(frame, text='7',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9),command=insert7) 
....>if uhh want to use long method then write command for each button

'''

btn_7=tk.Button(frame, text='7',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_8=tk.Button(frame, text='8',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_9=tk.Button(frame, text='9',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_x=tk.Button(frame, text='*',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))

btn_7.grid(row=1,column=0,padx=3,pady=3)
btn_8.grid(row=1,column=1,padx=3,pady=3)
btn_9.grid(row=1,column=2,padx=3,pady=3)
btn_x.grid(row=1,column=3,padx=3,pady=3 )

#lets bind the left click event
btn_7.bind('<Button-1>',test)
btn_8.bind('<Button-1>',test)
btn_9.bind('<Button-1>',test)
btn_x.bind('<Button-1>',test)

#add bottons...> row 2....>4,5,6,-
btn_4=tk.Button(frame, text='4',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_5=tk.Button(frame, text='5',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_6=tk.Button(frame, text='6',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_minus=tk.Button(frame, text='-',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))

btn_4.grid(row=2,column=0,padx=3,pady=3)
btn_5.grid(row=2,column=1,padx=3,pady=3)
btn_6.grid(row=2,column=2,padx=3,pady=3)
btn_minus.grid(row=2,column=3,padx=3,pady=3 )

#lets bind the left click event
btn_4.bind('<Button-1>',test)
btn_5.bind('<Button-1>',test)
btn_6.bind('<Button-1>',test)
btn_minus.bind('<Button-1>',test)

#add bottons...> row 3....>1,2,3,+
btn_1=tk.Button(frame, text='1',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_2=tk.Button(frame, text='2',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_3=tk.Button(frame, text='3',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_plus=tk.Button(frame, text='+',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))

btn_1.grid(row=3,column=0,padx=3,pady=3)
btn_2.grid(row=3,column=1,padx=3,pady=3)
btn_3.grid(row=3,column=2,padx=3,pady=3)
btn_plus.grid(row=3,column=3,padx=3,pady=3 )

#lets bind the left click event
btn_1.bind('<Button-1>',test)
btn_2.bind('<Button-1>',test)
btn_3.bind('<Button-1>',test)
btn_plus.bind('<Button-1>',test)

#add bottons...> row 4....>=,0,.,/
btn_equal=tk.Button(frame, text='=',width=9,height=3,bg='#1e90ff',fg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_0=tk.Button(frame, text='0',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_decimal=tk.Button(frame, text='.',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))
btn_divide=tk.Button(frame, text='/',width=9,height=3,bg='#ffffff',relief='groove',font=('Trebuchet',9))

btn_equal.grid(row=4,column=0,padx=3,pady=3)
btn_0.grid(row=4,column=1,padx=3,pady=3)
btn_decimal.grid(row=4,column=2,padx=3,pady=3)
btn_divide.grid(row=4,column=3,padx=3,pady=3 )

btn_equal.bind('<Button-1>',test)
btn_0.bind('<Button-1>',test)
btn_decimal.bind('<Button-1>',test)
btn_divide.bind('<Button-1>',test)

#lets run mainloop
root.mainloop()
