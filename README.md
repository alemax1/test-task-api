Задание: 
----
* Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
* Django Модель `Item` с полями `(name, description, price) `
* API с двумя методами:
    * GET `/buy/{id}`, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
    * GET `/item/{id}`, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном `Item` и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на `/buy/{id}`, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
Пример реализации можно посмотреть в пунктах 1-3 тут Залить решение на Github, описать запуск в Readme.md
* Выполненные доп задания:
  * Использование `environment variables`
  * Просмотр Django Моделей в Django Admin панели - username: `admin`, pass: `654654`
  * Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте



Запуск
----
```
git clone https://github.com/alemax1/test-task-api.git
python -m venv ./venv
venv/scripts/activate
pip install -r requirements.txt
python manage.py runserver
```

Сервис
----------------------------
* `admin/` - Админка с просмотром таблиц username: `admin`, pass: `654654`
* `buy/<item_id>` - купить товар
* `item/<item_id>` - страница товара
