import xlsxwriter
from base import BaseXlsBlock
from blocks import ActiveClientsReport, GeographyClientsReport, Status

class ExcelWriter:
    ANALYTICS_BLOCKS_CLASSES = [
        ActiveClientsReport,
        GeographyClientsReport,
        Status
    ]
    def __init__(self, request_parameters):
        self.request_parameters = request_parameters
        self.filename = f"my_payments_analytics_{self.request_parameters.date_of_extraction}.xlsx"
        self.workbook = xlsxwriter.Workbook(self.filename)
        self.worksheet = self.workbook.add_worksheet()
        self.current_row = 0

    def writer(self):
        self.write_request_parameters()
        for items in self.ANALYTICS_BLOCKS_CLASSES:
            item_init = items(self.data, self.current_row, self.worksheet)
            item_init.writer_title()
            item_init.writer_data()

    def write_request_parameters(self):
        request_parameters_data = [
            ["Параметры запроса"],
            ["Дата выгрузки", self.request_parameters.date_of_extraction],
            ["Период, за который сделана выгрузка", f"{self.request_parameters.period_start} - {self.request_parameters.period_end}"]
        ]

        for row_data in request_parameters_data:
            for col_num, col_value in enumerate(row_data):
                self.worksheet.write(self.current_row, col_num, col_value)
            self.current_row += 1

    def write_active_clients_report(self, active_clients_report):
        self.current_row += 1
        self.worksheet.write(self.current_row, 0, "Отчёт по активным клиентам")
        self.current_row += 1

        self.worksheet.write(self.current_row, 0, "Топ клиентов по количеству платежей")

        quarters = [(3, 2023), (3, 2023), (2, 2023), (1, 2023), (4, 2022)]

        for column, (quarter, year) in enumerate(quarters, start=1):
            self.worksheet.write(self.current_row, column, f"Q{quarter} {year} год")
            top_clients = active_clients_report.generate_top_clients_report(year, quarter)
            for i, client in enumerate(top_clients, start=self.current_row + 1):
                self.worksheet.write(i, column, f"{i - self.current_row}. {client.fio}")

        self.current_row += 12
        #
        self.worksheet.write(self.current_row, 0, "География клиентов")
        self.current_row += 1

        cell_range = xlsxwriter.utility.xl_range(self.current_row, 0, self.current_row + 1, 0)
        self.worksheet.merge_range(cell_range, "Статистика распределения клиентов")

        cell_range = xlsxwriter.utility.xl_range(self.current_row, 1, self.current_row, 2)
        self.worksheet.merge_range(cell_range, "Russia")
        self.current_row += 1
        self.worksheet.write(self.current_row, 1, "Города")
        self.worksheet.write(self.current_row, 2, "Количество клиентов")

        top_cities = active_clients_report.generate_top_clients_geography()

        for i, (city, count) in enumerate(top_cities, start=self.current_row + 1):
            self.worksheet.write(i, 1, f"{i - self.current_row}. {city}")
            self.worksheet.write(i, 2, count)

        self.current_row += 13
        #

        self.worksheet.write(self.current_row, 0, "Анализ состояния счета")

        cell_range = xlsxwriter.utility.xl_range(self.current_row, 0, self.current_row + 1, 0)
        self.worksheet.merge_range(cell_range, "Статистика состояния счёта клиента")

        cell_range = xlsxwriter.utility.xl_range(self.current_row, 1, self.current_row, 2)
        self.worksheet.merge_range(cell_range, "Задолженность")

        cell_range = xlsxwriter.utility.xl_range(self.current_row, 3, self.current_row, 4)
        self.worksheet.merge_range(cell_range, "Прибыльность")
        self.current_row += 1

        self.worksheet.write(self.current_row, 1, "Клиент")
        self.worksheet.write(self.current_row, 2, "Состояние счета")
        self.worksheet.write(self.current_row, 3, "Клиент")
        self.worksheet.write(self.current_row, 4, "Состояние счета")

        top_clients_account, top_clients_debt = active_clients_report.generate_top_clients_account()

        for i, client in enumerate(top_clients_account, start=self.current_row + 1):
            self.worksheet.write(i, 1, f"{i - self.current_row}. {client.fio}")
            self.worksheet.write(i, 2, client.account)

        for i, client in enumerate(top_clients_debt, start=self.current_row + 1):
            self.worksheet.write(i, 3, f"{i - self.current_row}. {client.fio}")
            self.worksheet.write(i, 4, client.account)

    def close_workbook(self):
        self.workbook.close()
