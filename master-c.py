# _*_ coding: utf-8 _*_
import socket
import struct
import json
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('kv260.xmutil.ninox',31222)) #连接服务器
while True:
    # 发收消息
    cmd = input('请你输入命令>>：').strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8')) #发送
    #先收报头的长度
    header_len = struct.unpack('i',phone.recv(4))[0]  #吧bytes类型的反解
    #在收报头
    header_bytes = phone.recv(header_len) #收过来的也是bytes类型
    header_json = header_bytes.decode('utf-8')   #拿到json格式的字典
    header_dic = json.loads(header_json)  #反序列化拿到字典了
    total_size = header_dic['total_size']  #就拿到数据的总长度了
    #最后收数据
    recv_size = 0
    total_data=b''
    while recv_size<total_size: #循环的收
        recv_data = phone.recv(1024) #1024只是一个最大的限制
        recv_size+=len(recv_data) #有可能接收的不是1024个字节，或许比1024多呢，
        # 那么接收的时候就接收不全，所以还要加上接收的那个长度
        total_data+=recv_data #最终的结果
    print('返回的消息：%s'%total_data.decode('gbk'))
    if cmd == 'quit':
        break
phone.close()
