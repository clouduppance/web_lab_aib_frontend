from datetime import datetime, timedelta
from base import BaseXlsBlock
import xlsxwriter


class ClientBlock:
    def __init__(self, id, fio, phone, city, email):
        self.id = id
        self.fio = fio
        self.phone = phone
        self.city = city
        self.email = email
        self.payment_count = 0
        self.account = 0

    def increment_payment_count(self):
        self.payment_count += 1

    def transaction_account_count(self, payment):
        self.account += payment.amount


class PaymentBlock:
    def __init__(self, id, client_id, amount, created_at):
        self.id = id
        self.client_id = client_id
        self.amount = amount
        self.created_at = created_at


class RequestParametersBlock(BaseXlsBlock):
    TITLE = "Параметры запроса"
    SUBTITLE = "Дата выгрузки"
    PERIOD = "Период, за который сделана выгрузка"

    def write_title(self):
        return True

    def write_data(self):
        date_of_extraction = datetime.today().strftime("%Y-%m-%d")
        period_start = datetime.strptime(self.payments[0].created_at, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
        period_end = datetime.strptime(self.payments[-1].created_at, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")

        request_parameters_data = [
            [self.TITLE],
            [self.SUBTITLE, date_of_extraction],
            [self.PERIOD, f"{period_start} - {period_end}"]
        ]

        for row_data in request_parameters_data:
            for col_num, col_value in enumerate(row_data):
                self.worksheet.write(self.current_row, col_num, col_value)
            self.current_row += 1

        return self.current_row + 1


class ActiveClientsReport(BaseXlsBlock):
    TITLE = "Отчёт по активным клиентам"
    HEADER = "Топ клиентов по количеству платежей"

    def calculate_quarter(self, year, quarter):
        if not isinstance(year, int) or not isinstance(quarter, int):
            raise ValueError("Квартал и год и год должны быть числами")

        if quarter < 1 or quarter > 4:
            raise ValueError("Ошибка, квартал введен не верно")

        if year < 1:
            raise ValueError("Ошибка, год < 1")

        quarter_starts = [1, 4, 7, 10]

        if 1 <= quarter <= 4:
            start_month = quarter_starts[quarter - 1]
            start_date = datetime(year, start_month, 1)

            if quarter == 4:
                end_date = datetime(year + 1, 1, 1) - timedelta(days=1)
            else:
                end_date = datetime(year, start_month + 2, 1) - timedelta(days=1)

            return start_date, end_date

    def payment_date_check(self, payment, start_date, end_date):
        payment_date = datetime.strptime(payment.created_at, "%Y-%m-%dT%H:%M:%S.%fZ")

        if start_date <= payment_date <= end_date:
            return True
        else:
            return False

    def generate_top_clients_report(self, year=None, quarter=None):
        if year is None or quarter is None:
            current_date = datetime.now()
            year = current_date.year
            quarter = (current_date.month - 1) // 3 + 1

        start_date, end_date = self.calculate_quarter(year, quarter)

        for client in self.clients:
            client.payment_count = 0

        for payment in self.payments:
            for client in self.clients:
                if payment.client_id == client.id and self.payment_date_check(payment, start_date, end_date):
                    client.increment_payment_count()

        sorted_clients = sorted(self.clients, key=lambda x: x.payment_count, reverse=True)

        return sorted_clients[:10]

    def write_data(self):
        self.worksheet.write(self.current_row, 0, self.HEADER)

        quarters = [(3, 2023), (3, 2023), (2, 2023), (1, 2023), (4, 2022)]

        for column, (quarter, year) in enumerate(quarters, start=1):
            self.worksheet.write(self.current_row, column, f"Q{quarter} {year} год")
            top_clients = self.generate_top_clients_report(year, quarter)
            for iter, client in enumerate(top_clients, start=self.current_row + 1):
                self.worksheet.write(iter, column, f"{iter - self.current_row}. {client.fio}")

        return len(top_clients) + self.current_row

    def write_title(self):
        self.current_row += 1
        self.worksheet.write(self.current_row, 0, self.TITLE)
        self.current_row += 1


class GeographyClientsReport(BaseXlsBlock):
    TITLE = "География клиентов"
    SUBTITLE = "Статистика распределения клиентов"
    COUNTRY = "Russia"
    CITY = "Города"
    QUANTITY = "Количетсво клиентов"

    def generate_top_clients_geography(self):
        city_counts = {}
        for client in self.clients:
            city_counts[client.city] = city_counts.get(client.city, 0) + 1

        top_cities = sorted(city_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        return top_cities

    def write_title(self):
        self.worksheet.write(self.current_row, 0, self.TITLE)
        self.current_row += 1

        cell_range = xlsxwriter.utility.xl_range(self.current_row, 0, self.current_row + 1, 0)
        self.worksheet.merge_range(cell_range, self.SUBTITLE)

        cell_range = xlsxwriter.utility.xl_range(self.current_row, 1, self.current_row, 2)
        self.worksheet.merge_range(cell_range, self.COUNTRY)
        self.current_row += 1
        self.worksheet.write(self.current_row, 1, self.CITY)
        self.worksheet.write(self.current_row, 2, self.QUANTITY)

    def write_data(self):
        top_cities = self.generate_top_clients_geography()

        for iter, (city, count) in enumerate(top_cities, start=self.current_row + 1):
            self.worksheet.write(iter, 1, f"{iter - self.current_row}. {city}")
            self.worksheet.write(iter, 2, count)

        return len(top_cities) + 4


class AccountClientsReport(BaseXlsBlock):
    TITLE = "Анализ состояния счета"
    SUBTITLE = "Статистика состояния счёта клиента"
    SUBTITLE_ACCOUNT = "Прибыльность"
    SUBTITLE_DEBT = "Задолженность"
    CLIENT = "Клиент"
    ACCOUNT = "Состояние счета"

    def generate_top_clients_account(self):

        for client in self.clients:
            client.account = 0

        for payment in self.payments:
            for client in self.clients:
                if payment.client_id == client.id:
                    client.transaction_account_count(payment)

        top_clients_account = sorted(self.clients, key=lambda x: x.account, reverse=True)[:10]
        top_clients_debt = sorted(self.clients, key=lambda x: x.account, reverse=False)[:10]

        return top_clients_account, top_clients_debt

    def write_title(self):
        self.worksheet.write(self.current_row, 0, self.TITLE)
        self.current_row += 1

        cell_range = xlsxwriter.utility.xl_range(self.current_row, 0, self.current_row + 1, 0)
        self.worksheet.merge_range(cell_range, self.SUBTITLE)

        cell_range = xlsxwriter.utility.xl_range(self.current_row, 1, self.current_row, 2)
        self.worksheet.merge_range(cell_range, self.SUBTITLE_DEBT)

        cell_range = xlsxwriter.utility.xl_range(self.current_row, 3, self.current_row, 4)
        self.worksheet.merge_range(cell_range, self.SUBTITLE_ACCOUNT)
        self.current_row += 1

        self.worksheet.write(self.current_row, 1, self.CLIENT)
        self.worksheet.write(self.current_row, 2, self.ACCOUNT)
        self.worksheet.write(self.current_row, 3, self.CLIENT)
        self.worksheet.write(self.current_row, 4, self.ACCOUNT)

    def write_data(self):
        top_clients_account, top_clients_debt = self.generate_top_clients_account()

        for iter, client in enumerate(top_clients_account, start=self.current_row + 1):
            self.worksheet.write(iter, 1, f"{iter - self.current_row}. {client.fio}")
            self.worksheet.write(iter, 2, client.account)

        for iter, client in enumerate(top_clients_debt, start=self.current_row + 1):
            self.worksheet.write(iter, 3, f"{iter - self.current_row}. {client.fio}")
            self.worksheet.write(iter, 4, client.account)

        return len(top_clients_account) + 4
