from tkinter import *
import xml.etree.ElementTree as ET
import labeleditor as editor


class HomeWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x400")
        self.frame = Frame(self.master)
        btn = Button(self.master, text="Create Label", command= self.create_label_button)
        btn2 = Button(self.master, text="Update/Delete Label", command= self.delete_label_button)
        btn3 = Button(self.master, text="Quit", command= self.quit)
        self.frame.pack()
        self.load_xml()
        btn.pack()
        btn2.pack()
        btn3.pack()

    def create_label_button(self):
        self.load_xml()
        self.new = Toplevel(self.master)
        CreateLabelWindow(self.new,self.root_menu,self.labels_menu)

    def delete_label_button(self):
        self.load_xml()
        self.new = Toplevel(self.master)
        DeleteLabelWindow(self.new, self.root_menu, self.root_user, self.labels_menu, self.labels_user, self.all_labels)

        return

    def load_xml(self):
        print("updating xml")
        self.tree_menu = ET.parse('MENUDATA.xml')
        self.tree_user = ET.parse('USERDATA.xml')
        self.root_menu = self.tree_menu.getroot()
        self.root_user = self.tree_user.getroot()

        self.labels_menu = self.root_menu.find('Labels')
        self.items_menu = self.labels_menu.findall('Item')

        self.labels_user = self.root_user.find('Labels')
        self.items_user = self.labels_user.findall('Item')
        self.all_labels = dict()
        for label in self.items_menu:
            text = label.find('Caption').text
            self.all_labels[text] = editor.find_tags(label)
        for label in self.items_user:
            text = label.find('Caption').text
            self.all_labels[text] = editor.find_tags(label)

    def quit(self):
        self.master.destroy()

class CreateLabelWindow:
    def __init__(self,master,root_menu,labels_menu):
        self.master = master
        self.master.geometry("800x400")
        self.frame = Frame(self.master)
        self.root_menu = root_menu
        self.labels_menu = labels_menu
        self.create_widgets()
        self.create_grid()
        self.create_radio_buttons()
        self.create_radio_button_grid()
        self.frame.grid()
    
    def create_widgets(self):
        self.item_name_label = Label(self.master, text="Item Name")
        self.item_name = Entry(self.master, width=20)
        self.message_label = Label(self.master, text="Print Message")
        self.message = Entry(self.master, width=20)
        self.expiry_label = Label(self.master, text="Number of Days to Expire")
        self.expiry = Entry(self.master, width=20)
        self.btn = Button(self.master, text="submit", command=self.submit)

    def create_radio_buttons(self):
        self.radio_var = StringVar(value="0")
        self.category1 = Radiobutton(self.master, text="Bar / Bread", value="Bar / Bread", variable=self.radio_var)
        self.category2 = Radiobutton(self.master, text="Cheese / Dairy", value="Cheese / Dairy", variable=self.radio_var)
        self.category3 = Radiobutton(self.master, text="Chicken", value="Chicken", variable=self.radio_var)
        self.category4 = Radiobutton(self.master, text="Frozen", value="Frozen", variable=self.radio_var)
        self.category5 = Radiobutton(self.master, text="Fry / Sanitation", value="Fry / Sanitation", variable=self.radio_var)
        self.category6 = Radiobutton(self.master, text="Grocery", value="Grocery", variable=self.radio_var)
        self.category7 = Radiobutton(self.master, text="Meat", value="Meat", variable=self.radio_var)
        self.category8 = Radiobutton(self.master, text="Produce / Potato", value="Produce / Potato", variable=self.radio_var)
        self.category9 = Radiobutton(self.master, text="Sauces", value="Sauces", variable=self.radio_var)
        self.category10 = Radiobutton(self.master, text="Seafood", value="Seafood", variable=self.radio_var)

    def create_radio_button_grid(self):
        self.category1.grid(row=1,column=0)
        self.category2.grid(row=1,column=1)
        self.category3.grid(row=1,column=2)
        self.category4.grid(row=1,column=3)
        self.category5.grid(row=1,column=4)
        self.category6.grid(row=2,column=0)
        self.category7.grid(row=2,column=1)
        self.category8.grid(row=2,column=2)
        self.category9.grid(row=2,column=3)
        self.category10.grid(row=2,column=4)

    def create_grid(self):
        self.item_name.grid(row=0,column=1)
        self.item_name_label.grid(row=0,column=0)

        self.message_label.grid(row=3,column=0)
        self.message.grid(row=3,column=1)

        self.expiry_label.grid(row=4,column=0)
        self.expiry.grid(row=4,column=1)

        self.btn.grid(row=5,column=0)


    def submit(self):
        if self.item_name.get() == '' or self.radio_var.get() == '0' or self.message.get() == '' or self.expiry.get() == '':
            print("we have a blanker")
        else: 
            created_label = editor.create_label(self.item_name.get(),self.radio_var.get(),self.message.get(),self.expiry.get())
            self.labels_menu.append(created_label)
            updated_xml = ET.tostring(self.root_menu)
            with open("MENUDATA.xml","wb") as test_file:
                test_file.write(updated_xml)
        self.master.destroy()

