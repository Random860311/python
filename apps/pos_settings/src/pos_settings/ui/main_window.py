from PySide6.QtWidgets import QMainWindow

from pos_settings.ui.generated.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect button clicks to your methods
        # self.ui.myButton.clicked.connect(self.on_my_button_clicked)

    # def on_my_button_clicked(self):
    #     print("Clicked!")