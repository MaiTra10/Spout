import sys
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Signal, Qt
from ui_form import Ui_Widget
from ui_dialog import Ui_Dialog
sys.path.append('C:\\Users\\Ricky\\Documents\\Local Programs\\Spout-1\\API')
from WeatherChecker import WeatherChecker
from sprinkler import post_handler, main

index = int(0)

class CustomDialog(QDialog, Ui_Dialog):
    dataEntered = Signal(str, str)  # Add a signal to pass data

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect the OK button to a custom slot
        self.buttonBox.accepted.connect(self.handle_ok_button)


    def handle_ok_button(self):
        # Get the entered data
        data1 = self.lineEdit.text()
        data2 = self.lineEdit_2.text()

        # Check if both data fields are non-empty
        if data1 and data2:
            # Emit the signal with the entered data
            self.dataEntered.emit(data1, data2)
            self.accept()

    def reset_dialog(self):
        # Clear the contents of the input fields or reset other properties
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        # Add any other reset logic as needed


class Widget(QWidget, Ui_Widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Connect buttons to functions
        self.newWindow.clicked.connect(self.show_popup)
        self.previousButton.clicked.connect(self.show_previous_page)
        self.nextButton.clicked.connect(self.show_next_page)

        # Connect the custom signal from the dialog to a slot in Widget
        self.dialog = CustomDialog()
        self.dialog.dataEntered.connect(self.handle_dialog_data)

    def show_popup(self):
        self.dialog.reset_dialog()  # Reset the dialog's state
        self.dialog.exec()

    def handle_dialog_data(self, data1, data2):
        # Create a new page with received data

#        data = {'function': 'add', 'id': index, 'name': str(data1), 'period': '0', 'seed_type': 3}


        reccomendation = "NULL"

        if WeatherChecker('ea2af1037f4540a4844235921231111') == True:
            reccomendation = "Rest easy, it will rain soon"

        else:
            reccomendation = "Your plants will appreciate being watered as usual"

        new_page = QWidget(self.stackedWidget)  # Access stackedWidget from Ui_Widget
        layout = QVBoxLayout(new_page)
        label1 = QLabel(f"Spout Connected: {data1}", new_page, alignment=Qt.AlignmentFlag.AlignTop)
        label2 = QLabel(f"Seed type: {data2}", new_page)
        label3 = QLabel("Status: Active", new_page)
        label4 = QLabel(f"{reccomendation}", new_page,  alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)S
        layout.addWidget(label4)


        # Add the new page to the stacked widget
        self.stackedWidget.addWidget(new_page)
#        index += 1

        # Set the current page to the newly added page
        self.stackedWidget.setCurrentWidget(new_page)

    def show_previous_page(self):
        # Show the previous page in the stackedWidget
        current_index = self.stackedWidget.currentIndex()
        total_pages = self.stackedWidget.count()

        if total_pages > 0:
            new_index = (current_index - 1) % total_pages
            self.stackedWidget.setCurrentIndex(new_index)

    def show_next_page(self):
        # Show the next page in the stackedWidget
        current_index = self.stackedWidget.currentIndex()
        total_pages = self.stackedWidget.count()

        if total_pages > 0:
            new_index = (current_index + 1) % total_pages
            self.stackedWidget.setCurrentIndex(new_index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())