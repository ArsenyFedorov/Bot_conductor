import sqlite3
from data_base.data_base import DataBase
from aiogram.types import CallbackQuery


class DayOfSport(DataBase):

    def __init__(self, data):
        if isinstance(data, CallbackQuery):
            self.tg_id = data.from_user.id
            self.name = data.from_user.first_name
            self.datetime = None
            self.status = "Не подтверждён"
            self.create()
            sport = self.load(tg_id=self.tg_id)
            self.tg_id, self.name, self.datetime, self.status = sport
        elif isinstance(data, str):
            self.datetime = data
            sport = self.load(day=self.datetime)
            self.tg_id, self.name, self.datetime, self.status = sport

    @staticmethod
    def great_table():
        sql = '''CREATE TABLE IF NOT EXISTS sport
                                 (tg_id INTEGER, name TEXT,
                                 datetime DATETIME, status TEXT)'''
        DayOfSport.execute(sql, commit=True)

    def load(self, **kwargs):
        sql = """SELECT * FROM sport WHERE """
        sql, parameters = self.extract_kwargs(sql, kwargs)
        sport = self.execute(sql, parameters, fetchone=True)
        return sport

    def save(self):
        sql = """UPDATE sport SET """
        sql, parameters = self.extract_kwargs(sql, self.__dict__, _and=False)
        sql = sql + f" WHERE tg_id={self.tg_id}"
        self.execute(sql, parameters, commit=True)

    def create(self):
        sql = """INSERT INTO sport(tg_id,name,datetime, status) VALUES (?,?,?,?)"""
        self.execute(sql, (self.tg_id, self.name, self.datetime, self.status), commit=True)
