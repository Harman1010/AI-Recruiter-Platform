from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):

    """A blueprint for working with reusable parameters"""

    gemini_api_key : str

    database_url : str

    model_config = SettingsConfigDict(
        env_file=".env"
    )

    #docker_database_url : str

settings = Settings()