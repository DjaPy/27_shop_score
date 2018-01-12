# Shop Score Page

This [applications](https://telescore.herokuapp.com/)  shows the workload of the call center store.

# About app

The app is updated every 10 seconds

Displays the following information:

1. The time of confirmation of the order.
2. The number of unconfirmed orders. 
3. The number of confirmed orders.
4. The field changes color:
  ```
  - green   - waiting less than 7 minutes
  - yellow  - waiting from 7 to 30 minures
  - red     - waiting more than 30 minutes
  ```

# Run locally

Use Venv or virtualenv for insulation project. Virtualenv example:

```
$ python virtualevn myenv
$ source myenv/bin/activate
```

Install requirements:

```
pip install -r requirements.txt
```
Run gunicorn:

At the root of the project
```
gunicorn server:app
```
and simple [click](http://localhost:8000)



# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
