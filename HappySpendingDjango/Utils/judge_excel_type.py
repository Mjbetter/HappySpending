import csv
import os


# 判断csv账单文件属于支付宝还是微信
def judge_excel_type(file_path):
    if not os.path.isfile(file_path) or not file_path.endswith('.csv'):
        return ''
    try:
        with open(file_path, 'r', encoding='utf-8') as file_content:
            csv_reader = csv.reader(file_content)
            need_row_one = []
            need_row_two = []
            for index, rows in enumerate(csv_reader):
                if index == 0:
                    need_row_one = rows
                if index == 3:
                    need_row_two = rows
                    break
            if need_row_one[0] == '微信支付账单明细':
                return 'wechat'
            elif '支付宝账户' in need_row_two[0]:
                return 'alipay'
            else:
                return ''
    except Exception as e:
        return ''
