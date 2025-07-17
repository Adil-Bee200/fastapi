from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    database_url: str | None = None

    database_hostname : str
    database_port : str
    database_password : str
    database_name : str 
    database_username : str
    secret_key : str 
    algorithm : str 
    access_token_expire_minutes : str

    @property
    def sqlalchemy_database_url(self):
        if self.database_url:
            return self.database_url
        return (
            f'postgresql://{self.database_username}:{self.database_password}@{self.database_hostname}:{self.database_port}/{self.database_name}'
        )

    class Config:
        env_file = ".env"

settings = Settings()