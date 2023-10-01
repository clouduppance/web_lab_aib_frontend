# HTTP HTTPS и их параметры 
___________________________________________________
## Отчет к лабораторной работе №1

### Цель работы
Познакомиться с протоколом HTTP и протоколом HTTPS, а так же особенностями установления соединения между источником и получателем.
___________________________________________________
### Описание 
Был создан скрипт script.sh:
```shell
curl -Iv www.rzd.ru
```
Параметры утилиты curl:
+ I - позволяет получить только заголовки ответа.
+ v - выводит подробную информацию о запросе и ответе.

По итогу выоплнения скрипта выводится:
```shell
$ ./script.sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 212.164.138.126:80...
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0* Connected to www.rzd.ru (212.164.138.126) port 80 (#0)
> HEAD / HTTP/1.1
> Host: www.rzd.ru
> User-Agent: curl/7.88.1
> Accept: */*
>
< HTTP/1.1 301 Moved Permanently
< Date: Tue, 05 Sep 2023 16:40:33 GMT
< Content-Type: text/html
< Content-Length: 150
< Connection: keep-alive
< Location: https://www.rzd.ru:443/
<
  0   150    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 301 Moved Permanently
Date: Tue, 05 Sep 2023 16:40:33 GMT
Content-Type: text/html
Content-Length: 150
Connection: keep-alive
Location: https://www.rzd.ru:443/


* Connection #0 to host www.rzd.ru left intact

```

Расшифровка данных в заголовке ответа:
```shell
  0   150    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 301 Moved Permanently #Код ответа http. 301 - Перемещён на постоянной основе.
Date: Tue, 05 Sep 2023 16:40:33 GMT #Дата ответа сервера, считается по UTC
Content-Type: text/html #То, чем ответил на http запрос. В этом случае Html.
Content-Length: 150 #Размер html (в байтах)
Connection: keep-alive #Параметр, который показывает, что подключение к серверу должно быть постоянно
Location: https://www.rzd.ru:443/ #Туда, куда перемещен запрос (код 301)

```
-----------------------------
### Вывод
В ходе данной лаборатной работы мы изучили светлую строну и утилиту curl, сделали GET запрос и обработали полученные данные.