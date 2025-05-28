[![wakatime](https://wakatime.com/badge/github/vo0ov/dollar-notify-bot.svg)](https://wakatime.com/badge/github/vo0ov/dollar-notify-bot)

# Dollar Notify Bot

Telegram-бот для мониторинга курса доллара (USD) к рублю с уведомлениями о каждом изменении.
Работает только для владельца (OWNER_ID). Использует данные с официального сайта ЦБ РФ.

## 🚀 Быстрый старт

1. **Склонируй репозиторий**

    ```sh
    git clone https://github.com/vo0ov/dollar-notify-bot.git
    cd dollar-notify-bot
    ```

2. **Создай .env на основе .env.sample**

    ```sh
    cp .env.sample .env
    ```

    Заполни токен бота, ID владельца и нужный интервал проверки.

3. **Запусти через Docker Compose**

    ```sh
    docker-compose up --build
    ```

## ⚙️ Настройки (файл `.env`)

| Переменная     | Описание                             |
| -------------- | ------------------------------------ |
| BOT_TOKEN      | Токен Telegram-бота                  |
| OWNER_ID       | Telegram ID владельца (админа)       |
| CHAT_ID        | ID чата (дублирует OWNER_ID)         |
| CHECK_INTERVAL | Интервал проверки курса (в секундах) |

## 📦 Стек

-   Python 3.12+
-   aiogram 3.x
-   aiohttp
-   defusedxml
-   pydantic-settings
-   Docker + Alpine

## 📝 Возможности

-   Уведомляет о каждом изменении курса USD к RUB (по данным ЦБ РФ)
-   Работает строго для одного пользователя (owner)
-   Надёжная работа цикла (устойчива к изменению времени и сбоям)
-   Команды: `/start`, `/help`, `/course`

## 💡 Пример использования

1. Запусти бота.
2. Получай уведомления при каждом изменении курса доллара.
3. В любой момент используй команду `/course` для ручного запроса курса.

## 🏷️ Лицензия на программное обеспечение «Dollar Notify Bot»

```text
The MIT License (MIT)

Copyright © 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
