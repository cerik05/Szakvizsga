from service import Service
import PySimpleGUI as sg


class Ui():
    def __init__(self):
        self.service = Service()

    def run(self):
        # Create the layout for the main window
        main_layout = [
            [sg.Text("Choose user (0 to exit, 1 for Applicant, 2 for Admin)")],
            [sg.Button("Applicant", key="1"), sg.Button("Admin", key="2"), sg.Button("Exit", key="0")]
        ]

        # Create the layout for the Applicant window
        applicant_layout = [
            [sg.Text("Choose command:")],
            [sg.Listbox(
                values=["1. Job list", "2. Apply for a job", "3. Highest paying jobs with lowest year requirement",
                        "0. Exit"], size=(40, 4), key="-LIST-")],
            [sg.Button("OK"), sg.Button("Back")],
            [sg.Output(size=(40, 10))]
        ]

        # Create the layout for the Admin window
        admin_layout = [
            [sg.Text("Choose command:")],
            [sg.Listbox(values=["1. New job", "2. Remove a job", "3. Job list", "4. Inspecting a specific department",
                                "5. Applicants in a specific job", "0. Exit"], size=(40, 6), key="-LIST-")],
            [sg.Button("OK"), sg.Button("Back")],
            [sg.Output(size=(40, 10))]
        ]

        # Create the window object for the main window
        main_window = sg.Window("Main Window", main_layout)

        # Create the window object for the Applicant window
        applicant_window = sg.Window("Applicant Window", applicant_layout)

        # Create the window object for the Admin window
        admin_window = sg.Window("Admin Window", admin_layout)

        # Hide the Applicant and Admin windows initially
        applicant_window.hide()
        admin_window.hide()

        # Use a while loop to read the events and values from the main window
        while True:
            event, values = main_window.read()
            # If the user chooses to exit, break the loop
            if event in (None, "0", "Exit"):
                break
            # If the user chooses Applicant, show the Applicant window and hide the main window
            elif event == "1":
                applicant_window.un_hide()
                main_window.hide()
                # Use a nested while loop to read the events and values from the Applicant window
                while True:
                    event, values = applicant_window.read()
                    # If the user chooses to exit or go back, break the loop and show the main window
                    if event in (None, "0", "Exit", "Back"):
                        break
                    # If the user chooses a command, execute it according to the logic of your program
                    elif event == "OK":
                        command = values["-LIST-"][0][0]  # Get the first character of the selected item
                        if command == "1":
                            for job in self.service.getjoblist():
                                print(str(job))
                        elif command == "2":
                            print("Insert your data")
                            self.service.applicant_information()
                        elif command == "3":
                            years = sg.popup_get_text("Choose experience years: ")
                            self.service.bubbleSort(self.service.getjoblist())
                            for job in self.service.getjoblist():
                                if job.get_years() < years:
                                    print(job)
                # Hide the Applicant window and show the main window
                applicant_window.hide()
                main_window.un_hide()
            # If the user chooses Admin, show the Admin window and hide the main window
            elif event == "2":
                admin_window.un_hide()
                main_window.hide()
                # Use a nested while loop to read the events and values from the Admin window
                while True:
                    event, values = admin_window.read()
                    # If the user chooses to exit or go back, break the loop and show the main window
                    if event in (None, "0", "Exit", "Back"):
                        break
                    # If the user chooses a command, execute it according to the logic of your program
                    elif event == "OK":
                        command = values["-LIST-"][0][0]  # Get the first character of the selected item
                        if command == "1":
                            self.service.add_job()
                        elif command == "2":
                            self.service.remove_job()
                        elif command == "3":
                            for job in self.service.getjoblist():
                                print(str(job))
                        elif command == "4":
                            self.service.specific_jobs()
                        elif command == "5":
                            self.service.job_applicants()
                # Hide the Admin window and show the main window
                admin_window.hide()
                main_window.un_hide()

        # Close the windows
        main_window.close()
        applicant_window.close()
        admin_window.close()


new_ui = Ui()
new_ui.run()
