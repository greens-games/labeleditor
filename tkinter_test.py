from tkinter import *
import xml.etree.ElementTree as ET
import labeleditor as editor

item_string = '''<Item>
            <Caption> </Caption>
            <AssignedCategory> </AssignedCategory>
            <Caption_Alt1> </Caption_Alt1>
            <Category_Alt1> </Category_Alt1>
            <Print_Message> </Print_Message>
            <Expire1_Message> </Expire1_Message>
            <Expire1_Days> </Expire1_Days>
            <Expire1_Hours> </Expire1_Hours>
            <Expire1_Mins> </Expire1_Mins>
            <Expire2_Message> </Expire2_Message>
            <Expire2_Days> </Expire2_Days>
            <Expire2_Hours> </Expire2_Hours>
            <Expire2_Mins> </Expire2_Mins>
            <Expire2_EOD> </Expire2_EOD>
            <Barcode> </Barcode>
            <Price> </Price>
            <Edit_Lock> </Edit_Lock>
            <Print_Button_Disable> </Print_Button_Disable>
            <Serving_Size> </Serving_Size>
            <Servings_Per_Container> </Servings_Per_Container>
            <Calories> </Calories>
            <Calories_From_Fat> </Calories_From_Fat>
            <Total_Fat_Percent> </Total_Fat_Percent>
            <Total_Fat_Grams> </Total_Fat_Grams>
            <Saturated_Percent> </Saturated_Percent>
            <Saturated_Fat_Grams> </Saturated_Fat_Grams>
            <Trans_Fat_Grams> </Trans_Fat_Grams>
            <Cholesterol_Percent> </Cholesterol_Percent>
            <Cholesterol_Grams> </Cholesterol_Grams>
            <Sodium_Percent> </Sodium_Percent>
            <Sodium_Grams> </Sodium_Grams>
            <Total_Carbs_Percent> </Total_Carbs_Percent>
            <Total_Carbs_Grams> </Total_Carbs_Grams>
            <Dietary_Fiber_Percent> </Dietary_Fiber_Percent>
            <Dietary_Fiber_Grams> </Dietary_Fiber_Grams>
            <Sugars_Grams> </Sugars_Grams>
            <Protein_Grams> </Protein_Grams>
            <Vitamin_A_Percent> </Vitamin_A_Percent>
            <Vitamin_C_Percent> </Vitamin_C_Percent>
            <Calcium_Percent> </Calcium_Percent>
            <Iron_Percent> </Iron_Percent>
            <Description1> </Description1>
            <Ingredients> </Ingredients>
        </Item>
        '''
    
tree_menu = ET.parse('MENUDATA.xml')
tree_user = ET.parse('USERDATA.xml')
root_menu = tree_menu.getroot()
root_user = tree_user.getroot()

new_item = ET.fromstring(item_string) #base new item object

labels_menu = root_menu.find('Labels')
items_menu = labels_menu.findall('Item')

labels_user = root_user.find('Labels')
items_user = labels_user.findall('Item')
# for label in items_user:
#     print(label.tag)
all_labels = list()
index = 0
for label in items_menu:
    text = label.find('Caption').text
    all_labels.append(text)
for label in items_user:
    text = label.find('Caption').text
    all_labels.append(text)
all_labels.sort()
# def create_label(new_item):

#     for i in new_item:
#         if i.tag == 'Caption':
#             i.text = caption

#         if i.tag == 'AssignedCategory':
#             i.text = input('Enter Category ')

#         if i.tag == 'Caption_Alt1':
#             i.text = caption

#         if i.tag == 'Print_Message':
#             i.text = input('Enter Message ')

#         if i.tag == 'Expire1_Message':
#             i.text = 'Date'

#         if i.tag == 'Expire1_Days':
#             i.text = '0'

#         if i.tag == 'Expire2_Message':
#             i.text = 'Use By'

#         if i.tag == 'Expire2_Days':
#             i.text = input('Enter Expire end day ')

#     return

class HomeWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.frame = Frame(self.master)
        btn = Button(self.master, text="Create Label", command= lambda: self.create_label_button(CreateLabelWindow))
        btn2 = Button(self.master, text="Delete Label", command= lambda: self.create_label_button(DeleteLabelWindow))
        self.frame.pack()
        btn.pack()
        btn2.pack()

    def create_label_button(self, _class):
        self.new = Toplevel(self.master)
        _class(self.new)

class CreateLabelWindow:
    def __init__(self,master):
        self.master = master
        self.master.geometry("600x400+200+200")
        self.frame = Frame(self.master)
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
        created_label = editor.create_label(self.item_name.get(),self.radio_var.get(),self.message.get(),self.expiry.get())
        labels_menu.append(created_label)
        updated_xml = ET.tostring(root_menu)
        with open("new_xml.xml","wb") as test_file:
            test_file.write(updated_xml)
        self.master.destroy()

class DeleteLabelWindow:
    def __init__(self,master):
        self.master = master
        self.master.geometry("600x400+200+200")
        self.master.configure(background="Gray")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master_frame = Frame(self.master,bg="Light Blue",  bd=3, relief=RIDGE)
        self.scroll_frame = Frame(self.master_frame, bg="Red")

        self.canvas = Canvas(self.scroll_frame, bg="Red")
        # self.button_canvas = Canvas(self.button_frame, bg="Yellow")

        self.button_frame = Frame(self.canvas, bg="Yellow", bd=2)
        self.scrollbar = Scrollbar(self.scroll_frame, orient=VERTICAL, command=self.canvas.yview)

        self.btns = []
        i=0
        # self.new_btn = Button(self.button_frame,text="Hello")
        # self.new_btn1 = Button(self.button_frame,text="Hello1")
        # self.new_btn2 = Button(self.button_frame,text="Hello2")

        self.master_frame.grid(row=0,column=0,sticky='nsew')
        self.scroll_frame.grid(row=0,column=1,sticky='nw')
        self.canvas.grid(row=0,column=1,sticky='nsew')
        # self.button_canvas.grid(row=0,column=0,sticky='nsew')
        self.scrollbar.grid(row=0,column=2,sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.button_frame.grid(row=0,column=0,sticky='nw')
        while i < 10:
            self.btn = Button(self.button_frame,text="Yo"+str(i))
            self.btn.grid(row=i,column=0,sticky='nsew')
            i = i + 1
        # self.new_btn.grid(row=0,column=0,sticky='nsew')
        # self.new_btn1.grid(row=1,column=0,sticky='nsew')
        # self.new_btn2.grid(row=2,column=0,sticky='nsew')
        #list all labels as radio buttons
        # 
        # self.button_canvas = Canvas(self.button_frame)
        # self.scrollbar = Scrollbar(self.scroll_frame, orient='vertical', command=self.canvas.yview)
        # self.create_radio_buttons()
        # self.canvas.create_window((0,0),window=self.button_frame,anchor=NW)
        # self.master_frame.grid(row=0,column=0,sticky='nsew')
        # self.scrollbar.grid(row=0,column=1,sticky='ns')
        # self.canvas.grid(row=0,column=1,sticky='nsew')
        # self.button_canvas.grid(row=0,column=0,sticky='nsew')
        # self.button_frame.grid(sticky='nsew')
        # self.scroll_frame.grid(sticky='nsew')
        # self.create_radio_buttons_grid()


    def create_radio_buttons(self):
        self.radio_buttons = []
        self.radio_var = StringVar(value="0")
        for item in all_labels:
            self.radio_buttons.append(Radiobutton(self.button_frame, text=item, value=item, variable=self.radio_var))

    def create_radio_buttons_grid(self):
        #we got 5 columns then add 1 to the row reset column index
        row_num = 0
        col_num = 0
        radio_button_index = 0
        while radio_button_index < len(self.radio_buttons)-1:
            while col_num < 5:
                self.radio_buttons[radio_button_index].grid(row=row_num, column=col_num)
                radio_button_index = radio_button_index + 1
                print(radio_button_index)
                col_num = col_num + 1

            radio_button_index = radio_button_index + 1
            row_num = row_num + 1
            col_num = 0
            print(radio_button_index)
root = Tk()
home = HomeWindow(master=root)
root.mainloop()


