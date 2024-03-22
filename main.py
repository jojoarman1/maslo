import logging
import time
import asyncio
from aiogram import Bot, Dispatcher, types

# Устанавливаем уровень логгирования
logging.basicConfig(level=logging.INFO)

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на ваш токен, который получили у BotFather
TOKEN = '6850987188:AAGaqkwWj092UNLpTsK1uoIRaeOBgR9tfVs'

# Создаем экземпляр бота
bot = Bot(token=TOKEN)
# Создаем диспетчер для обработки входящих сообщений
dp = Dispatcher(bot)


# Функция, которая формирует клавиатуру с инлайн кнопками
def get_main_menu_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("Меню", callback_data="menu")
    )
    return keyboard


# Функция, которая формирует клавиатуру с остальными кнопками
def get_sub_menu_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("Подбор по авто", callback_data="auto_selection"),
        types.InlineKeyboardButton("Подбор на China auto", callback_data="china_auto_selection")
    )
    keyboard.row(
        types.InlineKeyboardButton("Масло", callback_data="oil"),
        types.InlineKeyboardButton("LYNXauto", callback_data="LYNXauto")
    )
    keyboard.row(
        types.InlineKeyboardButton("SUFIX", callback_data="SUFIX"),
        types.InlineKeyboardButton("MECAFILTER", callback_data="MECAFILTER")
    )
    keyboard.row(
        types.InlineKeyboardButton("INKO", callback_data="INKO"),
        types.InlineKeyboardButton("JEENICE", callback_data="JEENICE")
    )
    keyboard.row(
        types.InlineKeyboardButton("DJB", callback_data="DJB"),
        types.InlineKeyboardButton("G-AUTOPARTS", callback_data="G-AUTOPARTS")
    )
    keyboard.row(
        types.InlineKeyboardButton("Aplus", callback_data="Aplus"),
        types.InlineKeyboardButton("Аккумуляторы", callback_data="batteries")
    )
    keyboard.row(
        types.InlineKeyboardButton("Акции", callback_data="promotions")
    )
    return keyboard


# Обработка нажатия кнопки "Подбор по авто"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'auto_selection')
async def show_auto_selection_menu(callback_query: types.CallbackQuery):
    # Отправляем сообщение с клавиатурой для выбора автомобилей
    await bot.edit_message_text("Выберите автомобиль:", callback_query.from_user.id,
                                callback_query.message.message_id, reply_markup=get_auto_selection_keyboard())


# Функция, которая формирует клавиатуру с кнопками подбора авто
def get_auto_selection_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("Accent 1.5 Тагаз 102 л.с", callback_data="accent_tagaz"),
        types.InlineKeyboardButton("Almera G15", callback_data="almera_g15")
    )
    keyboard.row(
        types.InlineKeyboardButton("Corolla E150 2006-2013", callback_data="corolla_e150"),
        types.InlineKeyboardButton("Focus II Рестайл", callback_data="focus_restyled")
    )
    keyboard.row(
        types.InlineKeyboardButton("Logan до 2014", callback_data="logan"),
        types.InlineKeyboardButton("Polo седан 2010-2018", callback_data="polo_sedan")
    )
    keyboard.row(
        types.InlineKeyboardButton("Priora", callback_data="priora"),
        types.InlineKeyboardButton("Rapid", callback_data="rapid")
    )
    keyboard.row(
        types.InlineKeyboardButton("Solaris-Rio c 2017", callback_data="solaris_rio"),
        types.InlineKeyboardButton("Vesta седан с 2015", callback_data="vesta_sedan")
    )
    keyboard.row(
        types.InlineKeyboardButton("Выйти в меню", callback_data="menu")  # Добавляем кнопку "Меню"
    )
    return keyboard


# Обработка нажатия кнопки "Accent 1.5 Тагаз 102 л.с"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'accent_tagaz')
async def send_accent_tagaz_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Accent1.5 Тагаз 102 лс.xlsx')


# Обработка нажатия кнопки "Almera G15"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'almera_g15')
async def send_almera_g15_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Almera G15.xlsx')


# Обработка нажатия кнопки "Corolla E150 2006-2013"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'corolla_e150')
async def send_corolla_e150_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Corolla E150 2006-2013.xlsx')


# Обработка нажатия кнопки "Focus II Рестайл"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'focus_restyled')
async def send_focus_restyled_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Focus II рестайл.xlsx')


# Обработка нажатия кнопки "Logan до 2014"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'logan')
async def send_logan_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Logan до 2014.xlsx')


# Обработка нажатия кнопки "Polo седан 2010-2018"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'polo_sedan')
async def send_polo_sedan_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Polo седан 2010-2018.xlsx')


# Обработка нажатия кнопки "Priora"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'priora')
async def send_priora_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Priora.xlsx')


# Обработка нажатия кнопки "Rapid"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'rapid')
async def send_rapid_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Rapid.xlsx')


# Обработка нажатия кнопки "Solaris-Rio c 2017"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'solaris_rio')
async def send_solaris_rio_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Solaris-Rio c 2017.xlsx')


