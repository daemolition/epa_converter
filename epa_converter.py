# Standard library
import os

# Third party
import sys
import pandas as pd
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, 
    QVBoxLayout, QFileDialog, QMessageBox, QMenuBar, QMenu, QComboBox, QTextEdit,
    QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


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
        self.setFixedHeight(250)

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
        
        layout.addSpacerItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )
       
        # SelectField (Combobox)
        self.combo = QComboBox()        
        self.combo.currentTextChanged.connect(self.on_selection_changed)
        layout.addWidget(self.combo)
        
        layout.addSpacerItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )
        
        self.string_font = QFont()
        self.string_font.setPointSize(10)
        self.string_label = QTextEdit("Noch nichts ausgewählt")
        self.string_label.setReadOnly(True) 
        self.string_label.setViewportMargins(0, 25, 0, 25)
        self.string_label.setFont(self.string_font) 
        layout.addWidget(self.string_label)
        
        developer_font = QFont()
        developer_font.setPointSize(8)
        self.developer_label = QLabel("Developed by Christopher Abanilla @ 2025")
        self.developer_label.setWordWrap(True)
        self.developer_label.setAlignment(Qt.AlignCenter)
        self.developer_label.setFont(developer_font)
        layout.addWidget(self.developer_label)

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

        filtered_df = self.cleaned.loc[self.cleaned['Klarname'] == row['Klarname']]
        katalog, code = (
                filtered_df[['Katalog', 'CODE']].iloc[0].fillna('')
            )

        final_string = f"{katalog}{"," + code if code else ""},{row['Klarname']},XDS_CLASS_CODE#XDS_CONTENT_TYPE_CODE#XDS_FORMAT_CODE#COMPANYTYPE_20#XDS_TYPE_CODE#XDS_PRACTICE_SETTING_CODE#XDS_CONFIDENTIALY_CODE"

        return final_string
                
                
    def on_selection_changed(self, text):
        print(text)
        
        if hasattr(self, "cleaned") and not self.cleaned.empty:
            index = self.combo.currentIndex()
            if index > 0:
                text = self.cleaned.iloc[index]
                       
                self.string_label.setPlainText(f"{self.create_string(text)}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
