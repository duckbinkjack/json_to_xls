import json
import pprint

import xlsxwriter

class FileManagement(object):
    def __init__(self):
        self.json_file_name = 'input.json'
        self.excel_file_name = 'output.xlsx'
        self.array_user_id = []
        self.array_heart_rate = []
        self.array_resp_rate = []
        self.array_stress_lvl = []

    def read_text_file(self):
        try:
            with open(self.json_file_name) as data_file:
                data = json.load(data_file)
                #pprint.pprint(data)
                for x in data['data']:
                    user_id = x['user_id']
                    heart_rate = x['heart_rate']
                    resp_rate = x['respiratory_rate']
                    stress_lvl = x['stress_level']
                    self.array_user_id.append(user_id)
                    self.array_heart_rate.append(heart_rate)
                    self.array_resp_rate.append(resp_rate)
                    self.array_stress_lvl.append(stress_lvl)

        except IOError:
            print('unexpected error')
    def save_to_xlsx(self):
        workbk = xlsxwriter.Workbook(self.excel_file_name)
        worksheet = workbk.add_worksheet()
        for index, value in enumerate(self.array_user_id):
            worksheet.write(index, 0, self.array_user_id[index])
            worksheet.write(index, 1, self.array_heart_rate[index])
            worksheet.write(index, 2, self.array_resp_rate[index])
            worksheet.write(index, 3, self.array_stress_lvl[index])

if __name__  == '__main__':
    filemanagement = FileManagement()
    filemanagement.read_text_file()
    filemanagement.save_to_xlsx()

