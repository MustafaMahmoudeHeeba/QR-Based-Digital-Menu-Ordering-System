from fastapi import FastAPI

from app.routers.menu import router as menu_router


app = FastAPI(
    title="QR Menu API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "QR Menu API is running 🚀"
    }


app.include_router(menu_router)