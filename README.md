# MMORPG Community Blog
[![Django](https://img.shields.io/badge/Django-5.1-green)](https://www.djangoproject.com/)  
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/) 


**MMORPG Blog** — это веб-платформа для публикации объявлений и обсуждений в тематике MMORPG-игр. Пользователи могут создавать объявления, оставлять отклики и управлять контентом через интуитивный интерфейс.

---

## 🛠️ Технологии

### Backend 
- **Backend**: Python 3.11, Django 5.1
- **База данных**: SQLite
- **Аутентификация**: `django-allauth` (email)
- **Редактор**: CKEditor (`django-ckeditor`)  
- **Поиск**: Django ORM (`icontains`) 
- **Дополнительно**:
  - Загрузка изображений (`ImageField`)
  - Фильтрация объявлений по категориям
  - Пагинация и сортировка
## 🎨 Интерфейс
- **Шаблоны**: Django Templates (серверный рендеринг)
- **Стили**: Bootstrap 5 (через CDN) + кастомный CSS
- **Редактор текста**: Django CKEditor
- **JavaScript**: Нативный JS (без фреймворков)
---

## ⚙️ Установка и запуск  

### 1. Клонирование репозитория  
```bash  
git clone https://github.com/DiMiRka/MMORPG_blog.git  
cd MMORPG_blog
```
### 2. Создайте и активируйте виртуальное окружение
```bash  
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate  # Для Windows
```
### 3. Установите зависимости
```bash  
pip install -r requirements.txt
```
### 4. Примените миграции
```bash  
python manage.py migrate
```
### 5. Создайте суперпользователя (опционально)
```bash  
python manage.py createsuperuser
```
### 6. Запустите сервер
```bash  
python manage.py runserver
```
### Откройте в браузере: http://127.0.0.1:8000

## 📚 Функционал
### 🔐 Пользователи
- Регистрация и вход через логин/пароль
- Личный кабинет с объявлениями и откликами
### 📢 Объявления
- Создание/редактирование и удаление объявлений с форматированным текстом (CKEditor)
- Прикрепление изображений
- Фильтрация по категориям
- Поиск по автору, названию, категории, дате публикации
### 💬 Отклики
- Публикация откликов на объявления
- Принятие/отклонение откликов (для авторов объявлений)