class DeleteLabelWindow:
    def __init__(self,master, root_menu, root_user, labels_menu, labels_user, all_labels):
        self.master = master
        self.master.geometry("1240x640")
        self.master.configure(background="Gray")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.root_menu = root_menu
        self.root_user = root_user
        self.labels_menu = labels_menu
        self.labels_user = labels_user
        self.all_labels = all_labels

        self.master_frame = Frame(self.master,bg="Light Blue",  bd=3, relief=RIDGE)
        self.scroll_frame = Frame(self.master_frame)

        self.canvas = Canvas(self.scroll_frame)

        self.scrollbar = Scrollbar(self.scroll_frame, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.button_frame = Frame(self.canvas)

        self.master_frame.grid(row=0,column=0,sticky='nsew')
        self.scroll_frame.grid(row=0,column=5,sticky='nw')
        self.canvas.grid(row=0,column=5)
        self.scrollbar.grid(row=0,column=6,sticky='ns')

        self.create_radio_buttons()
        self.create_radio_buttons_grid()
        self.canvas.create_window((0,0), window=self.button_frame,anchor='nw')
        self.master_frame.bind("<Configure>",self.bindFunc)


    def bindFunc(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width= 1080,height=600)
    

    def create_radio_buttons(self):
        self.radio_buttons = []
        index = 0
        self.svars = []
        while index < len(self.all_labels):
            self.svars.append(StringVar(value='Nothing'))
            index = index + 1
        index = 0
        for item in sorted(self.all_labels):
            self.radio_buttons.append(Checkbutton(self.button_frame, text=item, onvalue=item, variable=self.svars[index]))
            index = index + 1

    def create_radio_buttons_grid(self):
        #we get 5 columns then add 1 to the row reset column index
        row_num = 0
        col_num = 0
        i = 0
        while i < len(self.radio_buttons):
            while i<len(self.radio_buttons) and col_num < 5:
                self.radio_buttons[i].grid(row=row_num, column=col_num, sticky='nsew')
                i = i + 1
                col_num = col_num + 1

            i = i + 1
            row_num = row_num + 1
            col_num = 0
        print(row_num)
        self.delete_btn = Button(self.button_frame, text='Delete', command=self.delete)
        self.update = Button(self.button_frame, text='Update', command=self.update)
        # self.update2 = Button(self.button_frame, text='Update2', command=self.update2)
        self.delete_btn.grid(row=row_num,column=3,sticky='nsew')
        self.update.grid(row=row_num,column=4,sticky='nsew')
        # self.update2.grid(row=row_num,column=2,sticky='nsew')


    def delete(self):
        items_list = []
        for item in self.svars:
            if item.get() != 'Nothing':
                items_list.append(item.get())
        editor.delete_label(self.labels_menu,self.labels_user,items_list)
        updated_xml = ET.tostring(self.root_menu)
        updated_user = ET.tostring(self.root_user)
        with open("MENUDATA.xml","wb") as test_file:
            test_file.write(updated_xml)
        with open("USERDATA.xml","wb") as test_file:
            test_file.write(updated_user)
        
        self.master.destroy()

    # def update(self):
    #     items_list = []
    #     for item in self.svars:
    #         if item.get() != 'Nothing':
    #             items_list.append(self.all_labels[item.get()])
        
    #     i = 0
    #     while i < 3:
    #         self.new = Toplevel(self.master)
    #         UpdateForm2(self.new, self.root_menu, self.root_user, self.labels_menu, self.labels_user, items_list[i])
    #         i += 1
    #     return

    def update(self):
        items_list = []
        for item in self.svars:
            if item.get() != 'Nothing':
                items_list.append(self.all_labels[item.get()])
        
        self.new = Toplevel(self.master)
        UpdateForm(self.new, self.root_menu, self.root_user, self.labels_menu, self.labels_user, items_list)
        return


    #, item_name, item_message, item_expire
class UpdateForm:
    def __init__(self,master,root_menu,root_user,labels_menu,labels_user,items_list):
        self.master = master
        self.master.geometry('1240x640')
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        #class variables
        self.root_menu = root_menu
        self.root_user = root_user
        self.labels_menu = labels_menu
        self.labels_user = labels_user
        self.items_list = items_list

        #scroll things
        self.master_frame = Frame(self.master,bg="Light Blue",  bd=3, relief=RIDGE)
        self.scroll_frame = Frame(self.master_frame)

        self.canvas = Canvas(self.scroll_frame)

        self.scrollbar = Scrollbar(self.scroll_frame, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.button_frame = Frame(self.canvas)
        self.index = 0
        self.frames = []
        self.radio_vars = []
        self.item_names = []
        self.messages = []
        self.expiries = []

        self.master_frame.grid(row=0,column=0,sticky='nsew')
        self.scroll_frame.grid(row=0,column=3,sticky='nw')
        self.canvas.grid(row=0,column=3)
        self.scrollbar.grid(row=0,column=4,sticky='ns')

        for item in self.items_list:
            self.frames.append(Frame(self.button_frame, bd=4, bg='Light Blue'))
            self.radio_vars.append(StringVar(value="0"))
            self.create_widgets(self.index,item)
            self.create_grid(self.index)
            self.create_radio_buttons(self.index,item)
            self.create_radio_button_grid(self.index)
            self.frames[self.index].grid()
            self.index += 1

        self.done_btn = Button(self.button_frame, text='Done', command=self.done)
        self.canvas.create_window((0,0), window=self.button_frame,anchor='nw')
        self.done_btn.grid(row=self.index, column=0, sticky='nsew')
        self.master_frame.bind("<Configure>",self.bindFunc)


    def bindFunc(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width= 1080,height=600)

    
    def create_widgets(self, index, item):
        self.item_name_label = Label(self.frames[index], text="Item Name", bg='Light Blue')
        self.item_names.append(Entry(self.frames[index], width=20, textvariable=StringVar(value=item[0])))
        self.message_label = Label(self.frames[index], text="Print Message", bg='Light Blue')
        self.messages.append(Entry(self.frames[index], width=20, textvariable=StringVar(value=item[3])))
        self.expiry_label = Label(self.frames[index], text="Number of Days to Expire", bg='Light Blue')
        self.expiries.append(Entry(self.frames[index], width=20, textvariable=StringVar(value=item[4])))
        self.btn = Button(self.frames[index], text="submit", command=self.submit)

    def create_radio_buttons(self, index, item):
        self.radio_vars[index] = StringVar(value=item[1])
        self.category1 = Radiobutton(self.frames[index], text="Bar / Bread", value="Bar / Bread", variable=self.radio_vars[index], bg='Light Blue')
        self.category2 = Radiobutton(self.frames[index], text="Cheese / Dairy", value="Cheese / Dairy", variable=self.radio_vars[index], bg='Light Blue')
        self.category3 = Radiobutton(self.frames[index], text="Chicken", value="Chicken", variable=self.radio_vars[index], bg='Light Blue')
        self.category4 = Radiobutton(self.frames[index], text="Frozen", value="Frozen", variable=self.radio_vars[index], bg='Light Blue')
        self.category5 = Radiobutton(self.frames[index], text="Fry / Sanitation", value="Fry / Sanitation", variable=self.radio_vars[index], bg='Light Blue')
        self.category6 = Radiobutton(self.frames[index], text="Grocery", value="Grocery", variable=self.radio_vars[index], bg='Light Blue')
        self.category7 = Radiobutton(self.frames[index], text="Meat", value="Meat", variable=self.radio_vars[index], bg='Light Blue')
        self.category8 = Radiobutton(self.frames[index], text="Produce / Potato", value="Produce / Potato", variable=self.radio_vars[index], bg='Light Blue')
        self.category9 = Radiobutton(self.frames[index], text="Sauces", value="Sauces", variable=self.radio_vars[index], bg='Light Blue')
        self.category10 = Radiobutton(self.frames[index], text="Seafood", value="Seafood", variable=self.radio_vars[index], bg='Light Blue')

    def create_radio_button_grid(self, index):
        self.category1.grid(row=index+1,column=0)
        self.category2.grid(row=index+1,column=1)
        self.category3.grid(row=index+1,column=2)
        self.category4.grid(row=index+1,column=3)
        self.category5.grid(row=index+1,column=4)
        self.category6.grid(row=index+2,column=0)
        self.category7.grid(row=index+2,column=1)
        self.category8.grid(row=index+2,column=2)
        self.category9.grid(row=index+2,column=3)
        self.category10.grid(row=index+2,column=4)

    def create_grid(self, index):
        self.item_names[index].grid(row=index,column=1)
        self.item_name_label.grid(row=index,column=0)

        self.message_label.grid(row=index+3,column=0)
        self.messages[index].grid(row=index+3,column=1)

        self.expiry_label.grid(row=index+4,column=0)
        self.expiries[index].grid(row=index+4,column=1)

        self.btn.grid(row=index+5,column=0)


    def submit(self):
        print(self.item_names[0].get())
        self.index = 0
        while self.index < len(self.items_list):
            self.items_list[self.index][0] = self.item_names[self.index].get()
            self.items_list[self.index][1] = self.radio_vars[self.index].get()
            self.items_list[self.index][2] = self.item_names[self.index].get()
            self.items_list[self.index][3] = self.messages[self.index].get()
            self.items_list[self.index][4] = self.expiries[self.index].get()
            self.index += 1
        print(self.items_list)
        # editor.update_label(self.labels_menu, self.labels_user, item_to_update, self.original_name)
        updated_xml = ET.tostring(self.root_menu)
        with open("MENUDATA.xml","wb") as test_file:
            test_file.write(updated_xml)
        

    def done(self):
        self.master.destroy()

# class UpdateForm2:
#     def __init__(self,master,root_menu, root_user, labels_menu, labels_user, item_to_update):
#         self.master = master
#         self.master.geometry('600x400')
#         self.master.lift()
#         self.frame = Frame(self.master)
#         self.root_menu = root_menu
#         self.root_user = root_user
#         self.labels_menu = labels_menu
#         self.labels_user = labels_user
#         self.item_to_update = item_to_update
#         self.original_name = item_to_update[0]
#         self.create_widgets()
#         self.create_grid()
#         self.create_radio_buttons()
#         self.create_radio_button_grid()
#         self.frame.grid()
    
#     def create_widgets(self):
#         self.item_name_label = Label(self.master, text="Item Name")
#         self.item_name = Entry(self.master, width=20, textvariable=StringVar(value=self.item_to_update[0]))
#         self.message_label = Label(self.master, text="Print Message")
#         self.message = Entry(self.master, width=20, textvariable=StringVar(value=self.item_to_update[3]))
#         self.expiry_label = Label(self.master, text="Number of Days to Expire")
#         self.expiry = Entry(self.master, width=20, textvariable=StringVar(value=self.item_to_update[4]))
#         self.btn = Button(self.master, text="submit", command=self.submit)

#     def create_radio_buttons(self):
#         self.radio_var = StringVar(value='0')
#         self.category1 = Radiobutton(self.master, text="Bar / Bread", value="Bar / Bread", variable=self.radio_var)
#         self.category2 = Radiobutton(self.master, text="Cheese / Dairy", value="Cheese / Dairy", variable=self.radio_var)
#         self.category3 = Radiobutton(self.master, text="Chicken", value="Chicken", variable=self.radio_var)
#         self.category4 = Radiobutton(self.master, text="Frozen", value="Frozen", variable=self.radio_var)
#         self.category5 = Radiobutton(self.master, text="Fry / Sanitation", value="Fry / Sanitation", variable=self.radio_var)
#         self.category6 = Radiobutton(self.master, text="Grocery", value="Grocery", variable=self.radio_var)
#         self.category7 = Radiobutton(self.master, text="Meat", value="Meat", variable=self.radio_var)
#         self.category8 = Radiobutton(self.master, text="Produce / Potato", value="Produce / Potato", variable=self.radio_var)
#         self.category9 = Radiobutton(self.master, text="Sauces", value="Sauces", variable=self.radio_var)
#         self.category10 = Radiobutton(self.master, text="Seafood", value="Seafood", variable=self.radio_var)

#     def create_radio_button_grid(self):
#         self.category1.grid(row=1,column=0)
#         self.category2.grid(row=1,column=1)
#         self.category3.grid(row=1,column=2)
#         self.category4.grid(row=1,column=3)
#         self.category5.grid(row=1,column=4)
#         self.category6.grid(row=2,column=0)
#         self.category7.grid(row=2,column=1)
#         self.category8.grid(row=2,column=2)
#         self.category9.grid(row=2,column=3)
#         self.category10.grid(row=2,column=4)

#     def create_grid(self):
#         self.item_name.grid(row=0,column=1)
#         self.item_name_label.grid(row=0,column=0)

#         self.message_label.grid(row=3,column=0)
#         self.message.grid(row=3,column=1)

#         self.expiry_label.grid(row=4,column=0)
#         self.expiry.grid(row=4,column=1)

#         self.btn.grid(row=5,column=0)



#     def submit(self):
#         self.item_to_update[0] = self.item_name.get()
#         self.item_to_update[1] = self.radio_var.get()
#         self.item_to_update[2] = self.item_name.get()
#         self.item_to_update[3] = self.message.get()
#         self.item_to_update[4] = self.expiry.get()
#         editor.update_label(self.labels_menu, self.labels_user, self.item_to_update, self.original_name)
            
#         updated_xml = ET.tostring(self.root_menu)
#         updated_user = ET.tostring(self.root_user)
#         with open("MENUDATA.xml","wb") as test_file:
#             test_file.write(updated_xml)
#         with open("USERDATA.xml","wb") as test_file:
#             test_file.write(updated_user)
#         self.master.destroy()
        

root = Tk()
# root.attributes('-fullscreen',True)
home = HomeWindow(master=root)
root.mainloop()


