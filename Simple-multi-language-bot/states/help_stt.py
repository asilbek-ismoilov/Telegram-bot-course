from aiogram.fsm.state import State, StatesGroup

class Help(StatesGroup):
    help = State()

class ChooseLanguage(StatesGroup):
    language = State()