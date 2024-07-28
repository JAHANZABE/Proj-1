import json
import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser


root=Tk()
root.title("RESTful API CURD(Create, Update, Read Delete) Operation Project by         JAHANZABE KHAN")

#root.iconbitmap('F:\Tkinter exe request files\ICON2.ico')



s=ttk.Style()

s.theme_use("clam") # #---Use 1:- alt, 2:-clam, 3:-classic, 4:-default or alt


def style1():
           
                  s.theme_use("classic")

def style2():
           
                  s.theme_use("alt")

def style3():
           
                  s.theme_use("clam")
           
n=1                        
def insert():
        global n
        if (ent.get()=='' or nbFr1_ent0.get()=='' or nbFr1_ent1.get()=='' or nbFr1_ent2.get()=='' or nbFr1_ent3.get()==''):
                  messagebox.showinfo('Entry missing', ' "Seat No" , "Name", "Status",  "Urls" or any one of these is Empty ')
        else:
              try:
            
                  tv.delete(*tv.get_children())
                  print('')
                  urls=ent.get()
                  urls_for_insert=nbFr1_ent0.get()
                  convert=int(nbFr1_ent1.get())

                  
                  

                  res_post=requests.post(urls_for_insert, json={"seat" : [convert, nbFr1_ent2.get(), nbFr1_ent3.get()]})

                  #if res_post.ok:
                  fething_data=requests.get(urls).json()
                  print(type(fething_data))     #------ here is list
                 
                  
                  for keys in fething_data:
                              for items in keys.values():  #--dict.values for valu and dict.keys for key
                                          #print(items[0])
                                          #tv.delete(0, end)
                                          
                                          tv.insert('', n  ,values=(items[0], items[1], items[2]))
                                          
                  
                  print(fething_data)
                  res_gets=requests.get(urls)
                  webbrowser.open(urls)
                  n=+1
                  
                  
                  print('Send to server')
              except ValueError:
                  messagebox.showerror("Error", "Only Integer Value Allow in Seat Number")
                  


                #-------------------Second Function Delete Button--------------------#
nn=1
def delete():
        global nn
        if (ent.get()=='' or nbFr2_ent0.get()=='' or nbFr2_ent1.get()==''  or nbFr2_ent3.get()==''):
                  messagebox.showinfo('Entry missing', ' "Seat No" , "Name", "Status",  "Urls" or any one of these is Empty ')
        else:
            try:
                  tv.delete(*tv.get_children())
                  print('')
                  urls=ent.get()
                  urls_for_delete=nbFr2_ent0.get()
                  convert_del=int(nbFr2_ent1.get())
                  

                  
                  

                  res_del=requests.delete(urls_for_delete, json={"seat" : [convert_del, nbFr2_ent2.get(), nbFr2_ent3.get()]})

                  #if res_post.ok:
                  fething_data_del=requests.get(urls).json()
                  print(type(fething_data_del))     #------ here is list
                 
                  
                  for del_keys in fething_data_del:
                              for del_items in del_keys.values():  #--dict.values for valu and dict.keys for key
                                          #print(items[0])
                                          #tv.delete(0, end)
                                          
                                          tv.insert('', nn ,values=(del_items[0], del_items[1], del_items[2]))                  
                  
                  print(fething_data_del)
                  res_gets=requests.get(urls)
                  webbrowser.open(urls)
                  nn=+1
                  
                  
                  print('Send to server')
            except ValueError:
                  messagebox.showerror("Error", "Only Integer Value Allow in Seat Number")





