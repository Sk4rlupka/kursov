from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from users.router import get_users

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates")


@router.get("/base")
def get_base_page(request: Request, users = Depends(get_users)):
    return templates.TemplateResponse("base.html", {"request": request, "users": users})