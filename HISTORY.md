# Eriksson-interview

* Initialize repository in Github
* Initialize django project
* Break down the assignment into smaller parts
    * Database
        1. use SQLite as the database to start with
        2. replace PostgreSQL with SQLite as database to store the data
        3. test PostgreSQL in the production mode
    * User Model
        1. username
            * The maximal length is set to 128
        2. password
            * password validator
                * longer than 8 characters
                * a combination of number, capital and small letters
        3. email
            * should be unique in the database
    * API
        1. Create new user
        2. Edit the existing user
        3. Delete the existing user
        4. Views all users
    
    * Test
        1. Test on User models
        2. Test on Validators
        3. Test on API

    

