""" SQLAlchemy models """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

from .database import Base

""" Таблица SQLAlchemy "Меню" """
class Menu(Base):
    __tablename__ = "menus"

    menu_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

    submenu = relationship("Submenu", back_populates="menus")   # Связываем c таблицей подменю

""" Таблица SQLAlchemy "Подменю" """
class Submenu(Base):
    __tablename__ = "submenus"

    submenu_id = Column(Integer, primary_key=True)  # pk id таблицы
    submenu_name = Column(String)  # название подменю
    menu_id = Column(Integer, ForeignKey(Menu.menu_id))  # внешний ключ к таблице "Меню"

    menu = relationship("Menu", back_populates="submenus", cascade="all, delete-orphan") # связь с таблицей меню, с каскадным удалением
    dish = relationship("Dish", back_populates="submenus")                               # связь с таблицей блюд


""" Таблица SQLAlchemy "Блюдо" """
class Dish(Base):
    __tablename__ "dishes"

    dish_id = Column(Integer, primary_key=True)
    dish_name = Column(String)
    submenu_id = Column(Integer, ForeignKey(Submenu.submenu_id))

    submenu = relationship("Submenu", back_populates="dishes", cascade="all, delete-orphan") # связь с таблицей подменю