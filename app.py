from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from default_keyboards import main_menu 
from aiogram.dispatcher import FSMContext




token = "6473742098:AAHLBw4-zDduZe0HutTmLUJ4ZRi79Dfdf8A"
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)



@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    
    text = f"Assalomu alaykum, {message.from_user.full_name}"
    await message.answer(text=text, reply_markup=main_menu)


@dp.message_handler(text="Mahsulot sotish.")
async def mahsulot_sotuv(message:types.Message):
    text="QANDAY MAHSULOT SOTMOQCHISZ"
    await message.answer(text=text)

@dp.message_handler(text="Mars mahsulotlari.")
async def mahsulot_handler(message:types.Message):
    text="MAHSULOTLAR"
    await message.answer(text=text)
    
dp.message_handler(text="Mening mahsulotlarm.")
async def _my_mahsulot_handler(message:types.Message):
    text="siznig mahsulotlaringz"
    await message.answer(text=text)
@dp.message_handler(text="A'loqa.")
async def _my_contact_handler(message:types.Message):
    text="chat_id"
    await message.answer(text=text)




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)