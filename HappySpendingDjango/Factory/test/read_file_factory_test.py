from Factory.read_file_factory import ReadFileFactory, ReadFile, ReadFileWechat, ReadFileWechatFactory, ReadFileAliPayFactory, ReadFileAliPay

if __name__ == '__main__':
    # 创建文件读写工厂
    read_file_wechat_factory = ReadFileWechatFactory()
    read_file_wechat = read_file_wechat_factory.create_read_file_factory(ReadFileWechat)
    # 微信账单读取
    file_path_wechat = r"D:\Project\HappySpending\test_file\微信支付账单(20240621-20240721)\微信支付账单(20240621-20240721).csv"  # 微信账单
    read_file_wechat.parse_wechat_file(file_path_wechat)
    # 支付宝账单读取
    read_file_alipay_factory = ReadFileAliPayFactory()
    read_file_alipay = read_file_alipay_factory.create_read_file_factory(ReadFileAliPay)
    file_path_alipay = r"D:\Project\HappySpending\test_file\支付宝账单\alipay_record_20240721_215037.csv"  # 支付宝账单
    read_file_alipay.parse_alipay_file(file_path_alipay)

