# Installation process

> This README assumes that you have installed `python` (3.10.8) and `pip` (22.3).

1. Access the project directory (suggested root) via the terminal.
1. Create the virtual environment with:

    > `virtualenv <environment>`

    It is suggested to call it `env`, leaving the command as:

    > `virtualenv env`

## Enable the virtualenv of Python

> `$ .\env\Scripts\activate` \
> `(env)$ `

After this we are already inside our virtualenv, in case we no longer want to work on another virtualenv and we want to disable the current application:

> `(env)$ deactivate` \
> `$` 

## Configuration for the environment

---

Install the necessary extensions or libraries. In this case:
> `numpy==1.23.4` \
> `pandas==1.5.1` \
> `psycopg2==2.9.5` \
> `python-dateutil==2.8.2` \
> `python-dotenv==0.21.0` \
> `pytz==2022.6` \
> `six==1.16.0` \

They are installed using the `pip` of the new environment, this will be done by means of a file or file in which all the extensions will be ("requirements.txt"):

> `(env)$ pip install -r ./requirements.txt` 

This way you will be installing all the extensions, the file structure where the extensions are basically:

requirements.txt


## Location configuration of the CSV file to read

For test cases host it at the root of the project, do not add it to the repository because its size is large. You can set the CSV file name in the constant: 

> `FILE_PATH = "Stock.CSV"`