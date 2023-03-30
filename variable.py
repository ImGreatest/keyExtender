import string
import keyboard

modifier = list(keyboard.all_modifiers)
f_buttons = list([str(f'F{i}') for i in range(12)])
num_buttons = list([str(f'Num{i}') for i in range(0, 10)])
punctuation, ascii_lowercase = list([str(i) for i in string.punctuation]), list([str(i) for i in string.ascii_lowercase]),
digits = list([str(i) for i in string.digits])
substandard = ["esd", "page_up", "page_down", "home", "insert", "print screen", "tab", "esc", "space"]

hotkey = ['1']
print()
