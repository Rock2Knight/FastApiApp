from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  # Инициализация приложения

# Таблица блюд
class Dish(BaseModel):
    dish_id: int              # pk id таблицы
    dish_name: str
    submenu_id: int           # внешний ключ к таблице подменю

# Таблица подменю
class Submenu(BaseModel):
    submenu_id: int               # pk id таблицы
    submenu_name: str             # название подменю
    menu_id: int                  # внешний ключ к таблице "Меню"

class Menu(BaseModel):
    title: str
    description: str

@app.get("/")
async def read_root():             # Обработка пустого get-запроса
    return {"Hello": "World"}      # выдача json-ответа {"Hello": "World"}

@app.get("/api/v1/menus/", status_code=200)       # Обработка get-запроса с индексом
async def read_menu():
    return []    # выдача json-ответа {"item_id": item_id, "q": q}

@app.get("/submenus/{submenu_id}")       # Обработка get-запроса с индексом
async def read_submenu(submenu_id: int, q: str | None = None):
    return {"submenu_id": submenu_id, "q": q}    # выдача json-ответа {"item_id": item_id, "q": q}

@app.get("/dishes/{dish_id}")       # Обработка get-запроса с индексом
async def read_dish(dish_id: int, q: str | None = None):
    return {"dish_id": dish_id, "q": q}    # выдача json-ответа {"item_id": item_id, "q": q}

@app.post("/api/v1/menus", status_code=201)
async def post_menu(menu: Menu):
    return menu

@app.get("/api/v1/menus/", status_code=200)       # Обработка get-запроса с индексом
async def read_menu(menu: Menu):
    return list([menu])    # выдача json-ответа {"item_id": item_id, "q": q}