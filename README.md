# test_stripe
# Введение
Реализовано Django + Stripe API приложение со следующим функционалом и условиями:

#Функционал
1. Django Модель Item с полями (name, description, price, key) `key: ключ получения цены из аккаунта Stripe. Например: price_1Mb5xhJLtPVKs6Q3TKwnPdn4`
2. API с двумя методами:
a. `GET /buy/{id}`, c помощью которого можно получить `Stripe Session Id` для оплаты выбранного `Item`.
b. `GET /item/{id}`, c помощью которого можно получить HTML страницу, на которой будет информация о выбранном Item и кнопка Buy.
3. В админ панели можно выполнять CRUD операции над содержимым модели `Item`.
4. Если перейти на `http://localhost:8000/`, можно получить HTML страницу, на которой будет информация о всех Item и в форме можно выбрать какой Item мы хотим приобрести. По клику `checkout` будет создаваться сессия Stripe с перенаправлением на checkout_session.url.

