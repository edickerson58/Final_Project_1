from PyQt5.QtWidgets import *
from final_view import *
import csv
import os.path


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_save.clicked.connect(lambda: self.save())
        self.button_clear.clicked.connect(lambda: self.clear())

    def save(self):
        try:
            user_input_file = self.input_file_input.text()
            user_output_file = self.output_file_input.text()

            header = ['Email', 'Subject', 'Confidence']
            data = []
            temp = []
            temp2 = [1, 1, 1]
            emails = []
            subjects = []
            confidences = []

            # reads input file and parses for correct information
            with open(f'files/{user_input_file}', 'r') as input_file:
                for line in input_file:
                    if line.startswith('From: '):
                        email = line.split()[1]
                        temp.append(email)
                    if line.startswith('Subject: '):
                        subject = line.split()[4]
                        temp.append(subject)
                    if line.startswith('X-DSPAM-Confidence: '):
                        confidence = line.split()[1]
                        temp.append(confidence)

            for email in temp[::3]:
                emails.append(email)
            for subject in temp[1::3]:
                subjects.append(subject)
            for confidence in temp[2::3]:
                confidences.append(confidence)

            for i, email in enumerate(emails):
                temp2[0] = email
                temp2[1] = subjects[i]
                temp2[2] = confidences[i]
                data.append(temp2[:])

            # checks radio buttons and outputs to file
            if self.radio_new.isChecked():
                if self.find_file(f'files/{user_output_file}'):
                    self.message_label.setText('File Already Exists')

                else:
                    with open(f'files/{user_output_file}', 'w', newline='') as file:
                        writer = csv.writer(file, delimiter='-')
                        writer.writerow(header)
                        writer.writerows(data)

                    self.message_label.setText('Data Stored')

            elif self.radio_overwrite.isChecked():
                with open(f'files/{user_output_file}', 'w', newline='') as file:
                    writer = csv.writer(file, delimiter='-')
                    writer.writerow(header)
                    writer.writerows(data)

                self.message_label.setText('Data Stored')
        except FileNotFoundError:
            self.message_label.setText('File Not Found')
        except:
            self.message_label.setText('Something Went Wrong')

    def clear(self):
        self.input_file_input.setText('')
        self.output_file_input.setText('')
        self.radio_new.setChecked(True)

    def find_file(self, file):
        if os.path.isfile(file):
            return True
        else:
            return False
