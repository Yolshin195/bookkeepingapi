# Bookkeeping API
Bookkeeping API - это api для управления своими финансами.

## Функции
### Авторизация и Аутентификация
1. [ ] Регистрация
2. [ ] Авторизация
### Учет расходов и доходов
1. [ ] Регистрация расходов в простом формате, категория и сумма
2. [ ] Мультивалютный учет
3. [ ] Основные валюты: Доллар и одна на выбор
4. [ ] Возможность задать счёт расхода по умолчанию
5. [ ] Отражение расходов за день, неделю, месяц, год
6. [ ] Возможность создания бюджета на категорию, неделя, месяц
7. [ ] Настройка сигнальных и контрольных значений для бюджета
8. [ ] Вывод отчёта в разрезе, расходы, доходы, остаток за неделю, месяц, год, всё время
9. [ ] Возможность вести учёт в группе
10. [ ] Разные пользователи должны иметь возможность вести параллельный учёт без пересечения
### Курсы валют
1. [ ] Конвертация валют
2. [ ] Получить текущий курс
3. [ ] Загрузка курсов валют
### Web Клиент
1. [ ] Web клиент - Поддержка всего функционала
### Telegram bot
[Telegram bot](https://github.com/Yolshin195/bookkeepingbot)
1. [ ] Регистрации расходов
2. [ ] Просмотр расходов за день, месяц, год
3. [ ] Получение уведомления при приближении к сигнальным и контрольным значениям бюджета по категории

## SQLAlchemy

### Alembic
```commandline
alembic init migrations
alembic revision --autogenerate -m "Database creation"
alembic upgrade a6bb65055ddb            // Revision ID
```

Схема базы данных
Операции
	id
	Тип операции
	дата
	счёт расхода
	расход
	счёт дохода
	доход
	категория
	комментарий

Тип операции
	id
	code
	name
	description

Счёт
	id
	code
	name
	description
	валюта

Валюта
	id
	code
	name
	description

Категория
	id
	code
	name
	description
	

telegramClient

/start

/typeOperation
Доход
Расход
Перевод

/createOperation


#Python, #FastAPI, #FastAPI-Users #SqlAlchemy, #Alembic
