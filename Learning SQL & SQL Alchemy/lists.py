import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    fligts = db.execute("select * from Users").fetchall()

    for flight in fligts:
        print(flight)


if __name__== "__main__":
    main()