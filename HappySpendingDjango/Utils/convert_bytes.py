import re


def convert_bytes(bytes_num):
	"""
	将字节单位转化为最合适的单位
	:param bytes_num:文件大小(字节)
	:return: 转化后的文件大小及单位
	"""
	for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
		if bytes_num < 1024:
			return f'{bytes_num:.2f}{unit}'
		bytes_num /= 1024.0


def convert_to_bytes(size):
	"""
	将其他单位转化为字节单位
	:params size:文件大小(非字节单位，带单位(B、KB、MB、GB、TB))
	:return: 转化后的文件大小，不带单位
	"""
	unit_size = {
		'B': 1024,
		'KB': 1024 ** 2,
		'MB': 1024 ** 3,
		'GB': 1024 ** 4,
		'TB': 1024 ** 5
	}
	size_num = int(re.sub(u"([^\u0030-\u0039])", "", size))
	size_unit = re.sub(u'([^\u0041-\u007a])', '', size).upper()
	if size_unit in unit_size:
		size_num *= unit_size[size_unit]
	return size_num
