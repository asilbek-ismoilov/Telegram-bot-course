from aiogram.fsm.state import State, StatesGroup

class BagPic(StatesGroup):
    background_pic = State()  # Orqa fon rasmini yuklash holati
    photo = State()     # Ustki rasmni yuklash holati

class RemoveBg(StatesGroup):
    removebg = State() 


class BagColor(StatesGroup):
    bagcolor = State()  