import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy_utils import database_exists, create_database
import time

# waiting 1 sec db to start
time.sleep(1)
DATABASE_URI = os.getenv("DATABASE_URL")
db_engine = create_engine(DATABASE_URI)
base = declarative_base()


class Wizards(base):
    __tablename__ = 'wizards'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    side = Column(String(30))
    birthday = Column(DateTime(timezone=True))
    is_alive = Column(Boolean)
    power = Column(Integer)

    # one to many
    wizards_slogans = relationship("WizardsSlogans", cascade="all,delete", backref="wizards")
    # one to one
    short_story = relationship("ShortStory", cascade="all,delete", uselist=False, backref="wizards")

    def __repr__(self):
        return f'id = {self.id}: name = {self.name}, side = {self.side}, birthday = {self.birthday}, ' \
               f'is_alive = {self.is_alive}, power = {self.power}'


class WizardsSlogans(base):
    __tablename__ = 'wizards_slogans'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey('wizards.id'))
    moto_id = Column(Integer)
    moto = Column(String(100), unique=True)

    def __repr__(self):
        return f'id = {self.id}: hero_id = {self.hero_id}, moto_id = {self.moto_id}, moto = {self.moto}'


class ShortStory(base):
    __tablename__ = 'short_story'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey('wizards.id'), unique=True)
    story = Column(String(200))

    def __repr__(self):
        return f'id = {self.id}: hero_id = {self.hero_id}, story = {self.story}'


class WizardsClashes(base):
    __tablename__ = 'wizards_clashes'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    hero_1_id = Column(Integer,ForeignKey('wizards.id',ondelete='SET NULL'), nullable=True)
    hero_1_moto_id = Column(Integer, ForeignKey('wizards_slogans.id',ondelete='SET NULL'), nullable=True)
    hero_2_id = Column(Integer,ForeignKey('wizards.id',ondelete='SET NULL'), nullable=True)
    hero_2_moto_id = Column(Integer, ForeignKey('wizards_slogans.id',ondelete='SET NULL'), nullable=True)
    winner = Column(Integer)

    def __repr__(self):
        return f' Id = {self.id}: hero_1_id = {self.hero_1_id}, hero_1_moto_id = {self.hero_1_moto_id}, hero_2_id = {self.hero_2_id}, ' \
               f'hero_2_moto_id = {self.hero_2_moto_id}, winner = {self.winner}'


# Create database if it does not exist.
if not database_exists(db_engine.url):
    create_database(db_engine.url)
else:
    # Connect the database if exists.
    db_engine.connect()

base.metadata.create_all(db_engine)
Session = sessionmaker(bind=db_engine)


