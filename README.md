
# Django + Stripe API backend

App creates Stripe sesssion for chosen product and redirects to paying link. Now you can choose only one product to pay. In future I'm going to realize creating payong link for full order with several products.

## Watch app on Heroku

[Django_Stripe](https://tap-django-stripe.herokuapp.com)



## Run Locally

Clone the project

```bash
  git clone git@github.com:vap3003/test_Django_Stripe.git
```

Go to the project directory

```bash
  cd test_Django_Stripe
```

Create and activate Virtual Environments

```bash
  python3 -m venv venv
  source venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Create '.env' file and fill all Config vars, according to '.env.example'

```bash
  cd djangostripe
  touch .env
```

Create migrations

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Run a server

```bash
  python manage.py runserver
```

## API Reference

#### Get product page

```http
  GET /item/${id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `integer` | **Required**. Id of item |

#### Redirect to paying link

```http
  GET /buy/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of item|




## Author

- [@vap3003](https://www.github.com/vap3003)
