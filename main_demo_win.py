"""
This file is a demonstration on Windows.
You can run it without anythings,  of cause, you should install python at lease 3.7 (lol).
The fake data are on the file '.\Data'
lib: pandas
"""

from GUI_MainFrame import *
import random  # To create random date for resistance
import numpy as np
import pandas as pd
from time import sleep

# Excel Date ↓
# In fact, some data should be collected from hardware, however, by using the this file, the demo can running.
dateExcel = pd.read_excel('./Data/windSpeed_resistant.xlsx')


# Function of Choosing Mode
# can1st.option_add("*TCombobox*Listbox*Background", 'red')
ModeChoose_getText, ResistanceChoose_getText = 'Standard Resistant', ''       # Combobox default option
ResistantFilename = 'Data/..'   # The data file

def ModeChooseFunction(event):
    global ModeChoose_getText
    ModeChoose_getText = ModeChoose_Combobox_VariableIndex.get()
    ResistanceChoose_ComboboxID['value'] = ('Silver', 'Copper', "Iron", "Aluminium") \
        if ModeChoose_getText == 'Standard Resistant' \
        else ('Sample.NO.1', 'Sample.NO.2', "Sample.NO.3", "Sample.NO.4")
    # DateExcel=pd.read_excel()
    # print(ModeChoose_getText)
    ResistanceChoose_ComboboxID.current(0)
    FocusMoving_EnterFrame_ID.focus()

def ResistantChooseFunction(event):
    global ResistanceChoose_getText, ResistantFilename
    ResistanceChoose_getText = ResistantChoose_Combobox_VariableIndex.get()
    ResistantFilenameTemp = ResistantFilename + (ResistanceChoose_getText + '.xlsx')
    # print(ResistantFilenameTemp)
    # can1st.delete(resistantLine, averageLine)
    FocusMoving_EnterFrame_ID.focus()
    return 0

ModeChoose_Combobox_VariableIndex= tk.StringVar()
ModeChoose_ComboboxID = ttk.Combobox(can1st, state="readonly", textvariable=ModeChoose_Combobox_VariableIndex,
                                             justify=tk.CENTER, font=('Arial Black', 9),
                                             value=('Standard Resistant', 'Unknown Resistant'))

ModeChoose_ComboboxID.current(0)
ModeChoose_ComboboxID.bind("<<ComboboxSelected>>", ModeChooseFunction)
ModeChoose_ComboboxID.place(x=x_axisNum+63, y=ComboboxHeight+2)
# ----------------------------------------------------------------------------------------------------------------
ResistantChoose_Combobox_VariableIndex= tk.StringVar()
ResistanceChoose_ComboboxID = ttk.Combobox(can1st, state="readonly", width=12,
                                           textvariable=ResistantChoose_Combobox_VariableIndex,
                                           justify=tk.CENTER, font=('Arial Black', 10),
                                           value=('Silver', 'Copper', "Iron", "Aluminium"))
# ResistanceChoose_ComboboxID.current(0)

ResistanceChoose_ComboboxID.bind("<<ComboboxSelected>>", ResistantChooseFunction)
ResistanceChoose_ComboboxID.place(x=x_axisNum+340, y=ComboboxHeight+2)

'''
--------------------------------------------------------------------------------------------------------------------
This is the part of the chart !!!!!!
'''
# file
WindSpeed_Standard = dateExcel.values[:, 0]; WindSpeed_Standard = WindSpeed_Standard.tolist()
Resistant_Standard = dateExcel.values[:, 1]; Resistant_Standard = Resistant_Standard.tolist()
Resistant_Interval = [0, 1, -1, 2, -2]

# coordinate
cor_xAxis, cor_yAxis, cor_Length, cor_High, coordinate_Resistant_IndexMap = x_axisNum+30 , y_axisMax-35, x_axisMax*0.6, y_axisMax*0.75, 1
can1st.create_line(cor_xAxis, cor_yAxis, cor_xAxis, cor_yAxis - cor_High, fill=f'{can1st_line_color1st}',
                   arrow=tk.LAST, width=3)
