""" CRUD operations (Create, Read, Update, Delete) """
from sqlalchemy.orm import Session

from . import models, schemas

""" Получить подменю из списка подменю по id """
def get_submenu(db: Session, submenu_id: int):
    return db.query(models.Submenu).filter(models.Submenu.submenu_id == submenu_id).first()


""" Получить подменю по названию """
def get_submenu_name(db: Session, submenu_name: str):
    return db.query(models.Submenu).filter(models.Submenu.submenu_name == submenu_name).first()


""" Получить список подменю со смещением 0 количеством 100 """
def get_submenus(db: Session, menu_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Submenu).filter(models.Submenu.menu_id == menu_id).offset(skip).limit(limit).all()


""" Создание подменю """
def create_submenu(db: Session, submenu: schemas.SubmenuCrete, menu_id):
    db_submenu = models.Submenu(**submenu.model_dump(), menu_id=menu_id)
    #db_submenu = models.Submenu(submenu_name=submenu.submenu_name)  # Создаем модель(запись) подменю
    db.add(db_submenu)                                              # Добавляем модель(запись) в базу
    db.commit()                                                     # сохраняем изменения
    db.refresh(db_submenu)                                          # обновляем запись
    return db_submenu

""" Получить конкретное меню """
def  get_menu(db: Session, menu_id: int):
    return db.query(models.Menu).filter(models.Menu.menu_id == menu_id).first()


""" Получить список меню со смещением 0 количеством 100 """
def get_menus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Menu).offset(skip).limit(limit).all()


""" Создание меню """
def create_menu(db: Session, menu: schemas.MenuCreate):
    db_menu = models.Menu(**menu.model_dump())                     # Создаем модель(запись) меню
    db.add(db_menu)                                                # Добавляем модель(запись) в базу
    db.commit()                                                    # сохраняем изменения
    db.refresh(db_menu)                                            # обновляем запись
    return db_menu