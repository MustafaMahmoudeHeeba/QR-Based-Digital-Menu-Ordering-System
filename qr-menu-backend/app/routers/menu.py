from fastapi import APIRouter

router = APIRouter(
    prefix="/menu",
    tags=["Menu"]
)


@router.get("/")
def get_menu():
    return {
        "message": "Menu endpoint",
        "items": []
    }