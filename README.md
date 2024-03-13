# EZ Lyf

Easily copy repetitve strings to clipboard.

## How to use
1. Open config file with editor of choice.
2. Add all strings you want to be able to quickly copy, each on its own line, no line endings.
3. Click button to add string to clipboard.

## How to run

### Prerequisites
- python 3.10

### Run from source
- python -m venv .venv
- source .venv/Scripts/activate
- pip install -r requirements.txt
- python main.py

### Run exe
- Find exe in release folder and run it.

## How to build
- Install prerequisites
- Make sure youre in the right virtual environment
- run compile.sh

### Misc
- Emails will be split in 2 buttons: username and entire email(button label will be just @whatever.com, but content will be username@whatever.com)
- Clipboard is cleared on exit.
- Tool is set to stay always on top.
- Current week tray icon. Will make sense later.