from Utils.judge_excel_type import judge_excel_type

if __name__ == '__main__':
    file_path_wechat = r"D:\Project\HappySpending\test_file\微信支付账单(20240621-20240721)\微信支付账单(20240621-20240721).csv"  # 微信账单
    file_path_alipay = r"D:\Project\HappySpending\test_file\支付宝账单\alipay_record_20240721_215037.csv"  # 支付宝账单
    # judge_excel_type(file_path_wechat)
    excel_type = judge_excel_type(file_path_alipay)
    a = 1