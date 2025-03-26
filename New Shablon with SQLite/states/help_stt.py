from aiogram.fsm.state import State, StatesGroup

class Help(StatesGroup):
    help = State()

class LaptopAdd(StatesGroup):
    name = State()
    pic = State()
    storage = State()
    color = State()
    price = State()

class Computer(StatesGroup):
    computer = State()

class Registor(StatesGroup):
    name = State()
    surname = State()
    phone = State()