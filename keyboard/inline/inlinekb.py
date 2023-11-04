from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🎓Курсы', callback_data='kursi')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def kurs_kb():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='👤Саморазвитие', callback_data='razvitie')
    keyboard_builder.button(text='💻Программирование', callback_data='it')
    keyboard_builder.button(text='🎨Дизайн', callback_data='design')
    keyboard_builder.button(text='🥷Другое', callback_data='other')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def selfimpurl():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🎓Курсы', url='https://t.me/+pxM9DYZZnYk1NGQ0')
    keyboard_builder.button(text='◀️Назад', callback_data='kursi')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def iturl():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🎓Курсы', url='https://t.me/+75Ui-70pJqBiMDBk')
    keyboard_builder.button(text='◀️Назад', callback_data='kursi')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def design():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🎓Курсы', url='https://t.me/+nfPpYWI7x4U0YzU0')
    keyboard_builder.button(text='◀️Назад', callback_data='kursi')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def other():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🎓Курсы', url='https://t.me/+1WS_qVWYNqRiNmRk')
    keyboard_builder.button(text='◀️Назад', callback_data='other')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
