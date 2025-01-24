from aiogram.fsm.state import State, StatesGroup


class Registor(StatesGroup):
    name = State()
    surname = State()
    phone = State()
