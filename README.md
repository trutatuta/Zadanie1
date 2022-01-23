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

Działające kontenery:

![Screenshot_49](https://user-images.githubusercontent.com/61692272/150697077-4b129144-9ff2-4c23-9ff3-5c11198c4b97.png)

Działająca usługa:

Strona domowa:

![Screenshot_50](https://user-images.githubusercontent.com/61692272/150697091-7a4de50b-e568-40b4-bd22-2551f61fe2e1.png)

Strona kalkulatora:

![Screenshot_51](https://user-images.githubusercontent.com/61692272/150697098-22a49812-2a58-478a-b159-28b09e9b01b8.png)

Strona dokumentacji:

![Screenshot_52](https://user-images.githubusercontent.com/61692272/150697104-3087c79e-9b84-4ea4-8d3f-c202746a80c8.png)


