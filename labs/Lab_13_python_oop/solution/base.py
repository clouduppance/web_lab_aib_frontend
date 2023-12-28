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
        self.main_subtitle_col_style = self.workbook.add_format({
        'bg_color': '#C6E2FF',
        'border': 4,
        'bold': 1,
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
        'font_color': '#002060',
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

    def write_and_style(self, text, style, cell_range = None, row = None, col = None):
        ratio_width = (style.font_size / 20) + 1
        width = int(len(text)) * ratio_width

        if cell_range:
            self.worksheet.merge_range(cell_range, text, style)
        else:
            self.worksheet.write(row, col, text, style)
            self.worksheet.set_column(row, col, width)

        

    @abstractmethod
    def write_data(self):
        pass

    @abstractmethod
    def write_title(self):
        pass
