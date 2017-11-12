# Test-Driven Development with Python

## Introduction

Just me learning Test-Driven Development with Python, Django, Selenium, and JavaScript. For most of the time, I am following the steps from [Test-Driven Development with Python: Obey the Testing Goat: Using Django, Selenium, and JavaScript *by Harry J. W. Percival*](https://www.amazon.com/Test-Driven-Development-Python-Selenium-JavaScript/dp/1491958707) book that is available on [`obeythetestinggoat.com`](https://www.obeythetestinggoat.com/)

I intentionally take it to the extreme and see what else I can test.

In this `README`, I also added some tasks that I still need to do. They are a reminder for myself.

- [ ] task to do
- [x] task done!

## Up and Running

### Install

I recommend using [`venv`](https://docs.python.org/3/library/venv.html) for creating a virtual environment, until I containerize this app.

1. Use modern Python.
    
    ```bash
    $ python --version
    Python 3.6.2
    ```
    
2.  Create a virtual environment for your project and double-check [`pip`](https://en.wikipedia.org/wiki/Pip_(package_manager)) is installed.

    ```
    $ python -m venv venv
    $ source venv/bin/activate
    (venv) $ pip --version
    pip 9.0.1 
    ```
    
    - [ ] Activate virtual environment on `cd`ing into a directory.
    - [ ] Change name of the virtual environment

3. Install requirements with `pip`

    ```
    $ pip install -r requirements.txt
    ```
    
    
### Tests

#### Prerequisites

* `selenium` will be installed with `pip`
* You can install [`geckodriver`](https://github.com/mozilla/geckodriver) manually from their [GitHub Releases](https://github.com/mozilla/geckodriver/releases) page or use the script I wrote to fetch it
    
    ```
    $ bash install-geckodriver.sh
    ```

#### Run tests

```
$ python -m unittest discover tests
$ python manage.py test
```

## etc

[Project Avatar Image](https://www.pexels.com/photo/agriculture-animals-baby-blur-288621/)