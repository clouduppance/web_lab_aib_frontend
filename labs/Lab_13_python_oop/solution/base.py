from abc import ABCMeta, abstractmethod


class BaseXlsBlock(metaclass=ABCMeta):
    TITLE = "TITLE"
    def __init__(self, some_data, current_row, worksheet):
        self.some_data = some_data
        self.current_row = current_row
        self.worksheet = worksheet

    @abstractmethod
    def write_data(self):
        pass

    @abstractmethod
    def write_title(self):
        pass
    