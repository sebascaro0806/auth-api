from sqlalchemy import MetaData, create_engine
from src.config.setup import settings


engine = create_engine("postgresql://" + settings.DB_USER + ":" + settings.DB_USER_PASSWORD + "@" + settings.DB_HOST + "/" + settings.DB)

meta_data = MetaData()