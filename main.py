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


# Обработка нажатия кнопки "LYNXauto"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'LYNXauto')
async def handle_lynxauto_button(callback_query: types.CallbackQuery):
    # Создаем клавиатуру с кнопками для выбора
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("Товарные группы ТОП LA", callback_data="lynx_top_la"),
        types.InlineKeyboardButton("LYNX (автолампы)", callback_data="lynx_avtolampy")
    )
    keyboard.row(
        types.InlineKeyboardButton("LYNX (катушки зажигания)", callback_data="lynx_katushki_zazhiganiya"),
        types.InlineKeyboardButton("LYNX (комплекты ГРМ)", callback_data="lynx_komplekty_grm")
    )
    keyboard.row(
        types.InlineKeyboardButton("LYNX (подшипники и ступицы)", callback_data="lynx_podshipniki_i_stupitsy"),
        types.InlineKeyboardButton("LYNX (помпы водяные)", callback_data="lynx_pompy_vodyanye")
    )
    keyboard.row(
        types.InlineKeyboardButton("LYNX (свечи зажигания)", callback_data="lynx_svechi_zazhiganiya"),
        types.InlineKeyboardButton("LYNX (тормозные системы)", callback_data="lynx_tormoznye_sistemy")
    )
    keyboard.row(
        types.InlineKeyboardButton("LYNX (фильтры)", callback_data="lynx_filtry"),
        types.InlineKeyboardButton("LYNX (ШРУСы)", callback_data="lynx_shrusy")
    )
    keyboard.add(
        types.InlineKeyboardButton("LYNX (щётки стеклоочистителя)", callback_data="lynx_schetki_stekloochistitelya"),
        types.InlineKeyboardButton("Выйти в меню", callback_data="menu")  # Добавляем кнопку "Меню"
    )

    # Заменяем предыдущую клавиатуру новой
    await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id, reply_markup=keyboard)


