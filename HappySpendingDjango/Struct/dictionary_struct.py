# 文件信息结构
file_info = {
    "file_now_name": "",         # 当前文件名称
    "file_source_name": "",      # 导入时的原始文件名
    "file_now_path": "",         # 当前文件路径
    "file_source_path": "",      # 导入时的原始文件路径
    "file_type": "",             # 文件类型
    "file_size": "",             # 文件大小（以字节为单位）
    "file_source_date": "",      # 文件导入日期
    "file_modify_date": "",       # 文件最近修改日期
    "file_start_index": 0,       # 文件数据在file_data_info中的起始位置
    "file_end_index": 0,       # 文件数据在file_data_info中的结束位置
}


# 文件存储数据结构
file_data_info = {
    "trade_time": [],               # 交易时间
    "trade_type": [],               # 交易类型
    "trade_target": [],             # 交易对象
    "trade_goods": [],              # 交易商品
    "trade_target_account": [],     # 交易对象账号
    "trade_source": [],             # 交易来源(支付宝或微信)
    "budget": [],                   # 收支
    "trade_amount": [],             # 交易金额
    "trade_method": [],             # 交易方式
    "trade_status": [],             # 交易状态
    "trade_number": [],             # 交易单号
    "businesses_number": [],        # 商户单号
    "remark": []                    # 备注
}

