# singlenton class
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import QueuePool

from commons import constants
from db.models import Base


class db_connection:
    class __db_connection:
        _engine = None
        _session = None

        def __init__(self):
            self._engine = sqlalchemy.create_engine("mysql+pymysql://" + constants.DB_USERNAME +
                                                    ":" + constants.DB_PWD + '@' + constants.DB_URL +
                                                    "/" + constants.DB_NAME + "?charset=utf8", encoding='utf-8',
                                                    poolclass=QueuePool)
            Base.metadata.create_all(self._engine)
            self._session = scoped_session(sessionmaker(bind=self._engine, autoflush=False))

        def get_session(self):
            return self._session

        def commit(self):
            try:
                self._session.commit()
            except:
                self._session.rollback()
                raise

        def close_connection(self):
            try:
                if self._session:
                    self._session.remove()
                if self._engine:
                    self._engine.dispose()
            except Exception as ex:
                print(ex)

    instance = None

    def __init__(self):
        if not db_connection.instance:
            db_connection.instance = db_connection.__db_connection()

    def __getattr__(self, name):
        return getattr(self.instance, name)