nnn=1
def update():

        global nnn
                          
        
        tv.delete(*tv.get_children())
        print('')
        urls=ent.get()
        urls_for_upd=nbFr3_ent0.get()
        convert_ext=int(nbFr3_ent1.get())

                  
        convert_upd=int(nbFr3_ent4.get())
        nbFr3_ent5.get()
        nbFr3_ent6.get()

                  
                  
        try:
                  fething_data=requests.get(urls).json()
                  print(type(fething_data))     #------ here is list

                  index=fething_data.index({"seat" : [convert_ext, nbFr3_ent2.get(), nbFr3_ent3.get()]})  # This Line getting index number where we want to update this
                  str_index=str(index)                                                                   #  This Line convet index no in to string because urls not send into integer.
                 


                  
                  

                  res_put=requests.put(urls_for_upd+str_index, json={"seat" : [convert_upd, nbFr3_ent5.get(), nbFr3_ent6.get()]})
                  new_upd_data=(requests.get('https://jahanzabekhan.pythonanywhere.com/API/A1').json())

                          #if res_post.ok:
                                    
                  for keys in new_upd_data:
                            for items in keys.values():  #--dict.values for valu and dict.keys for key
                                                  #print(items[0])
                                                  #tv.delete(items)
                                                  
                                        tv.insert('', nnn ,values=(items[0], items[1], items[2]))                  
                  
                  print(fething_data)
                  res_gets=requests.get(urls)
                  webbrowser.open(urls)
                  nnn=+1
                  
                  
                  print('Send to server')
                          
        except ValueError:
                    
                          
                              
                  print("Data or any part in not exit")
                  messagebox.showerror("Data is not Exist", "Any value or data in not Exist.  " 
                                                + str(convert_ext) + "  "+ nbFr3_ent2.get() + "  " + nbFr3_ent3.get()+
                                                "    Please Insert First and update afterward")
        if (ent.get()=='' or nbFr3_ent0.get()=='' or nbFr3_ent1.get()==''  or nbFr3_ent3.get()==''
            or nbFr3_ent4.get()=='' or nbFr3_ent5.get()=='' or nbFr3_ent6.get()==''):
                  messagebox.showinfo('Entry missing', ' "Seat No" , "Name", "Status",  "Urls" or any one of these is Empty ')
def clear():
                  nbFr1_ent1.delete(0, "end")
                  nbFr1_ent2.delete(0, "end")
                  nbFr1_ent3.delete(0, "end")
                  nbFr2_ent1.delete(0, "end")
                  nbFr2_ent2.delete(0, "end")
                  nbFr2_ent3.delete(0, "end")
                  nbFr3_ent1.delete(0, "end")
                  nbFr3_ent2.delete(0, "end")
                  nbFr3_ent3.delete(0, "end")
                  nbFr3_ent4.delete(0, "end")
                  nbFr3_ent5.delete(0, "end")
                  nbFr3_ent6.delete(0, "end")
                  





def helps():
            tl=Toplevel(root)
            tl.title("Help")
            
        
            vrg= '''This Programe Develop by JAHANZABE JAMIL. In this projest API structure is  [{'seat' : ['Seat number' , 'Cuntomer Name', 'Status']}, ...].
            System Requirment:-
                        Windows 10 or Hgiher , 64 bits

            Explaination:-
                    API  rap in List and inside each objects depend on Dictionry, inside of Dictionry keys is 'seat' is constant and
                    value again rap in another List. This list consist on three values names 'Seat Number', 'Customer Name', 'Status'.
                    These values are variables in which we doing CURD operation with the help These programe. Doplicate value is
                    allow for insert(Create).But in Update Operation Value should already Exist for thiss Operation. Only Exist item
                    will be Delete. 

            First 'Help' Button for getting help, Next three Button 'Style' for three Styles that you will change in three diffrent styles.
            Entry bar for URLs for getting Information fron server with structure for (Read) Operation.

            Three Tabs are in this project :-
                    In all three tabs a long Entry bar for server URLs. Each Server address has diffrent End point for diffrent Operation with diffrent name
                    enclose in (Insert) (Delete) (Update). 

                    Insert:-
                              This Tab Create Objects and Inset new Values
                    Delete:-
                              This Tabs Delete Information
                    Update:-
                              This Tab Update resource. If Resource is not Exist then server Return Error.

            Press Button for doing Operation.

            Three Column are show Result in which you see output and automatic open your browser with (Read) Resource for check Result Operation Perfome Correctly.
            Column Data and Server Urls same that rap in second list thst showing you on browser.


            If Columns are Empty after doing Operation, May be Wrong/False Entries Occure, You Enter string value insead of Integer Value
            in Seat Number.


            
            Credit:-
                    M.JAHANZABE JAMIL KHAN

                                            T-H-A-N-K++Y-O-U  '''
            tl_lab=Label(tl, text=vrg)
            tl_lab.pack(pady=50)

                   
            


f1=Frame(root)
f1.pack(pady=10)

fr2=Frame(root)
fr2.pack(pady=10)

