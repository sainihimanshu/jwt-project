# JWT Project

*Project for ITMI 7.2 - Digital Security: Networking and Encryption*

This repo. contains a python flask implementation of jwt based authentication scheme. The app is **backend only** and can be tested using postman.

More about jwt at [http://jwt.io](http://jwt.io)

###Setup Database
1. Create a file called `main.db` in the root directory.
2. Open a python shell and run the following commands:
```
>>> from models import *
>>> models.create_tables()
```
*If you are cloning this repo, you can skip this step as it already has a database set*

### Registration
1.  Run the flask app - `$ python app.py`
2.  Open Postman and send a `post` request to `http://localhost:5000/register` with the following params
    - `username`
    - `password`  
3. The app will create a new record in db or throw an error.

### Authenticate
1. Send a `post` request to `http://localhost:5000` with `username` and `password` (the account for which you want to login)
2. The app will   send a `token` if authentication was successful and error otherwise.

### Secure Route
Try to open `http://localhost:5000/secure` in your browser (or send a get with postman). You should get a `400 not allowed error`. This is because this route is expecting a token and is available only to authorized users.

Now send a get to `http://localhost:5000/secure?token=eeee...`, the token is the one you received in `Authenticate` step. It the token is valid, then you'll see a `You have arrived` message.

### Insecure Route
This is an open route and returns a `Welcome !` message, with our without token.

