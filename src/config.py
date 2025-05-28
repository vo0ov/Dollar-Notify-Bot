from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str  # Токен Telegram-бота
    owner_id: int  # ID владельца бота
    chat_id: int    # ID чата/группы для уведомлений
    check_interval: int = 3600  # Интервал проверки (сек)

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )


settings = Settings()
