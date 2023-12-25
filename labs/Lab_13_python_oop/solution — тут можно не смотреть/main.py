import json
from blocks import ClientBlock, PaymentBlock, RequestParametersBlock, ActiveClientsReport
from datetime import datetime
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

    active_clients_report = ActiveClientsReport(clients, payments)
        
    request_parameters = RequestParametersBlock(
        date_of_extraction=datetime.today().strftime("%Y-%m-%d"),
        period_start=datetime.strptime(payments[0].created_at, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d"),
        period_end=datetime.strptime(payments[-1].created_at, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
    )

    excel_writer = ExcelWriter(request_parameters)
    
    excel_writer.write_request_parameters()
    excel_writer.write_active_clients_report(active_clients_report)

    excel_writer.close_workbook()

if __name__ == "__main__":
    main()
