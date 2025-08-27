from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///bulls_and_bulls.db')
Session = sessionmaker(bind=engine)
session = Session()

game_guess_association = Table(
    'game_guesses',
    Base.metadata,
    Column('game_id', Integer, ForeignKey('games.id'), primary_key=True)
    Column('guess_id', Integer, ForeignKey('guesses.id'), primary_key=True)
)

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    games = relationship("Game", back_populates="player")

    def __repr__(self):
        return f"<Player {self.username}>"
    
    
