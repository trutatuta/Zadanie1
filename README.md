# Realizacja zadania nr1 w ramach laboratorium PFSwCO
Hrybinchyk Bohdan

Architektura serwisu:

![architecture](https://user-images.githubusercontent.com/61692272/150696482-fc83701b-44a4-4514-8e05-77ad525a71fa.png)

Aplikacja stworzona za pomocą języka programowania Python oraz framework do tworzenia stron internetowych Flask.
Do przechowywania historii obliczeń wykorzystywany jest Redis.

Aplikacja jest oparta o Nginx i uWSGI.
NGINX to serwer WWW i reverse proxy który przekazuje żądania do uWSGI.
uWSGI to serwer aplikacji, który może komunikować się z serwerem WWW w celu odbierania żądań i przesyłania ich do Flask za pośrednictwem protokołu WSGI.

Plik "app.ini" w folderze "flask" to plik konfiguracyjny uwsgi. Plik "app.py" - kod programu. Plik "default.conf" w folderze "nginx" to plik konfiguracyjny nginx.

Do zbudowania wykorzystujemy polecenie:
```
docker compose build
```

Do uruchomienia wykorzystywane jest polecenie
```
docker compose up
```