# Обработка нажатия кнопки "Товарные группы ТОП LA"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'lynx_top_la')
async def handle_lynx_top_la_button(callback_query: types.CallbackQuery):
    with open('Товарные группы ТОП LA.xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Информация о товарных группах ТОП LA")


# Обработка нажатия кнопки "LYNX (автолампы)"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'lynx_avtolampy')
async def handle_lynx_avtolampy_button(callback_query: types.CallbackQuery):
    with open('LYNX (автолампы).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Информация о LYNX (автолампы)")


# Обработка нажатия кнопки "LYNX (катушки зажигания)"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'lynx_katushki_zazhiganiya')
async def handle_lynx_katushki_zazhiganiya_button(callback_query: types.CallbackQuery):
    with open('LYNX (катушки зажигания).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Информация о LYNX (катушки зажигания)")


# Обработка нажатия кнопки "LYNX (комплекты ГРМ)"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'lynx_komplekty_grm')
async def handle_lynx_komplekty_grm_button(callback_query: types.CallbackQuery):
    with open('LYNX (комплекты ГРМ).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Информация о LYNX (комплекты ГРМ)")


# Обработка нажатия кнопки "LYNX (подшипники и ступицы)"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'lynx_podshipniki_i_stupitsy')
async def handle_lynx_podshipniki_i_stupitsy_button(callback_query: types.CallbackQuery):
    with open('LYNX (подшипники и ступицы).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Информация о LYNX (подшипники и ступицы)")


# Обработка нажатия кнопки "LYNX (помпы водяные)"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'lynx_pompy_vodyanye')
async def handle_lynx_pompy_vodyanye_button(callback_query: types.CallbackQuery):
    with open('LYNX (помпы водяные).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Информация о LYNX (помпы водяные)")


# Обработка нажатия кнопки "LYNX (свечи зажигания)"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'lynx_svechi_zazhiganiya')
async def handle_lynx_svechi_zazhiganiya_button(callback_query: types.CallbackQuery):
    with open('LYNX (свечи зажигания).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Информация о LYNX (свечи зажигания)")


# Обработка нажатия кнопки "LYNX (тормозные системы)"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'lynx_tormoznye_sistemy')
async def handle_lynx_tormoznye_sistemy_button(callback_query: types.CallbackQuery):
    with open('LYNX (тормозные системы).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Информация о LYNX (тормозные системы)")


# Обработка нажатия кнопки "LYNX (фильтры)"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'lynx_filtry')
async def handle_lynx_filtry_button(callback_query: types.CallbackQuery):
    with open('LYNX (фильтры).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Информация о LYNX (фильтры)")


# Обработка нажатия кнопки "LYNX (ШРУСы)"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'lynx_shrusy')
async def handle_lynx_shrusy_button(callback_query: types.CallbackQuery):
    with open('LYNX (ШРУСы).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Информация о LYNX (ШРУСы)")


# Обработка нажатия кнопки "LYNX (щётки стеклоочистителя)"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'lynx_schetki_stekloochistitelya')
async def handle_lynx_schetki_stekloochistitelya_button(callback_query: types.CallbackQuery):
    with open('LYNX (щётки стеклоочистителя).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Информация о LYNX (щётки стеклоочистителя)")


# Обработка нажатия кнопки "SUFIX"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'SUFIX')
async def handle_sufix_button(callback_query: types.CallbackQuery):
    # Создаем клавиатуру с кнопками для каждой категории SUFIX
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("SUFIX (АМОРТИЗАТОРЫ)", callback_data="sufix_amortizatory"),
        types.InlineKeyboardButton("SUFIX (ДИСКИ ТОРМОЗНЫЕ)", callback_data="sufix_diski_tormoznye")
    )
    keyboard.row(
        types.InlineKeyboardButton("SUFIX (КАТУШКИ ЗАЖИГАНИЯ)", callback_data="sufix_katushki_zazhiganiya"),
        types.InlineKeyboardButton("SUFIX (КОЛОДКИ ТОРМОЗНЫЕ)", callback_data="sufix_kolodki_tormoznye")
    )
    keyboard.row(
        types.InlineKeyboardButton("SUFIX (СВЕЧИ ЗАЖИГАНИЯ)", callback_data="sufix_svechi_zazhiganiya"),
        types.InlineKeyboardButton("SUFIX (ФИЛЬТРЫ)", callback_data="sufix_filtry")
    )
    keyboard.add(
        types.InlineKeyboardButton("SUFIX (ЩЕТКИ СТЕКЛООЧИСТИТЕЛЕЙ)", callback_data="sufix_schetki_stekloochistiteley"),
        types.InlineKeyboardButton("Товарные группы ТОП", callback_data="tovar_group"),
        types.InlineKeyboardButton("Выйти в меню", callback_data="menu")  # Добавляем кнопку "Меню"
    )

    # Редактируем сообщение, заменяя текст и клавиатуру
    await bot.edit_message_text("Выберите нужный вам товар SUFIX:",
                                callback_query.message.chat.id,
                                callback_query.message.message_id,
                                reply_markup=keyboard)


# Обработка нажатия на категорию SUFIX (АМОРТИЗАТОРЫ)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'sufix_amortizatory')
async def handle_sufix_amortizatory(callback_query: types.CallbackQuery):
    with open('SUFIX (АМОРТИЗАТОРЫ).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file,
                                caption="")


# Обработка нажатия на категорию SUFIX (ДИСКИ ТОРМОЗНЫЕ)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'sufix_diski_tormoznye')
async def handle_sufix_diski_tormoznye(callback_query: types.CallbackQuery):
    with open('SUFIX (ДИСКИ ТОРМОЗНЫЕ).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file,
                                caption="")


# Обработка нажатия на категорию SUFIX (КАТУШКИ ЗАЖИГАНИЯ)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'sufix_katushki_zazhiganiya')
async def handle_sufix_katushki_zazhiganiya(callback_query: types.CallbackQuery):
    with open('SUFIX (КАТУШКИ ЗАЖИГАНИЯ).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file,
                                caption="")


# Обработка нажатия на категорию SUFIX (КОЛОДКИ ТОРМОЗНЫЕ)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'sufix_kolodki_tormoznye')
async def handle_sufix_kolodki_tormoznye(callback_query: types.CallbackQuery):
    with open('SUFIX (КОЛОДКИ ТОРМОЗНЫЕ).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file,
                                caption="")


# Обработка нажатия на категорию SUFIX (СВЕЧИ ЗАЖИГАНИЯ)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'sufix_svechi_zazhiganiya')
async def handle_sufix_svechi_zazhiganiya(callback_query: types.CallbackQuery):
    with open('SUFIX (СВЕЧИ ЗАЖИГАНИЯ).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file,
                                caption="")


# Обработка нажатия на категорию SUFIX (ФИЛЬТРЫ)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'sufix_filtry')
async def handle_sufix_filtry(callback_query: types.CallbackQuery):
    with open('SUFIX (ФИЛЬТРЫ).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="")


# Обработка нажатия на категорию SUFIX (ЩЕТКИ СТЕКЛООЧИСТИТЕЛЕЙ)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'sufix_schetki_stekloochistiteley')
async def handle_sufix_schetki_stekloochistiteley(callback_query: types.CallbackQuery):
    with open('SUFIX (ЩЁТКИ СТЕКЛООЧИСТИТЕЛЕЙ).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file,
                                caption="")


# Обработка нажатия на категорию Товарные группы ТОП
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'tovar_group')
async def handle_sufix_schetki_stekloochistiteley(callback_query: types.CallbackQuery):
    with open('Товарные группы ТОП.xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file,
                                caption="")


# Обработка нажатия кнопки "MECAFILTER"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'MECAFILTER')
async def handle_mecafilter_button(callback_query: types.CallbackQuery):
    # Создаем клавиатуру с двумя кнопками
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("MECAFILTER ТОП", callback_data="mecafilter_top"),
        types.InlineKeyboardButton("MECAFILTER TRUCK", callback_data="mecafilter_truck")
    )

    # Отправляем сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, "MECAFILTER", reply_markup=keyboard)


# Обработка нажатия кнопки "MECAFILTER ТОП"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mecafilter_top')
async def handle_mecafilter_top_button(callback_query: types.CallbackQuery):
    # Отправляем файл MECAFILTER ТОП
    with open('MECAFILTER TOП.xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Файл MECAFILTER ТОП")


# Обработка нажатия кнопки "MECAFILTER TRUCK"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mecafilter_truck')
async def handle_mecafilter_truck_button(callback_query: types.CallbackQuery):
    # Отправляем файл MECAFILTER TRUCK
    with open('MECAFILTER TRUCK.xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Файл MECAFILTER TRUCK")


# Обработка нажатия кнопки "INKO"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'INKO')
async def handle_inko_button(callback_query: types.CallbackQuery):
    # Создаем клавиатуру с кнопкой "INKO ТОП"
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("INKO ТОП", callback_data="inko_top"))

    # Отправляем сообщение с кнопкой "INKO ТОП"
    await bot.send_message(callback_query.from_user.id, "INKO", reply_markup=keyboard)


# Обработка нажатия кнопки "INKO ТОП"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'inko_top')
async def handle_inko_top_button(callback_query: types.CallbackQuery):
    # Отправляем файл
    with open('INKO ТОП.xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="")


# Обработка нажатия кнопки "JEENICE"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'JEENICE')
async def handle_jeenice_button(callback_query: types.CallbackQuery):
    # Отправляем кнопку "JEENICE ТОП"
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("JEENICE ТОП", callback_data="jeenice_top"))
    await bot.send_message(callback_query.from_user.id, "JEENICE", reply_markup=keyboard)


# Обработка нажатия кнопки "JEENICE ТОП"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'jeenice_top')
async def handle_jeenice_top_button(callback_query: types.CallbackQuery):
    # Отправить файл
    with open('JEENICE ТОП.xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="")


# Обработка нажатия кнопки "DJB"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'DJB')
async def handle_djb_button(callback_query: types.CallbackQuery):
    # Отправляем кнопку "DJB ТОП"
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("DJB ТОП", callback_data="djb_top"))
    await bot.send_message(callback_query.from_user.id, "DJB", reply_markup=keyboard)


# Обработка нажатия кнопки "DJB ТОП"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'djb_top')
async def handle_djb_top_button(callback_query: types.CallbackQuery):
    # Отправляем файл
    with open('DJB ТОП.xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="")


# Обработка нажатия кнопки "G-AUTOPARTS"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'G-AUTOPARTS')
async def handle_g_autoparts_button(callback_query: types.CallbackQuery):
    # Создаем клавиатуру с кнопкой "G-AUTOPARTS ТОП"
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("G-AUTOPARTS ТОП", callback_data="g_autoparts_top"))
    # Отправляем сообщение с клавиатурой
    await bot.send_message(callback_query.from_user.id, "Выберите G-AUTOPARTS ТОП:", reply_markup=keyboard)

    # Обработка нажатия кнопки "G-AUTOPARTS ТОП"
    @dp.callback_query_handler(lambda query: query.data == 'g_autoparts_top')
    async def handle_g_autoparts_top_button(query: types.CallbackQuery):
        # Отправляем файл
        with open('G-AUTOPARTS ТОП.xlsx', 'rb') as file:
            await bot.send_document(query.from_user.id, file, caption="G-AUTOPARTS ТОП")


# Обработка нажатия кнопки "Aplus"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Aplus')
async def handle_aplus_button(callback_query: types.CallbackQuery):
    # Создаем клавиатуру с кнопкой "Aplus ТОП"
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("Aplus ТОП", callback_data="aplus_top")
    )
    # Отправляем сообщение с кнопкой "Aplus ТОП"
    await bot.send_message(callback_query.from_user.id, "Выберите:", reply_markup=keyboard)


# Обработка нажатия кнопки "Aplus ТОП"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'aplus_top')
async def handle_aplus_top_button(callback_query: types.CallbackQuery):
    # Отправляем файл
    with open('APlus ТОП.xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="")


# Обработка нажатия кнопки "Аккумуляторы"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'batteries')
async def show_battery_menu(callback_query: types.CallbackQuery):
    # Отправляем сообщение с клавиатурой для выбора типа аккумулятора
    await bot.edit_message_text("Выберите аккумулятор:", callback_query.from_user.id,
                                callback_query.message.message_id, reply_markup=get_battery_selection_keyboard())


# Функция, которая формирует клавиатуру для выбора типа аккумулятора
def get_battery_selection_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("BARTEX", callback_data="battery_bartex"),
        types.InlineKeyboardButton("LYNX", callback_data="battery_lynx"),
        types.InlineKeyboardButton("Выйти в меню", callback_data="menu")  # Добавляем кнопку "Меню"
    )
    return keyboard


# Обработка выбора типа аккумулятора "BARTEX"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'battery_bartex')
async def send_bartex_info(callback_query: types.CallbackQuery):
    # Отправить файл с информацией о аккумуляторе BARTEX
    with open('BATREX.xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Информация о аккумуляторе BARTEX")


# Обработка выбора типа аккумулятора "LYNX"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'battery_lynx')
async def send_lynx_info(callback_query: types.CallbackQuery):
    # Отправить файл с информацией о аккумуляторе LYNX
    with open('LYNX (АККУМУЛЯТОРЫ).xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Информация о аккумуляторе LYNX")


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
        types.InlineKeyboardButton("Проценка", callback_data="bardahl_procentka"),
        types.InlineKeyboardButton("Контракт СТО", callback_data="bardahl_contract_sto")
    )
    keyboard.row(
        types.InlineKeyboardButton("Контракт СР", callback_data="bardahl_contract_sr"),
        types.InlineKeyboardButton("Хим анализ", callback_data="bardahl_chemical_analysis")
    )
    keyboard.row(
        types.InlineKeyboardButton("Выйти в меню", callback_data="menu"),  # Добавляем кнопку "Меню"
    )

    # Отправляем сообщение с дополнительными кнопками
    await bot.send_message(callback_query.from_user.id, "Выберите дополнительные опции BARDAHL:", reply_markup=keyboard)


# Обработка нажатия кнопки "NGN"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'ngn')
async def handle_ngn_button(callback_query: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("Проценка", callback_data="ngn_procentka"),
        types.InlineKeyboardButton("Контракт СТО", callback_data="sto_ngn")
    )
    keyboard.row(
        types.InlineKeyboardButton("Контракт СР", callback_data="cp_ngn"),
        types.InlineKeyboardButton("Хим анализ", callback_data="himia_ngn")
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
        types.InlineKeyboardButton("Проценка", callback_data="pemco_procentka"),
        types.InlineKeyboardButton("Контракт СТО", callback_data="pemco_contract_sto")
    )
    keyboard.row(
        types.InlineKeyboardButton("Контракт СР", callback_data="pemco_contract_sr"),
        types.InlineKeyboardButton("Хим анализ", callback_data="pemco_chemical_analysis")
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
        types.InlineKeyboardButton("Проценка", callback_data="korson_procentka"),
        types.InlineKeyboardButton("Контракт СТО", callback_data="korson_contract_sto")
    )
    keyboard.row(
        types.InlineKeyboardButton("Контракт СР", callback_data="korson_contract_sr"),
        types.InlineKeyboardButton("Хим анализ", callback_data="korson_chemical_analysis")
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
        types.InlineKeyboardButton("Проценка", callback_data="chempioil_procentka"),
        types.InlineKeyboardButton("Контракт СТО", callback_data="contract_sto")
    )
    keyboard.row(
        types.InlineKeyboardButton("Контракт СР", callback_data="contract_sr"),
        types.InlineKeyboardButton("Хим анализ", callback_data="chempioil_chemical_analysis")
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


# Обработка нажатия кнопки "BARDAHL Проценка"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'bardahl_procentka')
async def handle_bardahl_procentka_button(callback_query: types.CallbackQuery):
    with open('Проценка Bardahl.xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="BARDAHL Проценка")


# Обработка нажатия кнопки "BARDAHL Контракт СТО"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'bardahl_contract_sto')
async def handle_bardahl_contract_sto_button(callback_query: types.CallbackQuery):
    with open('Контракт Bardahl СТО.pdf', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="BARDAHL Контракт СТО")


# Обработка нажатия кнопки "BARDAHL Контракт СР"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'bardahl_contract_sr')
async def handle_bardahl_contract_sr_button(callback_query: types.CallbackQuery):
    with open('Контракт Bardahl СР.pdf', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="BARDAHL Контракт СР")


# Обработка нажатия кнопки "BARDAHL Хим анализ"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'bardahl_chemical_analysis')
async def handle_bardahl_chemical_analysis_button(callback_query: types.CallbackQuery):
    with open('Хим анализ BARDAHL XTC 5w30 60L.pdf', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="BARDAHL Хим анализ")


# NGN
# Обработка нажатия кнопки "NGN Проценка"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'ngn_procentka')
async def handle_ngn_procentka_button(callback_query: types.CallbackQuery):
    with open('Процентка NGN.xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Проценка для NGN")


# Обработка нажатия кнопки "NGN Контракт СТО"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'sto_ngn')
async def handle_ngn_procentka_button(callback_query: types.CallbackQuery):
    with open('Контракт NGN СТО.pdf', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="NGN Контракт СТО")


# Обработка нажатия кнопки "NGN Контракт СР"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'cp_ngn')
async def handle_ngn_procentka_button(callback_query: types.CallbackQuery):
    with open('Контракт NGN СР.pdf', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="NGN Контракт СР")


# Обработка нажатия кнопки "NGN Хим анализ"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'himia_ngn')
async def handle_ngn_procentka_button(callback_query: types.CallbackQuery):
    with open('Хим анализ NGN A-Line Gold.pdf', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="NGN Хим анализ")


# PREMCO

# Обработка нажатия кнопки "PEMCO Проценка"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'pemco_procentka')
async def handle_pemco_procentka_button(callback_query: types.CallbackQuery):
    with open('Проценка Pemco.xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Проценка для PEMCO")


# Обработка нажатия кнопки "PEMCO Контракт СТО"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'pemco_contract_sto')
async def handle_pemco_contract_sto_button(callback_query: types.CallbackQuery):
    with open('Контракт СТО PEMCO.pdf', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Контракт СТО для PEMCO")


# Обработка нажатия кнопки "PEMCO Контракт СР"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'pemco_contract_sr')
async def handle_pemco_contract_sr_button(callback_query: types.CallbackQuery):
    with open('Контракт СР PEMCO.pdf', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Контракт СР для PEMCO")


# Обработка нажатия кнопки "PEMCO Хим анализ"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'pemco_chemical_analysis')
async def handle_pemco_chemical_analysis_button(callback_query: types.CallbackQuery):
    with open('Хим анализ Pemco.pdf', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Хим анализ для PEMCO")


# KORSON

# Обработка нажатия кнопки "KORSON Проценка"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'korson_procentka')
async def handle_korson_procentka_button(callback_query: types.CallbackQuery):
    with open('Проценка Korson.xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Проценка для KORSON")


# Обработка нажатия кнопки "KORSON Контракт СТО"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'korson_contract_sto')
async def handle_korson_contract_sto_button(callback_query: types.CallbackQuery):
    with open('Контракт Korson СТО.pdf', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Контракт СТО для KORSON")


# Обработка нажатия кнопки "KORSON Контракт СР"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'korson_contract_sr')
async def handle_korson_contract_sr_button(callback_query: types.CallbackQuery):
    with open('Контракт Korson СР.pdf', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Контракт СР для KORSON")


# Обработка нажатия кнопки "KORSON Хим анализ"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'korson_chemical_analysis')
async def handle_korson_chemical_analysis_button(callback_query: types.CallbackQuery):
    with open('Хим анализ Korson.pdf', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Хим анализ для KORSON")


# chempoil
# Обработка нажатия кнопки "CHEMPIOIL Проценка"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'chempioil_procentka')
async def handle_chempioil_procentka_button(callback_query: types.CallbackQuery):
    with open('Проценка Chempioil.xlsx', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Проценка для CHEMPIOIL")


# Обработка нажатия кнопки "CHEMPIOIL Хим анализ"
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'chempioil_chemical_analysis')
async def handle_chempioil_chemical_analysis_button(callback_query: types.CallbackQuery):
    with open('Хим анализ Chempioil JP 5w30.pdf', 'rb') as file:
        await bot.send_document(callback_query.from_user.id, file, caption="Хим анализ для CHEMPIOIL")


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
