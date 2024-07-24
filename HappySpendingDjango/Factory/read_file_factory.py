import copy
import datetime
import os
from Utils.convert_bytes import convert_bytes
import itertools
import pandas as pd

from Struct import dictionary_struct


# 文件读取-抽象产品类
class ReadFile:
    file_info_list = []
    file_data_info = copy.deepcopy(dictionary_struct.file_data_info)
    file_info = copy.deepcopy(dictionary_struct.file_info)

    def parse_file(self, file_path):
        # 初始化文件信息
        file_size = convert_bytes(os.path.getsize(file_path))
        base_name = os.path.basename(file_path)
        file_type = base_name.split('.')[-1]
        now_date = datetime.datetime.now().strftime('%Y/%m/%d')
        self.file_info['file_size'] = file_size
        self.file_info['file_type'] = file_type
        self.file_info['file_source_path'] = file_path
        self.file_info['file_source_name'] = base_name
        self.file_info['file_now_name'] = base_name
        self.file_info['file_source_date'] = now_date
        self.file_info['file_modify_date'] = now_date
        self.file_info['file_start_index'] = len(self.file_data_info['trade_time'])

    def get_file_info(self):
        return self.file_info

    def get_file_data(self):
        return self.file_data_info


# 文件读取-具体产品类
class ReadFileWechat(ReadFile):

    def parse_wechat_file(self, file_path):
        # 初始化文件信息
        self.parse_file(file_path)
        # 根据文件的类型调用不同的函数进行解析
        if self.file_info['file_type'] == 'csv':
            self.parse_wechat_file_csv(file_path)

    def parse_wechat_file_csv(self, file_path):
        wechat_csv = pd.read_csv(file_path, skiprows=16)
        wechat_csv_values = wechat_csv.values
        for item in itertools.islice(wechat_csv_values, 0, None):
            self.file_data_info['trade_time'].append(item[0])
            self.file_data_info['trade_type'].append(item[1])
            self.file_data_info['trade_target'].append(item[2])
            self.file_data_info['trade_goods'].append(item[3])
            self.file_data_info['trade_target_account'].append('')
            self.file_data_info['trade_source'].append('微信')
            self.file_data_info['budget'].append(item[4])
            self.file_data_info['trade_amount'].append(item[5])
            self.file_data_info['trade_method'].append(item[6])
            self.file_data_info['trade_status'].append(item[7])
            self.file_data_info['trade_number'].append(item[8])
            self.file_data_info['businesses_number'].append(item[9])
            self.file_data_info['remark'].append(item[10])
        self.file_info['file_end_index'] = len(self.file_data_info['trade_time'])
        self.file_info_list.append(copy.deepcopy(self.file_info))


class ReadFileAliPay(ReadFile):

    def parse_alipay_file(self, file_path):
        # 初始化文件信息
        self.parse_file(file_path)
        # 根据文件的类型调用不同的函数进行解析
        if self.file_info['file_type'] == 'csv':
            self.parse_alipay_file_csv(file_path)

    def parse_alipay_file_csv(self, file_path):
        alipay_csv = pd.read_csv(file_path, skiprows=24)
        alipay_csv_values = alipay_csv.values
        for item in itertools.islice(alipay_csv_values, 0, None):
            self.file_data_info['trade_time'].append(item[0])
            self.file_data_info['trade_type'].append(item[1])
            self.file_data_info['trade_target'].append(item[2])
            self.file_data_info['trade_target_account'].append(item[3])
            self.file_data_info['trade_goods'].append(item[4])
            self.file_data_info['trade_source'].append('支付宝')
            self.file_data_info['budget'].append(item[5])
            self.file_data_info['trade_amount'].append(item[6])
            self.file_data_info['trade_method'].append(item[7])
            self.file_data_info['trade_status'].append(item[8])
            self.file_data_info['trade_number'].append(item[9])
            self.file_data_info['businesses_number'].append(item[10])
            self.file_data_info['remark'].append(item[11])
        self.file_info['file_end_index'] = len(self.file_data_info['trade_time'])
        self.file_info_list.append(copy.deepcopy(self.file_info))


# 文件读取-抽象工厂类
class ReadFileFactory:
    type = ''

    @staticmethod
    def create_read_file_factory(read_file_class):
        read_file_factory = read_file_class()
        return read_file_factory


# 文件读取-具体工厂类
class ReadFileWechatFactory(ReadFileFactory):
    def __init__(self):
        self.type = 'wechat'


class ReadFileAliPayFactory(ReadFileFactory):
    def __init__(self):
        self.type = 'alipay'
