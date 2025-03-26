from aiogram.fsm.state import State, StatesGroup


class Registor(StatesGroup):
    name = State()
    surname = State()
    phone = State()

class Computer(StatesGroup):
    computer = State()

# ❗️❗️❗️  ADMIN  ❗️❗️❗️

class Laptop(StatesGroup):
    name = State()
    photo = State()
    price = State()
    color = State()

