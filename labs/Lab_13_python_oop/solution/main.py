import json
from blocks import ClientBlock, PaymentBlock
from writer import ExcelWriter

def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def main():
    clients_data = read_json('clients.json')['clients']
    payments_data = read_json('payments.json')['payments']

    clients = [ClientBlock(**client) for client in clients_data]
    payments = [PaymentBlock(**payment) for payment in payments_data]

    excel_writer = ExcelWriter(clients, payments)
    
    excel_writer.write()

    excel_writer.close_workbook()

if __name__ == "__main__":
    main()
