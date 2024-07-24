import json
from django.http import JsonResponse
from Factory.read_file_factory import ReadFileFactory, ReadFile, ReadFileWechat, ReadFileWechatFactory, ReadFileAliPayFactory, ReadFileAliPay
from Utils.judge_excel_type import judge_excel_type


def read_csv_file(request):
    response_message_dic = {
        "code": '200',
        "info": {},
        "message": '成功解析文件！'
    }
    try:
        # 获取文件路径
        request_body = json.loads(request.body)
        file_path_list = request_body['file_path_list']

        read_file_wechat_factory = ReadFileWechatFactory()
        read_file_wechat = read_file_wechat_factory.create_read_file_factory(ReadFileWechat)
        read_file_alipay_factory = ReadFileAliPayFactory()
        read_file_alipay = read_file_alipay_factory.create_read_file_factory(ReadFileAliPay)

        for file_path in file_path_list:
            excel_file_type = judge_excel_type(file_path)
            if excel_file_type == 'wechat':
                read_file_wechat.parse_wechat_file(file_path)
                response_message_dic['info'][file_path] = read_file_wechat.get_file_data()
            elif excel_file_type == 'alipay':
                read_file_alipay.parse_alipay_file(file_path)
                response_message_dic['info'][file_path] = read_file_alipay.get_file_data()
            elif excel_file_type == '':
                response_message_dic['info'][file_path] = {}

        return JsonResponse(response_message_dic)
    except Exception as e:
        response_message_dic['code'] = '400'
        response_message_dic['message'] = f'解析文件失败，发生错误{e}'
