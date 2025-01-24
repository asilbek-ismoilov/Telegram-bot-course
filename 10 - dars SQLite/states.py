from aiogram.fsm.state import State, StatesGroup

class Registor(StatesGroup):
    ism = State() 
    familiya = State() 
    yosh = State()
    tel = State()
    kurs = State()
