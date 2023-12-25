from abc import ABCMeta, abstractmethod


class BaseXlsBlock(metaclass=ABCMeta):
    TITLE = str("TITLE")
    def __init__(self, clients, payments, current_row, worksheet):
        self.clients = clients
        self.payments = payments
        self.current_row = current_row
        self.worksheet = worksheet

    @abstractmethod
    def write_data(self):
        pass

    @abstractmethod
    def write_title(self):
        pass
    