can1st.create_line(cor_xAxis, cor_yAxis, cor_xAxis + cor_Length, cor_yAxis, fill=f'{can1st_line_color1st}',
                   arrow=tk.LAST, width=3)

# chart draw
resistantList = [random.randint(70, 230)+random.randint(0,40)]

chartShowSpeed = 0.1
chartSteep, chartResistantCounterMax = 79, 3       # Actually the true steep is 100 !!!!
tll = np.linspace(cor_xAxis, cor_xAxis+cor_Length, chartSteep+1, dtype=int, endpoint=True)
tll = tll.tolist()
chartResistantSummation = resistantList[0]
chartResistantAverage, chartResistantCounter = 0, 1
resistantLine = can1st.create_line(1, 1, 2, 2, fill='#ee3f4d', width=1)
averageLine=can1st.create_line(cor_xAxis, cor_yAxis - 200, cor_xAxis + cor_Length, cor_yAxis - 200, fill='#15559a', dash=7, width=5)
newlist = [tll[0], int(cor_yAxis-resistantList[0]*coordinate_Resistant_IndexMap)]

while 1:
    if ModeChoose_getText == 'Standard Resistant':
        can1st.delete(resistantLine, averageLine)
        sleep(chartShowSpeed)
        if ResistanceChoose_getText != '':
            if times < chartSteep:
                times += 1
                resistantList += [random.randint(75, 200) + random.randint(0, 40)]
                if chartResistantCounter < chartResistantCounterMax:
                    chartResistantSummation += resistantList[times]
                    chartResistantCounter += 1
                    chartResistantAverage = chartResistantSummation / (chartResistantCounter)
                else:
                    chartResistantSummation -= resistantList[times - chartResistantCounterMax]
                    chartResistantSummation += resistantList[times]
                    chartResistantAverage = chartResistantSummation / (chartResistantCounter)
                newlist += [tll[times], int(cor_yAxis - resistantList[times] * coordinate_Resistant_IndexMap)]
                # print("chartResistantSummation", chartResistantSummation)
                # print("chartResistantAverage",chartResistantAverage)
                # print("chartResistantCounter", chartResistantCounter)
            else:
                newlist = []
                del resistantList[0]
                resistantList += [random.randint(250, 280) + random.randint(0, 40)]
                chartResistantSummation = chartResistantSummation - resistantList[times - chartResistantCounterMax] + \
                                          resistantList[times]
                chartResistantAverage = chartResistantSummation / chartResistantCounter
                for i in range(times + 1):
                    newlist += [tll[i], int(cor_yAxis - resistantList[i] * coordinate_Resistant_IndexMap)]
                # print("newlist22=", newlist)
                # print("chartResistantSummation", chartResistantSummatpipion)
                # print("chartResistantAverage", chartResistantAverage)
                # print("chartResistantCounter", chartResistantCounter)
            for i in Resistant_Interval:
                try:
                    tempNumber = Resistant_Standard.index(int(chartResistantAverage) + i)
                    can1st.itemconfigure(can1st_text_Speed, text=f'{WindSpeed_Standard[tempNumber]}', fill="#fba414")
                    break
                except ValueError:
                    if i == Resistant_Interval[-1]:
                        can1st.itemconfigure(can1st_text_Speed, text=f'None Date', fill='Red', font=(f'{can1st_text_font_main}', 20))
                    else:
                        pass
            averageLine = can1st.create_line(cor_xAxis,
                                             int(cor_yAxis - chartResistantAverage * coordinate_Resistant_IndexMap),
                                             cor_xAxis + cor_Length,
                                             int(cor_yAxis - chartResistantAverage * coordinate_Resistant_IndexMap),
                                             fill='#bec936', dash=3)
            resistantLine = can1st.create_line(newlist, fill='#869d9d', width=1.3)
            can1st.itemconfigure(can1st_text_Resistant, text=f'{resistantList[times]}')
        mainDraw.update_idletasks()
        mainDraw.update()

    if ModeChoose_getText == 'Unknown Resistant':
        can1st.delete(resistantLine, averageLine)
        sleep(chartShowSpeed)
        print('Unknown Resistant Mode')
        mainDraw.update_idletasks()
        mainDraw.update()


mainDraw.mainloop()