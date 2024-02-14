import dearpygui.dearpygui as dpg
import googlemaps as map
import geopy
from datetime import datetime

def travel():
    with dpg.window(label="Travel", tag="travel_page", width=450, height=400, no_close=True, ):
        dpg.add_input_text(label="Depart from", tag="from", height=80)
        dpg.add_input_text(label="Arrive at", tag="to", height=80)
        dpg.add_button(label="find route", width=200,height=80,pos=[10,180])
        dpg.add_button(label="cancel", width=200,height=80,pos=[220,180], callback=close)
    raise NotImplementedError

def close():
    dpg.delete_item("travel_page")