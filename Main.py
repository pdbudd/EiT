import dearpygui.dearpygui as dpg
import Landing_page, Place_info, Travel, config
import googlemaps as gmaps

gmaps.Client(key=config.GMAPS_API_KEY)

dpg.create_context()
dpg.create_viewport(title='TooGoodToNOOOOO', width=450, height=800)
dpg.setup_dearpygui()
with dpg.window(label="TGTN", tag="main_window"):
    dpg.add_button(label="Travel", width=150, height=50, callback=Travel.travel)
    dpg.add_button(label="Places", width=150, height=50, callback=Place_info.places)

Landing_page.Land()

dpg.set_primary_window("main_window", True)

dpg.show_viewport()
dpg.start_dearpygui()