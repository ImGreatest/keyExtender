import getpass
import os
import time
import keyboard

from dearpygui.dearpygui import *

from variable import *

modifier = list(keyboard.all_modifiers)
key = ['Disable key']+ list([str(f'Num{i}') for i in range(0, 10)]) + ['end', 'page up', 'page down', 'home', 'insert', 'print screen', 'tab', 'esc', 'space'] + list([str(f'F{i}') for i in range(1, 13)]) + [*[i for i in string.punctuation], *[int(i) for i in digits], *[i for i in string.ascii_lowercase]] + list(keyboard.all_modifiers)

""
#def key(modifiers: bool=True, substandard: bool=True, f_keys: bool=True, num_keys: bool=True, punctuation: bool=True, ascii_lower: bool=True, digits: bool=True) -> list:
#    key = list
#    if modifiers:
#        key += [i for i in modifier]
#    if substandard:
#        key += substandard
#    if f_keys:
#        key += f_buttons
#    if num_keys:
#        key += num_buttons
#    if punctuation:
#        key += punctuation
#    if ascii_lower:
#        key += ascii_lowercase
#    if digits:
#        key += digitscase
#
#    return key


def auto_start(sender, appdata, user_data):
    username = getpass.getuser()
    bat_path = fr'C:\\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

    if appdata:

        file_path = os.path.dirname(os.path.realpath(__file__)) + "\output\main.exe"
        with open(bat_path + '\\' + "openExtender.bat", "w+") as bat_file:
            bat_file.write(r'start "" "%s"' % file_path)

    else:
        try:
            os.remove(bat_path + '\\' + "openExtender.bat")
        except:
            FileNotFoundError

def remap_action():

    if get_item_label("remap_button") == "Activate":

        set_item_label("remap_button", "Suspend")
        remap_key(get_value("remap_combo_source"), get_value("remap_combo_changer"))
        info_message("Remaping was successful!")

    else:

        set_item_label("remap_button", "Activate")
        unremap_key(get_value("remap_combo_source"), get_value("remap_combo_changer"))
        info_message("Unremaping was successful!")

def block_action():

    if get_item_label("block_button") == "Go Block":

        set_item_label("block_button", "Unblock")
        block_key(get_value("block_combo"))
        info_message("Block key was successful!")
        configure_item("block_combo", enabled=False)

    else:

        set_item_label("block_button", "Go Block")
        unblock_key(get_value("block_combo"))
        info_message("Unblock key was successful!")
        configure_item("block_combo", enabled=True)

def remap_key(source_key=str, change_key=str):
    try:
        keyboard.remap_key(source_key, change_key)
        keyboard.remap_key(change_key, source_key)
        print(keyboard.get_hotkey_name())
    except:
        ValueError

def unremap_key(source_key=str, change_key=str):
    try:
        keyboard.unremap_key(source_key)
        keyboard.unremap_key(change_key)
    except:
        ValueError, TypeError

def block_key(key=str):
    keyboard.block_key(key)

def unblock_key(key=str):
    keyboard.unblock_key(key)

def text_writer(key=str, text=str):
    keyboard.add_hotkey(f'{key}', lambda: keyboard.write(f'{text}'))

def text_substitute(source_text, replacement_text):
    keyboard.add_abbreviation(source_text, replacement_text)

def fullscreen(sender, appdata, user_data):

    if appdata:
        set_viewport_width(1920)
        set_viewport_height(1080)
        set_viewport_pos([0, 0])
        print(get_viewport_client_width(), get_viewport_client_height())
        #configure_item("MainWindow", )

    else:
        set_viewport_width(480)
        set_viewport_height(480)
        set_viewport_pos([100, 100])

def timer(timeOfTimer=float):
    time.sleep(timeOfTimer)

def info_message(message):

    with mutex():

        with window(label="message", modal=True) as modal:
            add_text(message)

    w, h = get_item_width(modal), get_item_height(modal)
    set_item_pos(modal, [get_viewport_client_width() - w, get_viewport_client_height()])

    timer(0.8)
    delete_item(modal)