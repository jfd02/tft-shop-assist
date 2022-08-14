## TFT SHOP ASSIST

## NOTES:
Make sure you don't have any overlays on (Blitz, Mobalytics, etc.).
League & client must be in English.
16:9 resolution borderless windowed is required in League, the game must also be on the main monitor (Use 1920x1080 for best results).
If the program crashes, create an issue with the error.

## INSTALLATION:
1. Install Python 3.10.6 from https://www.python.org/downloads/windows/
   - Note that Python 3.10.6 cannot be used on Windows 7 or earlier.
2. Clone the repository or download it from here https://github.com/jfd02/TFT-OCR-BOT/archive/refs/heads/main.zip
3. Open Command Prompt and change the current directory to the folder where main.py is located 
4. Run pip install -r requirements.txt in Command Prompt
5. Install tesseract using the Windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki
   - Note the tesseract path from the installation.
   - Set the tesseract path in the settings.py file (it may already be correct)
6. Disable all in-game overlays
7. Run the main.py file

## FEATURES:
- Read the champions in the shop and purchase the one that a user specifies
- Reroll the shop after purchasing champions

## TODO:
- Implement threading to speed up shop reading
- Implement GUI
