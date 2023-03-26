HTTP: HyperText Transfer Protocol


Webpage on the server and the client to access that webpage


GET : CLIENT
Server response: HTTP/1.1 200 OK
        content-type: text/html

    HTTP status code:
    200: OK
    301: Moved Permanently
    403: Forbidden
    404: Not Found
    500: Internal ServerError

Django: Web Framework
    create an new app:
                    python3 manage.py startapp <app_name>
    how to run it:
                    python3 manage.py runserver

    django stores all the data in the table
                    to create it we need
                    python3 manage.py migrate
