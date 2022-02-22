# Project description

This project is to build a backend based on `Django` framework with an application named `user`. The application is able to create, update, remove a single user and view all users from the database. 

# Application `user`

`user` is an application with a model called `User`, consisting of three fields: `usename`, `password` and `email`. Each of fields is defined with following properties. Each characteristic for every field is validated.

<ul>
    <li> username: consists of a string with the length between 2 and 32 <li> password: consists of a string with the length between 8 and 32 and contains at least one uppercase, one lowercase and one number
    <li> email: contains <b>@</b> and <b>extension</b> and is supposed to be unique in the database.
</ul>

# How to run project
prerequisite: `docker-compose` 

run `docker-compose up`
# Local Version vs Beta Version

The difference between local and beta version is database. SQLite is used as database to run local version. This version is used to develop and extend the features of the project for the developers. It is also good to know that it is necessary to configure `SECRET_KEY` and make migrations in your local environment before running the project.

For the Beta Version, I used posgreSQL served as database. Data migration and tests are automatically proccessed before lauching the web server. 


# Testing Section

Testing is seen an important part in this project. In order to cover and detect what are necessary to be tested, I employed [`coverage`](https://coverage.readthedocs.io/en/6.3.2/) to evaluate my test sets.

<img src="./coverage-report.png" alt="Coverage report" style="height: 700px; width:800px;"/>

Since Django has built-in module based on `unittest` for testing, I did not choose third-party library to build the test cases. To detect and run test cases in the project, run

```python manage.py test -v 2```

where `-v 2` is an optional tag to verbose each test case with name, testing result, and other info, for instance, print statements. 


