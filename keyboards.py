#keyboards.py
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

def main_menu():
    """
    Главное меню бота.
    """
    builder = InlineKeyboardBuilder()
    builder.button(text="🌤️ Получить прогноз", callback_data="open_forecast_menu")
    builder.button(text="📍 Указать город", callback_data="set_city")
    builder.button(text="⚙️ Настройки", callback_data="open_settings")
    builder.adjust(1)  # Расположение кнопок в один столбец
    return builder.as_markup()

def forecast_menu():
    """
    Меню выбора периода прогноза.
    """
    builder = InlineKeyboardBuilder()
    builder.button(text="🌤️ Сейчас", callback_data="get_weather_now")
    # Из-за того что бесплатный API позволяет только прогноз на 2 дня вперед, я вынужден поменять кнопки
    # builder.button(text="🌤️ На завтра", callback_data="get_tomorrow_weather")
    # builder.button(text="🌤️ На 3 дня", callback_data="get_weather_3days")
    builder.button(text="🌤️ На 2 дня", callback_data="get_weather_2days")
    builder.button(text="↩️ Назад", callback_data="back_to_menu")
    builder.adjust(1)  # Расположение кнопок в один столбец
    return builder.as_markup()

def settings_menu():
    """
    Меню настроек.
    """
    builder = InlineKeyboardBuilder()
    builder.button(text="🔔 Рассылка: Вкл/Выкл", callback_data="toggle_mailing")
    builder.button(text="🔤 Перевод: Вкл/Выкл", callback_data="toggle_translation")
    builder.button(text="💸 Пожертвование", callback_data="support")
    builder.button(text="↩️ Назад", callback_data="back_to_menu")
    builder.adjust(1)  # Расположение кнопок в один столбец
    return builder.as_markup()

def city_keyboard():
    """
    Клавиатура для выбора города.
    """
    cities = [
        ("Москва", "Moscow"),
        ("Санкт-Петербург", "Saint Petersburg"),
        ("Новосибирск", "Novosibirsk"),
        ("Екатеринбург", "Yekaterinburg"),
        ("Казань", "Kazan"),
        ("Нижний Новгород", "Nizhny Novgorod"),
        ("Челябинск", "Chelyabinsk"),
        ("Самара", "Samara"),
        ("Токио", "Tokyo"),
        ("Нью-Йорк", "New York"),
        ("Минск", "Minsk"),
        ("Киев", "Kyiv"),
        ("Астана", "Astana"),
        ("Ташкент", "Tashkent"),
    ]
    
    builder = InlineKeyboardBuilder()
    for text, city in cities:
        builder.button(text=text, callback_data=f"city_{city}")
    builder.button(text="🏙️ Другой", callback_data="other")
    builder.button(text="↩️ Назад", callback_data="back_to_menu")
    builder.adjust(2)  # Расположение кнопок в два столбца
    return builder.as_markup()

def back_menu():
    """
    Клавиатура с кнопкой "Назад".
    """
    builder = InlineKeyboardBuilder()
    builder.button(text="↩️ Назад", callback_data="back_to_menu")
    builder.adjust(1)
    return builder.as_markup()

def back_forecast():
    """
    Клавиатура с кнопкой "Назад".
    """
    builder = InlineKeyboardBuilder()
    builder.button(text="↩️ Назад", callback_data="open_forecast_menu")
    builder.adjust(1)
    return builder.as_markup()

def close():
    """
    Клавиатура с кнопкой "Закрыть".
    """
    builder = InlineKeyboardBuilder()
    builder.button(text="Закрыть ❌", callback_data="close")
    builder.adjust(1)
    return builder.as_markup()