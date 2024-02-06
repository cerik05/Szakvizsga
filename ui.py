from service import Service
import PySimpleGUI as sg


class Ui():
    def __init__(self):
        self.service = Service()
    def run(self):
        main_layout = [
            [sg.Text("Choose user ")],
            [sg.Button("Applicant", key="1"), sg.Button("Admin", key="2"), sg.Button("Exit", key="0")]
        ]
        applicant_layout = [
            [sg.Text("Choose command:")],
            [sg.Listbox(
                values=["1. Job list", "2. Apply for a job", "3. Highest paying jobs with lowest year requirement",
                        "0. Exit"], size=(40, 4), key="-LIST-", enable_events=True)],
            [sg.Button("OK"), sg.Button("Back")],
            [sg.Output(size=(40, 10))]
        ]
        admin_layout = [
            [sg.Text("Choose command:")],
            [sg.Listbox(values=["1. New job", "2. Remove a job", "3. Job list", "4. Inspecting a specific department",
                                "5. Applicants in a specific job", "0. Exit"], size=(40, 6), key="-LIST-", enable_events=True)],
            [sg.Button("OK"), sg.Button("Back")],
            [sg.Output(size=(40, 10))]
        ]
        main_window = sg.Window("Main Window", main_layout, finalize=True)
        applicant_window = sg.Window("Applicant Window", applicant_layout, finalize=True)
        admin_window = sg.Window("Admin Window", admin_layout, finalize=True)
        applicant_window.hide()
        admin_window.hide()
        while True:
            event, values = main_window.read(timeout=100)
            if event in (None, "0", "Exit"):
                break
            elif event == "1":
                applicant_window.un_hide()
                main_window.hide()
                while True:
                    event, values = applicant_window.read(timeout=100)
                    if event in (None, "0", "Exit", "Back"):
                        break
                    elif event == "-LIST-":
                        command = values["-LIST-"][0][0]
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
                applicant_window.hide()
                main_window.un_hide()
            elif event == "2":
                admin_window.un_hide()
                main_window.hide()
                while True:
                    event, values = admin_window.read(timeout=100)
                    if event in (None, "0", "Exit", "Back"):
                        break
                    elif event == "-LIST-":
                        command = values["-LIST-"][0][0]
                        if command == "1":
                            self.service.add_job()
                        elif command == "2":
                            self.service.remove_job()
                        elif command == "3":
                            for job in self.service.getjoblist():
                                print(str(job))
                        elif command == "4":
                            for job in self.service.specific_jobs():
                                print(str(job))
                        elif command == "5":
                            for applicant in self.service.job_applicants():
                                print(str(applicant))
                admin_window.hide()
                main_window.un_hide()
        main_window.close()
        applicant_window.close()
        admin_window.close()
new_ui = Ui()
new_ui.run()
