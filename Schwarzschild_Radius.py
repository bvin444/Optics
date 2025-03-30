# This is code to calculate the Schwarzchild radius


import PySimpleGUI as sg
import numpy as np
from typing import ClassVar

class Schwarzschild:

    def __init__(self):
        
        self.main()
    
    def main(self):

        self.window = self.create_main_window()

        while True:

            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, "EXIT"): break

            elif event == "SUBMIT":

                if self.input_Validation("MASS", values = values): continue
                self.Schwarzschild_Calculation()
    
    def create_main_window(self):

        Schwarzschild_Frame = sg.Frame("Schwarzschild Calculation",
                
                [ #
                    [sg.Text("The gravitational constant is: 6.674 * 10 ^-11 m^3 kg^-1 s^-2 "), sg.Text("The speed of light is: 8.0*10^9 (m / s)")],
                    [sg.Text("Please enter the mass of your object"), sg.Input("", key = "MASS")],
                    [sg.Text("The Schwarzschild radius of your object is:"), sg.Input("", key = "S_OUTPUT")],
                    [sg.Button("Submit", key = "SUBMIT"), sg.Button("Exit", key = "EXIT")]
                ])
        
        layout = [[Schwarzschild_Frame]]

        return sg.Window("Schwarschild calculation", layout, resizable = True)
    
    def Schwarzschild_Calculation(self):

        Mass = self.frame_Values["MASS"]
        c = 3 * (10**8)
        G = 6.674 * 10 ** -11 
        self.Answerrr = (2*G*Mass/(c ** 2))
        self.window["S_OUTPUT"].update(f"{round(self.Answerrr, 2)}")

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
