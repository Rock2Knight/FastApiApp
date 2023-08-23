""" Pydantic models (Schemas) """
from pydantic import BaseModel

class DishBase(BaseModel):
    dish_name: str

class DishCreate(DishBase):
    pass

class Dish(DishCreate):
    dish_id: int

    class Config:
        orm_mode = True


class SubmenuBase(BaseModel):
    submenu_name: str  # название подменю

class SubmenuCrete(SubmenuBase):
    pass

class Submenu(SubmenuCrete):
    submenu_id: int
    #menu_id: int  # внешний ключ к таблице "Меню"
    menus: list[Dish] = []

    class Config:
        orm_mode = True


class MenuBase(BaseModel):
    title: str
    description: str | None = None

class MenuCreate(MenuBase):
    pass

class Menu(MenuCreate):
    menu_id: int
    submenus: list[Submenu] = []

    class Config:
        orm_mode = True