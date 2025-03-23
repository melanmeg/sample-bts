import os
from logging.config import dictConfig
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import endpoints

app = FastAPI()

app.include_router(endpoints.router)

# ログファイルのディレクトリを作成（存在しない場合）
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# ロギング設定
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "access_log": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "midnight",
            "interval": 1,
            "backupCount": 15,
            "filename": os.path.join(log_directory, "access.log"),
            "formatter": "default",
        },
        "error_log": {
            "level": "ERROR",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "midnight",
            "interval": 1,
            "backupCount": 15,
            "filename": os.path.join(log_directory, "error.log"),
            "formatter": "default",
        },
        "exception_log": {
            "level": "ERROR",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "midnight",
            "interval": 1,
            "backupCount": 15,
            "filename": os.path.join(log_directory, "exception.log"),
            "formatter": "default",
        },
    },
    "loggers": {
        "uvicorn.access": {
            "handlers": ["access_log"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.error": {
            "handlers": ["error_log"],
            "level": "ERROR",
            "propagate": False,
        },
        "app.exception": {
            "handlers": ["exception_log"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}

dictConfig(LOGGING_CONFIG)


@app.get("/")
def root() -> Any:
    return {"message": "Hello, world!"}
