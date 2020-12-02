
#!flask/bin/python
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://admin:Pass_12345678@localhost/RTU")
Base = declarative_base()
Base.metadata.reflect(engine)

from sqlalchemy.orm import relationship, backref

class point(Base):
    __table__ = Base.metadata.tables['point']

if __name__ == '__main__':
    from sqlalchemy.orm import scoped_session, sessionmaker, Query
    db_session = scoped_session(sessionmaker(bind=engine))
    data=db_session.query(point.id_point,point.flag_station_slot,point.name_point,
                                point.point_position,point.id_slot,point.id_station)
    print(data)
    for item in data:
        print(item)