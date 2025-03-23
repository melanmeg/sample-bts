#!/bin/ash

# アプリ起動
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &

# マイグレーション実行
alembic -c /api-server/alembic.ini upgrade head

# バックグラウンドで実行したuvicornプロセスを待機させる
wait
