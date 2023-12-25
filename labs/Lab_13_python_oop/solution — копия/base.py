from abc import ABCMeta, abstractmethod


class BaseXlsBlock(metaclass=ABCMeta):
    TITLE = "TITLE"
    def __init__(self, some_data):
        self.some_data = some_data

    @abstractmethod
    def writer_data(self):
        pass

    @abstractmethod
    def writer_header(self):
        pass

    @abstractmethod
    def writer_title(self):
        pass
    