from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QComboBox, QLabel
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
from deep_translator import GoogleTranslator

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Deep Translator")
        self.setFixedSize(600, 700)

        # Light mode theme
        self.setStyleSheet("background-color: #f5f5f5; color: #333;")
        
        layout = QVBoxLayout()
        
        self.langs = GoogleTranslator().get_supported_languages()
        
        self.source_lang = QComboBox()
        self.source_lang.addItem("Auto", "auto")
        self.source_lang.addItems(self.langs)
        self.source_lang.setCurrentText("Auto")
        self.source_lang.setStyleSheet("background-color: white; color: #333; padding: 5px; border-radius: 5px;")
        layout.addWidget(QLabel("Source Language:"))
        layout.addWidget(self.source_lang)

        self.target_lang = QComboBox()
        self.target_lang.addItems(self.langs)
        self.target_lang.setCurrentText("english")
        self.target_lang.setStyleSheet("background-color: white; color: #333; padding: 5px; border-radius: 5px;")
        layout.addWidget(QLabel("Target Language:"))
        layout.addWidget(self.target_lang)
        
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type text here...")
        self.input_box.setStyleSheet("background-color: white; color: #333; padding: 10px; border: 1px solid #ccc; border-radius: 5px;")
        self.input_box.textChanged.connect(self.start_translation_timer)
        layout.addWidget(self.input_box)
        
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setStyleSheet("background-color: white; color: #333; padding: 10px; border: 1px solid #ccc; border-radius: 5px;")
        layout.addWidget(self.output_box)
        
        self.translate_button = QPushButton("Translate")
        self.translate_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px; font-weight: bold;")
        self.translate_button.clicked.connect(self.translate_text)
        layout.addWidget(self.translate_button)
        
        self.setLayout(layout)
        
        # Timer for real-time translation
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.translate_text)
    
    def start_translation_timer(self):
        self.timer.start(500)  # Delays translation by 500ms to avoid lag
    
    def translate_text(self):
        text = self.input_box.text()
        if not text.strip():
            self.output_box.clear()
            return
        
        src_lang = self.source_lang.currentData()
        tgt_lang = self.target_lang.currentText()
        
        try:
            translated_text = GoogleTranslator(source=src_lang, target=tgt_lang).translate(text)
            self.output_box.setPlainText(translated_text)
        except Exception as e:
            self.output_box.setPlainText("Translation Error: " + str(e))

if __name__ == "__main__":
    app = QApplication([])
    window = TranslatorApp()
    window.show()
    app.exec()
