# Standard library
import os

# Third party
import sys
import pandas as pd
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QFileDialog, QMessageBox, QMenuBar, QMenu, QComboBox
)

from PySide6.QtCore import Qt


def clean_data(path):
    data = pd.read_csv(path, delimiter=",")
    new_data = data[["Katalog", "CODE", "Klarname"]].copy()
    return new_data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EPA String Generator")
        
        # Feste Fenserbreite
        self.setFixedWidth(500)
        self.setMinimumHeight(300)

        # --- Menübar ---
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Datei")

        open_action = file_menu.addAction("Datei öffnen")
        quit_action = file_menu.addAction("Quit")

        open_action.triggered.connect(self.on_open)
        quit_action.triggered.connect(self.close)

        # --- Zentrales Widget ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        
        self.filename_label = QLabel()  
        self.filename_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.filename_label)

       
        # SelectField (Combobox)
        self.combo = QComboBox()        
        self.combo.currentTextChanged.connect(self.on_selection_changed)
        layout.addWidget(self.combo)
        
        self.string_label = QLabel("Noch nichts ausgewählt")
        layout.addWidget(self.string_label)

        central_widget.setLayout(layout)

    def on_open(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "CSV-Datei öffnen", "", "CSV files (*.csv)"
        )
        if file_path:
            try:
                self.cleaned = clean_data(file_path)                
                
                # Dataframe auf Combobox setzen
                self.combo.clear()
                self.combo.addItems(self.cleaned['Klarname'].astype(str).to_list()) 
                
                # Filename setzen
                self.filename_label.setText(file_path)
                
            except Exception as e:
                QMessageBox.critical(self, "Fehler", f"Kann Datei nicht laden: {e}")
                
                
    def create_string(self, row: str):
        return f"{row['Katalog']}{"_" + row['CODE'] if row['CODE'] else "_"}_{row['Klarname']}"
                
                
    def on_selection_changed(self, text):
        print(text)
        
        if hasattr(self, "cleaned") and not self.cleaned.empty:
            index = self.combo.currentIndex()
            if index > 0:
                text = self.cleaned.iloc[index]
                       
                self.string_label.setText(f"{self.create_string(text)}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