lab1=Label(f1, text="This Program Develop by :-   ", font=("Carial Rounded MT Bold", 20))
lab1.grid(row=1,column=1, padx=10, pady=10)

lab2=Label(f1, text=" JAHANZABE KHAN", font=("Cooper Std Black", 30), fg="red")  
lab2.grid(row=1,column=2, padx=10, pady=15)

lab3=Label(f1, text=" This Programe for API and structure is  [{'seat' : ['Seat number' , 'Cuntomer Name', 'Status']}, ...]")
lab3.grid(row=2, column=1, padx=10, pady=10)

#lab3=Label(f1, text=" zz ", font=15, fg="red")
#lab3.grid(row=2, column=2, padx=10, pady=10)



btn1=Button(fr2, text="Help",  bg="green", fg="white", height="2", width="15",  command=helps)
btn1.grid(row=5, column=1, pady=10)

btn2=Button(fr2, text="Style 1", bg="black", fg="white", height="2", width="15", command=style1)  #-----command=lambda: [style1(), style2(), style3()])
btn2.grid(row=5, column=2, pady=10)


btn2=Button(fr2, text="Style 2", bg="black", fg="white", height="2", width="15", command=style2)  #-----command=lambda: [style1(), style2(), style3()])
btn2.grid(row=5, column=3, pady=10)


btn2=Button(fr2, text="Style 3", bg="black", fg="white", height="2", width="15", command=style3)  #-----command=lambda: [style1(), style2(), style3()])
btn2.grid(row=5, column=4, pady=10)


lab=Label(fr2, text="Enter URLs (Read)")
lab.grid(row=6, column=1, sticky="w")

ent=Entry(fr2, width=55)
ent.grid(row=6, columnspan=8, sticky="e")











lf=LabelFrame(root, text="Entries Panel")
lf.pack(padx=10)

lfFr1=Frame(lf)
lfFr1.pack()

lfFr2=LabelFrame(lf, text="Result Panel")
lfFr2.pack()




nb=ttk.Notebook(lfFr1, height=200, width=800)

#-------------------1st fram-----------------------#


nbFr1=Frame(nb)

nbFr1_L1=Label(nbFr1, text='Enter Server URLs (Insert)')
nbFr1_L1.grid(row=0, column=1, padx=5, pady=5, sticky="w")




nbFr1_L1=Label(nbFr1, text='Enter Seat Number')
nbFr1_L1.grid(row=1, column=1, padx=5, pady=5, sticky="w")

nbFr1_L1=Label(nbFr1, text='Enter Name')
nbFr1_L1.grid(row=2, column=1, padx=5, pady=5, sticky="w")

nbFr1_L1=Label(nbFr1, text='Enter Status')
nbFr1_L1.grid(row=3, column=1, padx=5, pady=5, sticky="w")



nbFr1_ent0=ttk.Entry(nbFr1, width="55")
nbFr1_ent0.grid(row=0, column=2)


nbFr1_ent1=ttk.Entry(nbFr1)
nbFr1_ent1.grid(row=1, column=2, sticky="w")

nbFr1_ent2=ttk.Entry(nbFr1)
nbFr1_ent2.grid(row=2, column=2, sticky="w")

nbFr1_ent3=ttk.Entry(nbFr1)
nbFr1_ent3.grid(row=3, column=2, sticky="w")

nbFr1.pack(padx=10, pady=10)

nbFr1_btn1=ttk.Button(nbFr1, text="Insert", command=insert)
nbFr1_btn1.grid(row=4, column=1, pady=10)

nbFr1_btn2=ttk.Button(nbFr1, text="All Clear", command=clear)
nbFr1_btn2.grid(row=4, column=2, pady=10)






#-------------------2nd fram-----------------------#

nbFr2=Frame(nb)

nbFr2_L1=Label(nbFr2, text='Enter Server URLs (Delete)')
nbFr2_L1.grid(row=0, column=1, padx=5, pady=5, sticky="w")


nbFr1_L1=Label(nbFr2, text='Enter Seat Number')
nbFr1_L1.grid(row=1, column=1, padx=5, pady=5, sticky="w")

nbFr2_L1=Label(nbFr2, text='Enter Name')
nbFr2_L1.grid(row=2, column=1, padx=5, pady=5, sticky="w")

