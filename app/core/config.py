from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central configuration for the NexusAI application."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # ── Project Info
    PROJECT_NAME: str = "NexusAI"
    VERSION: str = "0.1.0"
    DEBUG: bool = False

    # ── API Keys 
    GOOGLE_API_KEY: str  # required — will raise at startup if missing

    # ── Text Chunking 
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200

    # ── LLM Settings 
    LLM_MODEL: str = "gemini-2.0-flash"
    EMBEDDING_MODEL: str = "models/embedding-001"
    LLM_TEMPERATURE: float = 0.3

    # ── Vector Search 
    SIMILARITY_TOP_K: int = 5


settings = Settings()
