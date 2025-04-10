# Libraries to Import
import PySimpleGUI as sg
from typing import ClassVar
from typing import Dict


class Bandgap:

    C : ClassVar[float] = 3 * (10 ** 8)
    multiplier_DICTIONARY : ClassVar[Dict] = {"kHz": 10**3, "MHz": 10**6, "GHz": 10**9, "THz": 10**12, "PHz": 10**15, "EHz": 10**18, "ZHz": 10**21}
    def __init__(self):

        self.main()
    
    def main(self):

        self.window = self.create_main_window()

        while True:

            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, "EXIT"): break
            elif event == "SUBMIT":
                if self.input_Validation("BANDGAP", values = values): continue
                self.bandgap_Calculation()
            elif event == "MULTIPLIER":
                if self.input_Validation("BANDGAP", values = values): continue
                self.update_Window(values)
                
    def create_main_window(self):
        
        main_Frame = sg.Frame("BandGap",
                [
                    [sg.Text("Please enter the bandgap of your material (eV)"), sg.Input("", key = "BANDGAP")],
                    [sg.Text("The maximum wavelength your material can absorb is (um): "), sg.Input("", size = (10, 10), disabled_readonly_background_color='white', readonly = True, key = "MAXIMUM_WAVELENGTH")],
                    [sg.Text("The mininum frequency your material can absorb is: "), sg.Input("", size = (20, 10), disabled_readonly_background_color='white', readonly = True, key = "MINIMUM_FREQUENCY"), sg.Combo(list(Bandgap.multiplier_DICTIONARY), enable_events = True, key = "MULTIPLIER")],
                    [sg.Button("Submit", key = "SUBMIT"), sg.Button("Exit", key = "EXIT")]
                ])
        
        layout = [[main_Frame]]
        return sg.Window("Bandgap", layout, resizable = True)

    def bandgap_Calculation(self):

        Wave = 1.24 / self.numerical_Array["BANDGAP"]
        self.Fre = Bandgap.C / (Wave * (10 ** (-6)))
        self.window["MAXIMUM_WAVELENGTH"].update(f"{round(Wave, 2)} (um)")
        self.window["MINIMUM_FREQUENCY"].update(f"{round(self.Fre, 2)}")

    def update_Window(self, values):

        new_Form = round(self.Fre / Bandgap.multiplier_DICTIONARY[values["MULTIPLIER"]], 5)
        self.window["MINIMUM_FREQUENCY"].update(f"{new_Form}")

    
    def input_Validation(self, *args, values):

        for test_Input in args:

            if values[test_Input] == '':

                sg.popup("Input cannot be blank!")
                self.window["MULTIPLIER"].update("")
                return True
            
            if values[test_Input] == '0':

                sg.popup("Input cannot be zero!")
                return True
            
        try:
            
            float(values[test_Input])

        except:

            sg.popup("Input must be a numeric")
            return True
        
        self.numerical_Array = {key : float(values[key]) for key in args}

if __name__ == "__main__":

    Executable = Bandgap()
    