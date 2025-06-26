from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from app.api.v1.web import router as web_router

app = FastAPI(title="My API")


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(
        title=app.title,
        version="1.0.0",
        routes=app.routes,
    )
    # Определяем схему bearerAuth
    schema.setdefault("components", {}) \
          .setdefault("securitySchemes", {})["bearerAuth"] = {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
    }
    # Добавляем её ко всем операциям по умолчанию
    for path_item in schema["paths"].values():
        for operation in path_item.values():
            operation.setdefault("security", []).append({"bearerAuth": []})

    app.openapi_schema = schema
    return schema


app.openapi = custom_openapi


# CORS — разрешаем фронту на 8000/8001
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:8001",
        "http://127.0.0.1:8001",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Все ваши веб-роуты в одном месте
app.include_router(web_router)