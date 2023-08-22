""" HTTP methods """
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import  Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)   # Create the database tables

app = FastAPI()  # Инициализация приложения

# Dependency (create new session)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root():             # Обработка пустого get-запроса
    return {"Hello": "World"}      # выдача json-ответа {"Hello": "World"}


""" Read menu list """
@app.get("/api/v1/menus/", response_model=list[schemas.Menu], status_code=200)       # Обработка get-запроса с индексом
async def read_menus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    menus = crud.get_menus(db, skip=skip, limit=limit)  # get menu list

    if not menus:
        return []    # выдача пустого списка меню
    return menus     # Выдача непустого списка меню


""" Create a new menu """
@app.post("/api/v1/menus", response_model=schemas.Menu, status_code=201)
async def create_menu(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    return crud.create_menu(db=db, menu=menu)


""" Issuance concrete menu """
@app.get("/api/v1/menus/{menu_id}", response_model=schemas.Menu, status_code=200)       # Обработка get-запроса с индексом
async def read_menu(menu_id: int, db: Session = Depends(get_db)):

    db_menu = crud.get_menu(db, menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="Menu is not found")
    return db_menu

"""
@app.patch("/api/v1/menus/{menu_id}", status_code=200)
async def patch_menu(menu: Menu, menu_id: int):
    id_last = list(myMenu.keys())[-1]

    if not myMenu or id_last < menu_id:
        return None
    else:
        myMenu[menu_id].title = menu.title
        myMenu[menu_id].description = menu.description

        return myMenu[menu_id]
"""

"""
@app.delete("/api/v1/menus/{menu_id}", status_code=200)
async def delete_menu(menu_id: int):
    id_list = list(myMenu.keys())

    if menu_id in id_list:
        myMenu.pop(menu_id)
"""


""" Get all submenus in menu with concrete menu_id """
@app.get("/api/v1/menus/{menu_id}/submenus", response_model=list[schemas.Submenu], status_code=200)       # Обработка get-запроса с индексом
async def read_submenus(menu_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    submenus = crud.get_submenus(db, menu_id=menu_id, skip=skip, limit=limit)
    return submenus


""" Create a new submenu """
@app.post("/api/v1/menus/{menu_id}/submenu", response_model=schemas.Submenu, status_code=201)
async def create_submenu(menu_id: int, submenu: schemas.SubmenuCrete, db: Session = Depends(get_db)):
    return crud.create_submenu(db, submenu=submenu, menu_id=menu_id)


""" Get the submenu with submenu_id from the menu with menu_id"""
@app.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}", response_model=schemas.Submenu, status_code=200)       # Обработка get-запроса с индексом
async def read_submenu(submenu_id: int, db: Session = Depends(get_db)):
    db_menu = crud.get_menu(db, submenu_id)


"""
@app.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}", status_code=200)
async def patch_menu(submenu: Submenu, menu_id: int, submenu_id: int):

    if not myMenu:
        return None

    id_last = list(myMenu.keys())[-1]
    if id_last < menu_id:
        return None

    if not submenuList:
        return None

    id_last = list(submenuList.keys())[-1]
    if id_last < submenu_id:
        return None

    submenuList[submenu_id].title = submenu.title
    submenuList[submenu_id].description = submenu.description

    return submenuList[submenu_id]
"""

"""
@app.get("/dishes/{dish_id}")       # Обработка get-запроса с индексом
async def read_dish(dish_id: int, q: str | None = None):
    return {"dish_id": dish_id, "q": q}    # выдача json-ответа {"item_id": item_id, "q": q}
"""