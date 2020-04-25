# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, Numeric, Table, Unicode
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



t_m_user = db.Table(
    'm_user',
    db.Column('id', db.Unicode(20)),
    db.Column('user_name', db.Unicode(50)),
    db.Column('password',  db.Unicode(50)),
    db.Column('phone_number', db.Unicode(50)),
    db.Column('email', db.Unicode(50)),
    db.Column('create_time', db.DateTime, nullable=False)
)



