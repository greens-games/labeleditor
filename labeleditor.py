from os import system
from tkinter import *
import xml.etree.ElementTree as ET

#stuff from tkinter
#buttons
#entry for input from user
#drop down or radio button for categories
#different windows for creating, deleting, updating, and home menu


#for any given item the elements in it and their appropriate indices are as follows:
#Caption = 0, 

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


def delete_label(item_to_delete):
    return

def create_label(name, cat, message, expire):
    new_item = ET.fromstring(item_string) #base new item object
    for elem in new_item:
        if elem.tag == 'Caption':
            elem.text = name

        if elem.tag == 'AssignedCategory':
            elem.text = cat

        if elem.tag == 'Caption_Alt1':
            elem.text = name

        if elem.tag == 'Print_Message':
            elem.text = message

        if elem.tag == 'Expire1_Message':
            elem.text = 'Date'

        if elem.tag == 'Expire1_Days':
            elem.text = '0'

        if elem.tag == 'Expire2_Message':
            elem.text = 'Use By'

        if elem.tag == 'Expire2_Days':
            elem.text = expire
    return new_item