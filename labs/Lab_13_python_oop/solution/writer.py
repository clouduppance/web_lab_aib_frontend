import xlsxwriter
from datetime import datetime
from blocks import ActiveClientsReport, GeographyClientsReport, AccountClientsReport, RequestParametersBlock


class ExcelWriter:
    ANALYTICS_BLOCKS_CLASSES = [
        RequestParametersBlock,
        ActiveClientsReport,
        GeographyClientsReport,
        AccountClientsReport
    ]

    def __init__(self, clients, payments):
        self.payments = payments
        self.clients = clients
        self.filename = f"my_payments_analytics_{datetime.today().strftime('%Y_%m_%d')}.xlsx"
        self.workbook = xlsxwriter.Workbook(self.filename)
        self.worksheet = self.workbook.add_worksheet()
        self.current_row = 0

    def write(self):
        for item in self.ANALYTICS_BLOCKS_CLASSES:
            item_init = item(self.clients, self.payments, self.current_row, self.worksheet, self.workbook)
            item_init.write_title()
            self.current_row += item_init.write_data()

    def close_workbook(self):
        self.workbook.close()
