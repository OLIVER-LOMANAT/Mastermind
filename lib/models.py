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
    

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    secret_number = Column(String, nullable=False)
    status = Column(String, default="in_progress")
    guesses_taken = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)

    player = relationship("Player", back_populates="games")

    guesses = relationship("Guess", secondary=game_guess_association, back_populates="games")

class Guess(Base):
    __tablename__ = 'guesses'

    id = Column(Integer, primary_key=True)
    guess_number = Column(String, nullable=False)
    bulls = Column(Integer, nullable=False)
    cows = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    games = relationship("Game", secondary=game_guess_association, back_populates="guesses")

    