# Обработка нажатия кнопки "Vesta седан с 2015"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'vesta_sedan')
async def send_vesta_sedan_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Vesta седан c 2015.xlsx')


# Функция, которая формирует клавиатуру для выбора автомобилей из Китая
def get_china_auto_selection_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("Emgrand X7", callback_data="emgrand_x7"),
        types.InlineKeyboardButton("Exeed TXL D21", callback_data="exeed_txl_d21")
    )
    keyboard.row(
        types.InlineKeyboardButton("Geely Atlas", callback_data="geely_atlas"),
        types.InlineKeyboardButton("Geely Atlas Pro", callback_data="geely_atlas_pro")
    )
    keyboard.row(
        types.InlineKeyboardButton("Geely Tugella", callback_data="geely_tugella"),
        types.InlineKeyboardButton("Haval F7X", callback_data="haval_f7x")
    )
    keyboard.row(
        types.InlineKeyboardButton("Haval Jolion", callback_data="haval_jolion"),
        types.InlineKeyboardButton("Monjaro KX11", callback_data="monjaro_kx11")
    )
    keyboard.row(
        types.InlineKeyboardButton("Omoda C5", callback_data="omoda_c5"),
        types.InlineKeyboardButton("Tiggo 4 T17", callback_data="tiggo_4_t17")
    )
    keyboard.row(
        types.InlineKeyboardButton("Tiggo 7 Pro T1E", callback_data="tiggo_7_pro_t1e"),
        types.InlineKeyboardButton("Выйти в меню", callback_data="menu")  # Добавляем кнопку "Меню"
    )
    return keyboard


# Функция, которая формирует клавиатуру с выбором масла
def get_oil_selection_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("BARDAHL", callback_data="bardahl"),
        types.InlineKeyboardButton("NGN", callback_data="ngn")
    )
    keyboard.row(
        types.InlineKeyboardButton("PEMCO", callback_data="pemco"),
        types.InlineKeyboardButton("KORSON", callback_data="korson")
    )
    keyboard.row(
        types.InlineKeyboardButton("CHEMPIOIL", callback_data="chempioil"),
        types.InlineKeyboardButton("Выйти в меню", callback_data="menu")  # Добавляем кнопку "Меню"
    )
    return keyboard


# Обработка нажатия кнопки "BARDAHL"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'bardahl')
async def handle_bardahl_button(callback_query: types.CallbackQuery):
    # Формируем клавиатуру с дополнительными кнопками
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("Проценка", callback_data="procentka"),
        types.InlineKeyboardButton("Контракт СТО", callback_data="contract_sto")
    )
    keyboard.row(
        types.InlineKeyboardButton("Контракт СР", callback_data="contract_sr"),
        types.InlineKeyboardButton("Хим анализ", callback_data="chemical_analysis")
    )
    keyboard.row(
        types.InlineKeyboardButton("Выйти в меню", callback_data="menu"),  # Добавляем кнопку "Меню"
    )

    # Отправляем сообщение с дополнительными кнопками
    await bot.send_message(callback_query.from_user.id, "Выберите дополнительные опции:", reply_markup=keyboard)


# Обработка нажатия кнопки "NGN"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'ngn')
async def handle_ngn_button(callback_query: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("Проценка", callback_data="procentka"),
        types.InlineKeyboardButton("Контракт СТО", callback_data="contract_sto")
    )
    keyboard.row(
        types.InlineKeyboardButton("Контракт СР", callback_data="contract_sr"),
        types.InlineKeyboardButton("Хим анализ", callback_data="chemical_analysis")
    )
    keyboard.row(
        types.InlineKeyboardButton("Выйти в меню", callback_data="menu"),  # Добавляем кнопку "Меню"
    )
    await bot.send_message(callback_query.from_user.id, "Выберите дополнительные опции:", reply_markup=keyboard)


# Обработка нажатия кнопки "PEMCO"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'pemco')
async def handle_pemco_button(callback_query: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("Проценка", callback_data="procentka"),
        types.InlineKeyboardButton("Контракт СТО", callback_data="contract_sto")
    )
    keyboard.row(
        types.InlineKeyboardButton("Контракт СР", callback_data="contract_sr"),
        types.InlineKeyboardButton("Хим анализ", callback_data="chemical_analysis")
    )
    keyboard.row(
        types.InlineKeyboardButton("Выйти в меню", callback_data="menu"),  # Добавляем кнопку "Меню"
    )
    await bot.send_message(callback_query.from_user.id, "Выберите дополнительные опции:", reply_markup=keyboard)


# Обработка нажатия кнопки "KORSON"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'korson')
async def handle_korson_button(callback_query: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("Проценка", callback_data="procentka"),
        types.InlineKeyboardButton("Контракт СТО", callback_data="contract_sto")
    )
    keyboard.row(
        types.InlineKeyboardButton("Контракт СР", callback_data="contract_sr"),
        types.InlineKeyboardButton("Хим анализ", callback_data="chemical_analysis")
    )
    keyboard.row(
        types.InlineKeyboardButton("Выйти в меню", callback_data="menu"),  # Добавляем кнопку "Меню"
    )
    await bot.send_message(callback_query.from_user.id, "Выберите дополнительные опции:", reply_markup=keyboard)


