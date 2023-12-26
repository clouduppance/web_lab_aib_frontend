from abc import ABCMeta, abstractmethod


class BaseXlsBlock(metaclass=ABCMeta):
    TITLE = "TITLE"

    def __init__(self, clients, payments, current_row, worksheet, workbook):
        self.clients = clients
        self.payments = payments
        self.current_row = current_row
        self.worksheet = worksheet
        self.workbook = workbook
        self.subtitile_col_style = self.workbook.add_format({
        'bg_color': '#C6E2FF',
        'border': 4,
        'border_color': '#000080',
        'text_wrap': 1,
        'font_color': '#000000',
        'font_size': 11,
        'align': 'center',
        'font_name': 'Arial',
        'valign': 'vcenter',
        'border_color': '#000080',
        })
        self.titile_col_style = self.workbook.add_format({
        'bg_color': '#FCD5B4',
        'border': 1,
        'text_wrap': 1,
        'bold': 1,
        'font_name': 'Arial',
        'border_color': '#000080',
        'font_color': '#000000',
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter',
        'border_color': '#000000'
        })
        self.data_col_style = self.workbook.add_format({
        'font_name': 'Arial',
        'font_color': '#000000',
        'font_size': 10,
        'valign': 'vcenter',
        'align': 'center',
        })
        self.num_col_style = self.workbook.add_format({
        'font_name': 'Arial',
        'font_color': '#000000',
        'font_size': 10,
        'valign': 'vcenter',
        'align': 'center',
        'num_format': '#',
        })

    def write_and_style(self, row, col, text, style=None, is_bold = None):
        self.worksheet.write(row, col, text, style)
        self.worksheet.set_column(row, col, int(len(text)) + int(len(text) * 0.5))
        if is_bold:
            self.worksheet.add_format(row, col, {'bold': 1})


    @abstractmethod
    def write_data(self):
        pass

    @abstractmethod
    def write_title(self):
        pass
