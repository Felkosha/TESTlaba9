# Лабораторная работа 9: автотесты в CI/CD (GitHub Actions)

Проект содержит простой модуль `app/calculator.py`, автотесты `tests/test_calculator.py`
и workflow `.github/workflows/run-tests.yml`, который запускает `pytest` при каждом push.

## Локальный запуск

```
pip install -r requirements.txt
pytest -v
```

## CI

При push в ветку `main`/`master` GitHub Actions автоматически:
1. разворачивает ОС (ubuntu-latest),
2. устанавливает Python 3.11,
3. устанавливает зависимости,
4. запускает `pytest`.
