import struct
'''
封包（打包）
'''
data = b"hello python"
b_date = struct.pack('H',len(data))+data
print(b_date)

'''
解包
'''
a_date = b'\x0c\x00hello python'
body_size = struct.unpack('H',a_date[:2])
print(body_size)
a_date = a_date[2:]
body = b_date[:body_size]
print(body)