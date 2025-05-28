# Импортируем базовый образ Python
FROM python:alpine

# Установим рабочую директорию
WORKDIR /app

# Скопируем зависимости и установим их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопируем исходники проекта
COPY . .

# Указываем переменные окружения
ENV PYTHONUNBUFFERED=1

# Запуск бота
CMD ["python", "main.py"]
