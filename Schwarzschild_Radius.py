# This is code to calculate the Schwarzchild radius


import PySimpleGUI as sg
import numpy as np
from typing import ClassVar
from typing import Dict

class Schwarzschild:

    multiplier_DICTIONARY : ClassVar[Dict] = {"kg (10^3)": 10**3, "Mg (10^6)": 10**6, "Gg (10^9)": 10**9, "Tg (10^12)": 10**12, 
                                            "Pg (10^15)": 10**15, "Eg (10^18)": 10**18, "Zg (10^21)": 10**21, "Yg (10^24)": 10**24, "Rg (10^27)": 10**27, "Qg (10^30)": 10**30}

    def __init__(self):
        
        self.main()
    
    def main(self):

        self.window = self.create_main_window()

        while True:

            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, "EXIT"): break

            elif event == "SUBMIT":

                if self.input_Validation("MASS", values = values): continue
                self.Schwarzschild_Calculation(values)
            
            elif event == "UNIT_CHANGE":
                
                self.unit_Change(values)
    
    def create_main_window(self):

        Schwarzschild_Frame = sg.Frame("Schwarzschild Calculation",
                
                [ #
                    [sg.Text("The gravitational constant is: 6.674 * 10 ^-11 m^3 kg^-1 s^-2 "), sg.Text("The speed of light is: 8.0*10^9 (m / s)")],
                    [sg.Text("Please enter the mass of your object (kg)"), sg.Input("", key = "MASS"), sg.Text("Choose multiplier"), 
                    sg.Combo(list(Schwarzschild.multiplier_DICTIONARY), enable_events = True, default_value = "kg", key = "MULTIPLY")],
                    [sg.Text("The Schwarzschild radius of your object is (mm):", key = "OUTPUT_TEXT"), sg.Input("", key = "S_OUTPUT"), sg.Button("Unit Change", key = "UNIT_CHANGE")],
                    [sg.Button("Submit", key = "SUBMIT"), sg.Button("Exit", key = "EXIT")]
                ])
        
        layout = [[Schwarzschild_Frame]]

        return sg.Window("Schwarschild calculation", layout, resizable = True)
    
    def Schwarzschild_Calculation(self, values):

        Mass = self.frame_Values["MASS"]*Schwarzschild.multiplier_DICTIONARY[values["MULTIPLY"]]
        c = 3 * (10**8)
        G = 6.674 * 10 ** -11 
        self.Answerrr = (2*G*Mass/(c ** 2))
        self.window["S_OUTPUT"].update(f"{round(self.Answerrr*1000, 3)}")

    def unit_Change(self, values):

        try:

            float(values["S_OUTPUT"])
            
        except:

            sg.popup("Please enter a mass and press submit first")
            return

        update = float(values["S_OUTPUT"]) / (10**6)
        self.window["OUTPUT_TEXT"].update("The Schwarzschild radius of your object is (km):")
        self.window["S_OUTPUT"].update(f"{round(update, 3)}")

    def input_Validation(self, *args, values):

        for test_Input in args:
            if values[test_Input] == '':
                sg.popup("Input cannot be blank!")
                return True
            try:
                float(values[test_Input])
            except:
                sg.popup("Input must be a numerical value")
                return True
        self.frame_Values = {key : float(values[key]) for key in args}

if __name__ == "__main__":

    Excutable = Schwarzschild()
