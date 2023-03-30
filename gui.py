from dearpygui.dearpygui import *
from functions import *
from variable import *


def gui():
    create_context()
    create_viewport(width=480, height=480, title='Extender', resizable=False)
    setup_dearpygui()

    with window(label='Extender', width=480, height=480, no_title_bar=True, tag="MainWindow"):

        set_viewport_pos([get_viewport_client_width() / 1.7, get_viewport_client_height() / 3])

        with menu_bar():

            with menu(label='Settings'):
                add_checkbox(label="Auto Start", default_value=False, callback=auto_start, tag='autostart_item')

                with tooltip(last_item()):
                    add_text("Start when Windows starts")

                add_checkbox(label="Fullscreen", default_value=False, callback=fullscreen, tag='fullscreen_item')

            add_menu_item(label='About', callback=lambda: print('aboba'))


        with tab_bar():

            with tab(label='remaping'):
                add_separator()
                add_text('Source key', pos=(60, 80))

                with tooltip(last_item()):
                    add_text('Select origin key')

                add_combo(key, default_value=key[0], pos=(25, 110), width=150, tag='remap_combo_source')
                add_button(label="...", )

                add_text('Change to', pos=(340, 80))

                with tooltip(last_item()):
                    add_text('Choose a key to change')

                add_combo(key, default_value=key[0], pos=(290, 110), width=150, tag='remap_combo_changer')

                add_button(label="Activate", pos=(200, 150), callback=lambda: remap_action(), tag="remap_button")
                print()


            with tab(label='Text changer'):
                add_separator()
                add_text('Key', pos=(60, 80))

                with tooltip(last_item()):
                    add_text('Choose key')

                add_combo(key, default_value=key[0], width=150, pos=(25, 110))

                add_text('Hotkey', pos=(340, 80))

                with tooltip(last_item()):
                    add_text('Choose hotkey')

                add_combo(hotkey, default_value=hotkey[0],  width=150, pos=(290, 110))

            with tab(label='blocking key'):
                add_separator()
                add_text('Key', pos=(60, 80))

                with tooltip(last_item()):
                    add_text('Choose key to lock')

                add_combo(key, default_value=key[0], pos=(25, 110), width=150)

                add_text('Hotkey', pos=(340, 80))

                with tooltip(last_item()):
                    add_text('Choose hotkey to lock')

                add_combo(hotkey, default_value=hotkey[0], pos=(290, 110), width=150, tag='Blocking Key')

            with tab(label='text substitute'):
                add_separator()
                add_text('help', pos=(25, 80))

                with tooltip(last_item()):
                    add_text('Enter replacement text')

                add_input_text(tag='text substitute ', pos=(25, 110), default_value='...', height=25, width=400, multiline=True, tab_input=True)

            with tab(label="Hotkeys"):
                add_separator()
                add_checkbox(label="Use Hotkeys", pos=(60, 80), default_value=False, tag='Hotkeys_check')





    show_viewport()
    start_dearpygui()
    destroy_context()