nbFr2_L1=Label(nbFr2, text='Enter Status')
nbFr2_L1.grid(row=3, column=1, padx=5, pady=5, sticky="w")


nbFr2_ent0=ttk.Entry(nbFr2, width="55")
nbFr2_ent0.grid(row=0, column=2, sticky="w")

nbFr2_ent1=ttk.Entry(nbFr2)
nbFr2_ent1.grid(row=1, column=2, sticky="w")

nbFr2_ent2=ttk.Entry(nbFr2)
nbFr2_ent2.grid(row=2, column=2, sticky="w")

nbFr2_ent3=ttk.Entry(nbFr2)
nbFr2_ent3.grid(row=3, column=2, sticky="w")

nbFr2_btn1=ttk.Button(nbFr2, text="Delete", command=delete)
nbFr2_btn1.grid(row=4, column=1, pady=10)

nbFr2_btn2=ttk.Button(nbFr2, text="All Clear", command=clear)
nbFr2_btn2.grid(row=4, column=2, pady=10)

nbFr2.pack()

#-------------------3nd fram-----------------------#




nbFr3=Frame(nb)

nbFr3_L1=Label(nbFr3, text='Enter Server URLs (Update)')
nbFr3_L1.grid(row=0, column=1, padx=5, pady=5, sticky="w")

nbFr3_L1=Label(nbFr3, text='Enter Existing Seat Number')
nbFr3_L1.grid(row=1, column=1, padx=5, pady=5, sticky="w")

nbFr3_L1=Label(nbFr3, text='Enter Existing Name')
nbFr3_L1.grid(row=2, column=1, padx=5, pady=5, sticky="w")

nbFr3_L1=Label(nbFr3, text='Enter Existing Status')
nbFr3_L1.grid(row=3, column=1, padx=5, pady=5, sticky="w")

nbFr3_L1=Label(nbFr3, text='Enter Update Seat Number')
nbFr3_L1.grid(row=1, column=3, padx=5, pady=5, sticky="w")

nbFr3_L1=Label(nbFr3, text='Enter Update Name')
nbFr3_L1.grid(row=2, column=3, padx=5, pady=5, sticky="w")

nbFr3_L1=Label(nbFr3, text='Enter Update Status')
nbFr3_L1.grid(row=3, column=3, padx=5, pady=5, sticky="w")






nbFr3_ent0=ttk.Entry(nbFr3, width="55")
nbFr3_ent0.grid(row=0, column=2, sticky="w")


nbFr3_ent1=ttk.Entry(nbFr3)
nbFr3_ent1.grid(row=1, column=2, sticky="w")


nbFr3_ent2=ttk.Entry(nbFr3)
nbFr3_ent2.grid(row=2, column=2, sticky="w")


nbFr3_ent3=ttk.Entry(nbFr3)
nbFr3_ent3.grid(row=3, column=2, sticky="w")


nbFr3_ent4=ttk.Entry(nbFr3)
nbFr3_ent4.grid(row=1, column=4, sticky="w")


nbFr3_ent5=ttk.Entry(nbFr3)
nbFr3_ent5.grid(row=2, column=4, sticky="w")


nbFr3_ent6=ttk.Entry(nbFr3)
nbFr3_ent6.grid(row=3, column=4, sticky="w")





nbFr3_btn1=ttk.Button(nbFr3, text="Update", command=update)
nbFr3_btn1.grid(row=4, column=1, pady=10)

nbFr3_btn2=ttk.Button(nbFr3, text="All Clear", command=clear)
nbFr3_btn2.grid(row=4, column=2, pady=10)

nbFr3.pack()

#-----------------NoteBooke Tab-----------------#

nb.add(nbFr1, text="Insert")
nb.add(nbFr2, text="Delete")
nb.add(nbFr3, text="Update")

nb.pack()

scbr1=ttk.Scrollbar(lfFr2, orient='vertical')
scbr1.pack(side="right", fill='y')

cols=['Seat Number', 'Name', 'Status']

tv=ttk.Treeview(lfFr2, height=15, column=cols, show="headings", yscrollcommand=scbr1.set)

tv.heading('#0')
tv.heading('Seat Number', text="Seat Number")
tv.heading('Name', text="Name")
tv.heading('Status', text="Status")




scbr1.config(command=tv.yview)

tv.pack()




root.mainloop()





