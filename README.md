# Giya

An awesome REST boilerplate that uses Flask-RESTX (formerly Flask-RESTPlus).
It has the usual API features to get you started and off the ground,
it's also designed to be easily scalable and extendable.

I wrote this boilerplate because I found that a lot of Flask REST boilerplates are either
doing too much, is lacking, or it simply doesn't fit my needs.


# Features

* Full featured framework for fast, easy, and documented API with [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/)
* JSON Web Token Authentication with [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
* Swagger Documentation (Part of Flask-RESTX).
* Unit Testing.
* Database ORM with [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* Database Migrations using [Flask-Migrate](https://github.com/miguelgrinberg/flask-migrate)
* Object serialization/deserialization with [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* Data validations with Marshmallow [Marshmallow](https://marshmallow.readthedocs.io/en/stable/quickstart.html#validation)

## Flask CLI help command output:
```sh
Usage: flask [OPTIONS] COMMAND [ARGS]...

  A general utility script for Flask applications.

  Provides commands from Flask, extensions, and the application. Loads the
  application defined in the FLASK_APP environment variable, or from a
  wsgi.py file. Setting the FLASK_ENV environment variable to 'development'
  will enable debug mode.

    $ export FLASK_APP=hello.py
    $ export FLASK_ENV=development
    $ flask run

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  db      Perform database migrations.
  routes  Show the routes for the app.
  run     Run a development server.
  shell   Run a shell in the app context.
  test    Run unit tests
```

# Pre-requisites

This boilerplate uses `SQLite` as its database, make sure you have it installed.
`Pipenv` is recommended to help manage the dependencies and virtualenv.

You can also use other DBs like `PostGreSQL`, make sure you have it setup and update your `DATABASE_URL` in your configs.
Read more at [Flask-SQLAlchemy's](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) documentations.

It uses [Black](https://github.com/psf/black) for code styling/formatting.

# Usage

## Notes

By default the `/` route is used by the `auth` blueprint.

The rest of the resources are found in `/api` (This is the docs route by default, this can be changed easily).

**Note**: Pipenv seems to have been becoming unmaintained or unsupported, so `virtualenv` is recommended to manage your packages and Python environment, hence why `requirements.txt` has been generated.

## Installing with Pipenv
```sh
# Clone the repo
$ git clone https://github.com/X1Zeth2X/flask-restx-boilerplate.git

# Install packages with pipenv
$ pipenv install
```

## Running
Please specify your app's environment variables in a `.env` file, otherwise Flask CLI wouldn't find your app.

```sh
# .env file example
export FLASK_APP=giya

# configs: production, testing, development, and default (uses DevelopmentConfig)
export FLASK_CONFIG=development

# Another way of assigning environment variables is:
FLASK_APP=giya
FLASK_CONFIG=development

# Read more at https://github.com/theskumar/python-dotenv
```

```sh
# Enter the virtualenv
$ pipenv shell

# (Optional for development, recommended)
$ flask db init # Initializes a new SQLite database.
$ flask db migrate # Creates the tables in the database.

# Run the app
$ flask run
```

## Unit testing
Giya has already some unit tests written, we encourage adding more unit tests as you scale.

```sh
# Unit testing
$ flask test

# Run specific unit test(s)
$ flask test tests.test_auth_api tests.test_user_model ...
```

## Swagger
- 自带的css文件里有个`td:first-of-type`的`padding`值改从`10px`为`25px`；Code与Description才能对齐

## 将数据库表结构转成model.py文件
```mysql
-- 每张表都应该有这两个时间，代码就不用处理了
`create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP comment '创建时间',
`update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP comment '更新时间',
```

把数据库转成model.py文件
```mysql

flask-sqlacodegen 'sqlite:///data-dev.sqlite' --tables user --outfile "app/models/user2.py"  --flask
flask-sqlacodegen 'mysql+pymysql://root:12345678@localhost/jinchu_order_menu' --tables product_order --outfile "common/models/product/tt.py"  --flask

```
