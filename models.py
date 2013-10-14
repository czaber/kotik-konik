from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///kotik.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    uid = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    avatar = Column(String)
    university = Column(String)
    faculty = Column(String)
    year_of_study = Column(Integer)
    github_username = Column(String)
    reddit_username = Column(String)
    linux_distribution = Column(String)
    known_technologies = Column(String)
    wants_to_learn = Column(String)
    willingness_to_attend_meetings = Column(String)
    active = Column(Boolean, nullable=False, default=False)
    given_answers = relationship("GivenAnswer")

    def __init__(self, firstname, lastname, nickname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.email = email

    def __repr__(self):
       fullname = "%s %s" % (self.firstname, self.lastname)
       return "<User('%s','%s', '%s', '%s')>" % (fullname, self.nickname, self.email)

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answers = relationship("Answer")

    def __init__(self, question):
        self.question = question

    def __repr__(self):
       return "<Question('%i', '%s')>" % (self.id, self.question)

class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    answer = Column(String, nullable=False)
    correct = Column(Boolean, nullable=False, default=False)
    question_id = Column(Integer, ForeignKey('questions.id'))
    given_answers = relationship("GivenAnswer")

    def __init__(self, answer, correct):
	self.answer = answer
	self.correct = correct

    def __repr__(self):
       return "<Answer('%i', '%i')>" % (self.id, self.question_id)

class GivenAnswer(Base):
    __tablename__ = 'givenanswers'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.uid'))
    answers_id = Column(Integer, ForeignKey('answers.id'))
    checked = Column(Boolean, nullable=False, default=False)

    def __init__(self, checked):
	self.checked = checked

    def __repr__(self):
       return "<GivenAnswer('%i')>" % (self.id)


users_table = User.__table__
questions_table = Question.__table__
answers_table = Answer.__table__
given_answers_table = GivenAnswer.__table__
metadata = Base.metadata
metadata = Base.metadata

if __name__ == "__main__":
    metadata.create_all(engine)
