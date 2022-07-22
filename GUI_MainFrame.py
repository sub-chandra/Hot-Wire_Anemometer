"""
This is the Global Frame of the Program !
It includes global variable and the frame of the tkinter windows.
"""

import tkinter as tk
import tkinter.ttk as ttk

'''
    Global Variable and Style Setting
'''
# Window
x_axisMax, y_axisMax = 720, 405  # The size of the window. Choose this size because it's suitable for 7in Screen.
x_axisNum = 210  # The x coordinate of the line
# Coordinate of fixed Word
x_axisText_t, y_axisText_t = 94, 28    # The coordinate of the Words: "Wind Speed" "Resistant" "Temperature"
x_axisText_n, y_axisText_n = 183, 109  # The coordinate of the Unit: "mΩ"...
# On-time variable, such as the number of the resistant
x_axisVariable_text, y_axisVariable_text = x_axisNum*0.52, 75
distance_Variable_text = 135
# Coordinate of Combobox and Explanation words
ComboboxHeight, ComboboxHeight_distance = 9, 39
appendixPara = 80  # the distance between the appendix parameter and the right borad

# Fake Data, which should be collected by hardware.
Voltage, Current = 6.40, 0.039   # Current = 0.0057*Voltage + 0.0056
windSpeed, Resistant = 0, 0      # Speed = 0.3113*Voltage - 1.1234

# Font
can1st_text_font_main, can1st_text_color_main = 'Arial Black', "#fba414"  # the words: wind, resistant, temp
can1st_text_font_Size, can1st_number_font_Size = 16, 13  # size of word
can1st_mode_text_Size = 11  # size of the words: mode material
can1st_line_color1st = '#15559a'  # color of the line

# Other
tempNumber = 0  # Temporary variable
times = 0

'''
    Frame Setting
'''
# Main Frame of the Windows
mainDraw = tk.Tk()
mainDraw.geometry(f"{x_axisMax}x{y_axisMax}")
mainDraw.title("Hot-wire Anemometer")
mainDraw.update()

# Subsidiary Frame
# Creating a enter frame to move the focus
FocusMoving_EnterFrame_String = tk.StringVar()
FocusMoving_EnterFrame_ID = ttk.Entry(mainDraw, width=1, textvariable=FocusMoving_EnterFrame_String)
FocusMoving_EnterFrame_ID.place(x=9999, y=9999)  # Move the frame to (9999, 9999), so we hide it!

# Create a canvas
# relief options: flat, groove, raised, ridge, solid, or sunken
can1st = tk.Canvas(mainDraw, width=x_axisMax, height=y_axisMax, relief='groove', bd=6, bg="#0f1423")
can1st.pack()


'''
    Draw on can1st(canvas)
'''
# Frame Line
can1st.create_line(x_axisNum, 1,                        x_axisNum, y_axisMax, 1,
                   y_axisMax, 1, y_axisMax / 3 * 2,     x_axisNum, y_axisMax / 3 * 2,
                   x_axisNum, y_axisMax / 3, 1, y_axisMax / 3,
                   width=2, fill=f'{can1st_line_color1st}')
can1st.create_line(x_axisNum, y_axisMax * 0.095,        1024, y_axisMax * 0.095,
                   width=2, fill=f'{can1st_line_color1st}')

# Fixed Words
x_axisText_list = [x_axisText_t, x_axisText_n, x_axisText_t - 15, x_axisText_n,
                   x_axisText_t + 15, x_axisText_n, x_axisNum + 30, x_axisNum + 290,
                   x_axisMax - appendixPara, x_axisMax - appendixPara, x_axisMax - appendixPara + 65,
                   x_axisMax - appendixPara + 65, ]
y_axisText_list = [y_axisText_t, y_axisText_n, y_axisText_t + y_axisMax / 3 - 10,
                   y_axisText_n + y_axisMax / 3, y_axisText_t + y_axisMax / 3 * 2 - 10,
                   y_axisText_n + y_axisMax / 3 * 2, ComboboxHeight + 18, ComboboxHeight + 18,
                   ComboboxHeight + ComboboxHeight_distance, ComboboxHeight + ComboboxHeight_distance + 14,
                   ComboboxHeight + ComboboxHeight_distance, ComboboxHeight + ComboboxHeight_distance + 14]
FixedTextList = ["Wind Speed", "m/s", "Resistant", "mΩ", "Wind Temperature", "℃", "Mode:", "Material:",
                 "Re_Current:", "Wi_Current:", "A", "A"]
TextSize = [can1st_text_font_Size, can1st_number_font_Size, can1st_text_font_Size, can1st_number_font_Size,
            can1st_text_font_Size-3, can1st_number_font_Size, can1st_mode_text_Size, can1st_mode_text_Size,
            10, 10, 10, 10]
for i in range(0, len(x_axisText_list)):
    if TextSize[i] != 10:
        can1st.create_text(x_axisText_list[i], y_axisText_list[i], text=FixedTextList[i],
                       font=(f'{can1st_text_font_main}', TextSize[i]), fill=f'{can1st_text_color_main}')
    else:
        can1st.create_text(x_axisText_list[i], y_axisText_list[i], text=FixedTextList[i],
                           font=('new times roman', 10), fill=f'{can1st_text_color_main}')

# variable text --- Fake Now
can1st_text_Speed = can1st.create_text(x_axisVariable_text, y_axisVariable_text, text='', font=(f'{can1st_text_font_main}', 28), fill=f'{can1st_text_color_main}')
can1st_text_Resistant = can1st.create_text(x_axisVariable_text, y_axisVariable_text + distance_Variable_text, text='', font=(f'{can1st_text_font_main}', 28), fill=f'{can1st_text_color_main}')
can1st_text_Temperature = can1st.create_text(x_axisVariable_text, y_axisVariable_text + distance_Variable_text * 2, text='0', font=(f'{can1st_text_font_main}', 28), fill=f'{can1st_text_color_main}')
can1st_text_ResistantCurrent = can1st.create_text(x_axisMax - appendixPara + 50, ComboboxHeight + ComboboxHeight_distance, text="---", font=('DIN', 8), fill=f'{can1st_text_color_main}')
can1st_text_WindCurrent = can1st.create_text(x_axisMax - appendixPara + 50, ComboboxHeight + ComboboxHeight_distance + 14, text="459", font=('DIN', 8), fill=f'{can1st_text_color_main}')








"""
Test Part  !!!!!!!!!!!!!!!!!!
Remember to delete  !!!!!!!!!!!!!!!!
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ 

"""
# for i in range(1,4):
#     can1st.create_text((i + 2) * 20, (i + 2) * 20, text=f"{i}", font=(f'{can1st_text_font_main}', can1st_text_font_Size), fill=f'{can1st_text_color_main}')

