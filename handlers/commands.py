from aiogram import F, Router, Dispatcher, Bot
from aiogram.types import Message
from aiogram import types
from keyboard.inline.inlinekb import get_inline_keyboard, kurs_kb, selfimpurl, iturl, design, other
from aiogram.utils.keyboard import ReplyKeyboardBuilder


bot = Bot
router = Router()
dp = Dispatcher


@router.message(F.text == '/start')
async def cmd_start(message: Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='🏡Главное меню'))
    builder.adjust(1)
    await message.answer('⚡Привет, меня зовут Курси', reply_markup=builder.as_markup(resize_keyboard=True),
                         )
    await message.answer_sticker('CAACAgQAAxkBAAEKkU1lM5RYih9nIAgK5r6GaNw3zkpA0gACdw0AAvEUWFOUVhzRUGKbKTAE')


@router.message(F.text == '🏡Главное меню')
async def cmd_start(message: Message):
    await message.answer('⚡Главное меню', reply_markup=get_inline_keyboard())
    await message.answer_sticker('CAACAgQAAxkBAAEKkU1lM5RYih9nIAgK5r6GaNw3zkpA0gACdw0AAvEUWFOUVhzRUGKbKTAE')


@router.callback_query(F.data == 'kursi')
async def kursi_cmd(callback: types.CallbackQuery):
    await callback.message.edit_text('😶‍🌫️️Выберите категорию курсов')
    await callback.message.edit_reply_markup(reply_markup=kurs_kb())


@router.callback_query(F.data == 'razvitie')
async def razvitie_cmd(callback: types.CallbackQuery):
    await callback.message.edit_text('👤Саморазвитие')
    await callback.message.edit_reply_markup(reply_markup=selfimpurl())


@router.callback_query(F.data == 'it')
async def it_cmd(callback: types.CallbackQuery):
    await callback.message.edit_text('💻Программирование')
    await callback.message.edit_reply_markup(reply_markup=iturl())


@router.callback_query(F.data == 'design')
async def it_cmd(callback: types.CallbackQuery):
    await callback.message.edit_text('🎨Дизайн')
    await callback.message.edit_reply_markup(reply_markup=design())


@router.callback_query(F.data == 'other')
async def it_cmd(callback: types.CallbackQuery):
    await callback.message.edit_text('🥷Другое')
    await callback.message.edit_reply_markup(reply_markup=other())







