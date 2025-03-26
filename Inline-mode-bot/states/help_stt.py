from aiogram.fsm.state import State, StatesGroup

class Help(StatesGroup):
    help = State()


class Voice(StatesGroup):
    name = State()
    voice = State()