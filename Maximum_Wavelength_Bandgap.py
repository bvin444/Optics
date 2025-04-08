# This is code to evaluate the bandgap of a material and its absorption spectrum

import PySimpleGUI as sg


class Bandgap:

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

    def create_main_window(self):
        
        main_Frame = sg.Frame("BandGap",
                [
                    [sg.Text("Please enter the bandgap of your material"), sg.Input("", key = "BANDGAP")],
                    [sg.Text("The maximum wavelength your material can absorb is: "), sg.Input("", size = (10, 10), disabled_readonly_background_color='white', readonly = True, key = "MAXIMUM_WAVELENGTH")],
                    [sg.Button("Submit", key = "SUBMIT"), sg.Button("Exit", key = "EXIT")]
                ])
        
        layout = [[main_Frame]]
        return sg.Window("Bandgap", layout, resizable = True)

    def bandgap_Calculation(self):

        Answer = 1.24 / self.numerical_Array["BANDGAP"]
        self.window["MAXIMUM_WAVELENGTH"].update(f"{round(Answer,2)} (um)")
    
    def input_Validation(self, *args, values):

        for test_Input in args:
            print(values[test_Input])
            if values[test_Input] == '':

                sg.popup("Input cannot be blank!")
                return True
            
        try:
            
            float(values[test_Input])

        except:

            sg.popup("Input must be a numeric")
            return True
        
        self.numerical_Array = {key : float(values[key]) for key in args}

if __name__ == "__main__":

    Executable = Bandgap()
    