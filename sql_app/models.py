""" SQLAlchemy models """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, backref

from sql_app.database import Base

""" Таблица SQLAlchemy "Меню" """
class Menu(Base):
    __tablename__ = "menus"

    menu_id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String)
    description = mapped_column(String)

    submenu = relationship("Submenu", back_populates="menu", cascade="all, delete-orphan")   # Связываем c таблицей подменю

""" Таблица SQLAlchemy "Подменю" """
class Submenu(Base):
    __tablename__ = "submenus"

    submenu_id = mapped_column(Integer, primary_key=True)  # pk id таблицы
    submenu_name = mapped_column(String)  # название подменю
    menu_id = mapped_column(Integer, ForeignKey(Menu.menu_id))  # внешний ключ к таблице "Меню"

    menu = relationship("Menu", backref=backref("submenu", cascade="all, delete-orphan")) # связь с таблицей меню, с каскадным удалением
    dish = relationship("Dish", back_populates="sub", cascade="all, delete-orphan")                               # связь с таблицей блюд


""" Таблица SQLAlchemy "Блюдо" """
class Dish(Base):
    __tablename__ = "dishes"

    dish_id = mapped_column(Integer, primary_key=True)
    dish_name = mapped_column(String)
    submenu_id = mapped_column(Integer, ForeignKey(Submenu.submenu_id))

    #sub = relationship("Submenu", backref=backref("dish", cascade="all, delete-orphan")) # связь с таблицей подменю