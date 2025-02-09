# Deep-Translator - Real-time Language Translator
---------------------------------------------------

## Description
QT Translator is a real-time language translation application built using PyQt6 and GoogleTranslator from the `deep_translator` module. The application allows users to input text, select source and target languages, and view instant translations with a smooth and responsive UI.

## Features
- **Real-time translation** with a slight delay to prevent excessive API calls.
- **Auto-detect source language** option.
- **Beautiful light mode UI** with clean and modern styling.
- **Fixed screen size** (600x700) to maintain a structured layout.
- **Selectable languages** from a dropdown menu.
- **Smooth and responsive performance**.
- **Translate button** for manual translation if needed.

## Installation
1. Make sure you have Python installed.
2. Install the required dependencies by running:
   ```sh
   pip install PyQt6 deep-translator
   ```
3. Download or clone this repository.
4. Run the application using:
   ```sh
   python translator.py
   ```

## Usage
1. Launch the application.
2. Select the **source language** (or leave it on "Auto" for automatic detection).
3. Select the **target language**.
4. Type text into the input field; translation will occur in real time.
5. View the translated text in the output box.
6. Optionally, press the **Translate** button for manual translation.

## Dependencies
- Python 3.x
- PyQt6
- deep-translator

## Future Enhancements
- Dark mode toggle option.
- Voice input support.
- Text-to-speech for translated text.
- Multi-paragraph translations.

## Author
Created by **Vaibhav Pandey**.

