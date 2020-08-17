from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import sqlite3
import os
import pandas as pd
import csv

root = Tk()
root.title('Routing')
root.geometry('400x400')

#Below is code essential to creating the database
today = date.today()
year = str(today)[0:4]
month = str(today)[5:7]
day = str(today)[8:10]
#dir_year = 'T:/Information Technology Drive/Automation/Routing' + '/' + year
#dir_month = 'T:/Information Technology Drive/Automation/Routing' + '/' + year + '/' + month
#dir_day = 'T:/Information Technology Drive/Automation/Routing' + '/' + year + '/' + month + '/' + day
#if not os.path.exists(dir_year):
#	os.mkdir(dir_year)
#if not os.path.exists(dir_month):
#	os.mkdir(dir_month)

#database = sqlite3.connect(str(dir_day) + '.db')
#c = database.cursor() 

#Frames
day_frame = Frame(root)
day_frame.grid(row=0, column=0)
routing_frame = Frame(root)
#routing_frame.grid(row=0, column=0)

#Instead of changing the windows, I will have code be inside frames, and we can change them in there 
welcome_label = Label(day_frame, text='Welcome to Northern Haserots Routing program. \n Please select the ship date.')
welcome_label.grid(row=0, column=0)

#this is the list used on the first frame
ship_days= [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday"
]

Mon_day_route_list = ["110","112","116","119","115","114","117","113","146",
						"145","121","103","104","105","107","120","108",
						"106","174","178","172","173","176","177","181","184",
						"170","186","144","101","102","127","125","130","141",
						"180","171","191","190","192","182","175","160","140",
						"193","194","195","169","179","144"]

Tues_day_route_list = ["235","232","233","236","238","234","242","237","239",
						"231","205","204","208","209","210","212","213","218",
						"253","254","294","296","201","202","221","203","252",
						"250","230","240","220","287","286","215","216","285",
						"292","260","265","245","280","255","290","270","219",
						"229","267","241","269"]

Wed_day_route_list = ["336","335","339","337","338","341","340","334","331",
						"332","308","309","307","306","305","304","314","313",
						"354","357","372","385","390","352","380","301","302",
						"303","345","353","330","350","351","371","393","325",
						"315","321","320","310","365","360","355","395","387",
						"344","346","347"]

Thurs_day_route_list = ["445","446","449","447","443","444","448","442","452",
						"441","405","404","403","406","408","409","415","414",
						"416","469","496","497","499","498","494","407","465",
						"410","401","402","450","417","476","430","451","490",
						"427","485","453","435","428","460","440","488","475",
						"493","420","495","470","468"]

Fri_day_route_list = ["540","541","542","543","544","546","549","539","547",
						"548","555","504","505","509","508","507","506","514",
						"519","527","516","552","556","521","522","545","520",
						"501","512","503","503","587","535","526","525","523",
						"592","550","551","585","589","590","570","530","515",
						"597","593","580","560","565","595", "598","594"]

day_selected = ttk.Combobox(day_frame, value=ship_days)
day_selected.current(0)
day_selected.grid(row=1, column=0)

#This function switches from the main frame to the routing frame
def P2():
	day_frame.grid_forget()
	routing_frame.grid(row=0, column=0)

#This function confirms the selection of the routing day selected
def choose_day_button():
	global response
	response = messagebox.askyesno('Confirm Day', 'You have selected ' + day_selected.get() +', is this the correct day?')
	#display_day_Confirm_deny=Label(root, text=str(response))
	#display_day_Confirm_deny.grid(row=3, column=0)
	
	if str(response) == 'True':
		P2()
	else:
		messagebox.showinfo('Incorrect day', 'Please select the correct day')

#This functions allows you to return to the main frame while in the routing frame
def day_return():
	routing_frame.grid_forget()
	day_frame.grid(row=1, column=0)

#this function begins the process of running routes
def run_routes():
	pass

#this function disables the checkboxes that are selected
def purge_routes():
	pass


day_selected_button = Button(day_frame, text="Select day", command=choose_day_button)
day_selected_button.grid(row=2, column=0)


#Below is the routes to be selected
select_routes_label = Label(routing_frame, text='Please check the routes you would like to route')
select_routes_label.grid(row=0, column=0, columnspan=5)

x=1
while x	< 51:
	route_var = str("RTV" + str(x))
	#t = str("RT" + str(x))
	t = Checkbutton(routing_frame, text=x + , variable=route_var, onvalue="R", offvalue="DR")
	t.deselect()
	
	#This if statement created the first column
	if x < 11:
		#col1 = 1
		t.grid(row=x + 2, column=1)
	#This if statement creates the second column
	if x < 21 and x > 10:
		#col2 = 3
		t.grid(row=x - 8, column=2)
	#This if statement creates the third column
	if x < 31 and x > 20:
		#col3 = 5
		t.grid(row=x - 18, column=3)
	#This if statement creates the fourth column
	if x < 41 and x > 30:
		#col4 = 7
		t.grid(row=x - 28, column=4)
	#This if statement creates the firth column
	if x < 51 and x > 40:
		#col5 = 9
		t.grid(row=x - 38, column=5)
	
	x += 1



Choose_routes_Button = Button(routing_frame, text="Run Routes", command=run_routes)
Choose_routes_Button.grid(row=14 ,column=2)

Purge_Route_Button = Button(routing_frame, text="Purge Routes", command=purge_routes)
Purge_Route_Button.grid(row=15 ,column=1)

return_to_day_select_button = Button(routing_frame, text='Change day', command=day_return)
return_to_day_select_button.grid(row=14, column=1)


day_selected_label = Label(routing_frame, text="You currently routing for " + day_selected.get())
day_selected_label.grid(row=17, column=1, columnspan=2)
#database.commit()
#database.close()
root.mainloop()