# Обработка нажатия кнопки "CHEMPIOIL"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'chempioil')
async def handle_chempioil_button(callback_query: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("Проценка", callback_data="procentka"),
        types.InlineKeyboardButton("Контракт СТО", callback_data="contract_sto")
    )
    keyboard.row(
        types.InlineKeyboardButton("Контракт СР", callback_data="contract_sr"),
        types.InlineKeyboardButton("Хим анализ", callback_data="chemical_analysis")
    )
    keyboard.row(
        types.InlineKeyboardButton("Выйти в меню", callback_data="menu"),  # Добавляем кнопку "Меню"
    )
    await bot.send_message(callback_query.from_user.id, "Выберите дополнительные опции:", reply_markup=keyboard)


# Обработка нажатия кнопки "Масло"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'oil')
async def show_oil_selection_menu(callback_query: types.CallbackQuery):
    # Отправляем сообщение с клавиатурой для выбора масла
    await bot.edit_message_text("Выберите масло:", callback_query.from_user.id, callback_query.message.message_id,
                                reply_markup=get_oil_selection_keyboard())


# Функция для отправки файла с информацией об автомобиле
async def send_car_info_file(callback_query: types.CallbackQuery, file_path: str):
    with open(file_path, 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Файл с информацией об автомобиле")


# Обработка нажатия кнопки "Emgrand X7"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'emgrand_x7')
async def send_emgrand_x7_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Emgrand X7.xlsx')


# Обработка нажатия кнопки "Exeed TXL D21"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'exeed_txl_d21')
async def send_exeed_txl_d21_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Exeed TXL D21.xlsx')


# Обработка нажатия кнопки "Geely Atlas"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'geely_atlas')
async def send_geely_atlas_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Geely Atlas.xlsx')


# Обработка нажатия кнопки "Geely Atlas Pro"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'geely_atlas_pro')
async def send_geely_atlas_pro_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Geely Atlas Pro.xlsx')


# Обработка нажатия кнопки "Geely Tugella"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'geely_tugella')
async def send_geely_tugella_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Geely Tugella.xlsx')


# Обработка нажатия кнопки "Haval F7X"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'haval_f7x')
async def send_haval_f7x_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Haval F7X.xlsx')


# Обработка нажатия кнопки "Haval Jolion"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'haval_jolion')
async def send_haval_jolion_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Haval Jolion.xlsx')


# Обработка нажатия кнопки "Monjaro KX11"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'monjaro_kx11')
async def send_monjaro_kx11_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Monjaro KX11.xlsx')


# Обработка нажатия кнопки "Omoda C5"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'omoda_c5')
async def send_omoda_c5_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Omoda C5.xlsx')


# Обработка нажатия кнопки "Tiggo 4 T17"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'tiggo_4_t17')
async def send_tiggo_4_t17_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Tiggo 4 T17.xlsx')


# Обработка нажатия кнопки "Tiggo 7 Pro T1E"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'tiggo_7_pro_t1e')
async def send_tiggo_7_pro_t1e_info(callback_query: types.CallbackQuery):
    await send_car_info_file(callback_query, 'Tiggo 7 Prо T1E.xlsx')


# Обработка команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Получаем имя пользователя и его user_id
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    # Создаем ссылку с именем пользователя
    user_link = f"<a href='tg://user?id={user_id}'>{user_name}</a>"
    # Создаем приветственное сообщение с кликабельным именем пользователя и кнопкой "Меню"
    welcome_message = f"Привет, менеджер {user_link}!\n"
    # Отправляем приветственное сообщение с кнопкой "Меню"
    await bot.send_message(message.chat.id, welcome_message, parse_mode=types.ParseMode.HTML,
                           reply_markup=get_main_menu_keyboard())


# Обработка нажатия кнопки "Меню"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'menu')
async def show_main_menu(callback_query: types.CallbackQuery):
    # Отправляем сообщение с главным меню
    await bot.edit_message_text("Выберите категорию:", callback_query.from_user.id, callback_query.message.message_id,
                                reply_markup=get_sub_menu_keyboard())


# Обработка нажатия кнопки "Подбор на China auto"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'china_auto_selection')
async def show_china_auto_selection_menu(callback_query: types.CallbackQuery):
    # Отправляем сообщение с клавиатурой для выбора автомобилей из Китая
    await bot.edit_message_text("Выберите автомобиль из Китая:", callback_query.from_user.id,
                                callback_query.message.message_id, reply_markup=get_china_auto_selection_keyboard())


async def main():
    try:
        # Основная логика вашего приложения
        await dp.start_polling()
    except Exception as e:
        # Логируем ошибку
        logging.error(f"An error occurred in main: {e}")

if __name__ == '__main__':
    # Запускаем бесконечный цикл для работы бота
    while True:
        try:
            # Создаем и запускаем асинхронный цикл
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
        except Exception as error:
            # Логируем ошибку
            logging.error(f"An error occurred: {error}")
            # Пауза перед повторной попыткой запуска бота
            time.sleep(5)  # Можно изменить время паузы по необходимости
