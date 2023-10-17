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
Проверка скрипта через протокол https:
```shell
curl -Iv https://www.rzd.ru

```
Ответ:
```shell
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 212.164.138.123:443...
* Connected to www.rzd.ru (212.164.138.123) port 443 (#0)
* ALPN: offers h2,http/1.1
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
*  CAfile: D:/Git/mingw64/etc/ssl/certs/ca-bundle.crt
*  CApath: none
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [112 bytes data]
* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [3945 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [589 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384
* ALPN: server accepted http/1.1
* Server certificate:
*  subject: CN=*.rzd.ru
*  start date: May 24 07:13:14 2023 GMT
*  expire date: Jun 24 07:13:13 2024 GMT
*  subjectAltName: host "www.rzd.ru" matched cert's "*.rzd.ru"
*  issuer: C=BE; O=GlobalSign nv-sa; CN=GlobalSign GCC R3 DV TLS CA 2020
*  SSL certificate verify ok.
* using HTTP/1.1
} [5 bytes data]
> HEAD / HTTP/1.1
> Host: www.rzd.ru
> User-Agent: curl/7.88.1
> Accept: */*
>
{ [5 bytes data]
< HTTP/1.1 403 Forbidden
< Connection: close
< Content-Length: 109
< Content-Type: text/html
<
* Excess found: excess = 109 url = / (zero-length body)
  0   109    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 403 Forbidden
Connection: close
Content-Length: 109
Content-Type: text/html


* Closing connection 0
{ [5 bytes data]
* TLSv1.2 (IN), TLS alert, close notify (256):
{ [2 bytes data]
* TLSv1.2 (OUT), TLS alert, close notify (256):
} [2 bytes data]

```

В данном примере происходит попытка подключения к сайту www.rzd.ru на тупор 443 (стандартный порт для HTTPS-соединений). Первая строка вывода сообщает о том, что происходит попытка подключения к указанному IP-адресу и порту. Далее идут строки, связанные с установлением безопасного соединения (TLS handshake) между клиентом (curl) и сервером (www.rzd.ru). В конце выводится ответ сервера в виде HTTP-статуса 403 Forbidden, который означает, что клиент не имеет доступа к запрашиваемому ресурсу. Затем соединение закрывается.

TLS handshake - это процесс установления безопасного соединения между клиентом и сервером при использовании протокола HTTPS.

Таким образом, разница между HTTP и HTTPS соединениями заключается в том, что HTTPS обеспечивает безопасность передачи данных (что видно из примера выше), а HTTP передает данные в открытом виде.

-----------------------------
### Вывод
В ходе данной лаборатной работы мы изучили светлую строну и утилиту curl, сделали GET запрос и обработали полученные данные.