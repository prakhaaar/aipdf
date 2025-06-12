from db.database import Base, engine
from db.models import PDF  # ensure model is imported

def init_db():
    Base.metadata.create_all(bind=engine)
