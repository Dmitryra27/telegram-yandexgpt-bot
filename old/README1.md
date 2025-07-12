# Telegram Бот с YandexGPT и WebApp интерфейсом

Этот проект — Telegram-бот с поддержкой YandexGPT и WebApp интерфейсом внутри Telegram. 
Можно развернуть на [Railway](https://railway.app ).

## Установка

### Через Railway:

1. Перейди на [railway.app/project/new](https://railway.app/project/new )
2. Выбери свой GitHub-репозиторий или загрузи ZIP
3. Добавь переменные окружения:
    - `TELEGRAM_BOT_TOKEN` – токен Telegram-бота
    - `YANDEX_API_KEY` – ключ от Yandex Cloud
    - `YANDEX_FOLDER_ID` – ID папки в Yandex Cloud
4. Бот будет доступен через Telegram

### Через GitHub:

1. Создай новый репозиторий на GitHub
2. Закоммить все файлы из этого проекта
3. Подключи к Railway через GitHub
4. Добавь переменные окружения

## Использование

- `/start` – откроет WebApp интерфейс
- Любой текст – отправит запрос в YandexGPT и получит ответ

## Лицензия

MIT
