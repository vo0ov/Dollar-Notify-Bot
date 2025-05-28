import aiohttp
import defusedxml.ElementTree as ET

# URL для получения курсов валют ЦБ РФ
CBR_URL = 'https://www.cbr-xml-daily.ru/daily.xml'


async def get_usd_rate() -> float:
    """
    Асинхронно получает текущий курс доллара (USD) к рублю с сайта ЦБ РФ.

    Возвращает:
        float: курс 1 USD в RUB

    Исключения:
        ValueError: если в XML нет информации по доллару США
    """

    # Открываем асинхронную HTTP-сессию
    async with aiohttp.ClientSession() as session:
        # Отправляем GET-запрос к ЦБ РФ
        async with session.get(CBR_URL) as resp:
            # Получаем ответ как текст (XML)
            text = await resp.text(encoding='windows-1251')

            # Парсим XML безопасным парсером
            tree = ET.fromstring(text)

            # Перебираем все элементы <Valute> (валюты)
            for valute in tree.findall('Valute'):
                # Получаем дочерний элемент <CharCode> (буквенный код валюты)
                char_code = valute.find('CharCode')

                # Если это доллар США
                if char_code is not None and char_code.text == 'USD':
                    # Получаем значение курса (<Value>) и номинал (<Nominal>)
                    value = valute.find('Value')
                    nominal = valute.find('Nominal')

                    # Если оба значения найдены
                    if value is not None and nominal is not None:
                        # Значение приходит с запятой — заменяем на точку, делим на номинал (обычно 1)
                        return float(value.text.replace(',', '.')) / int(nominal.text)

            # Если не найден доллар — выбрасываем ошибку
            raise ValueError('USD not found in CBR XML')
