#这里读取一个不存在的文件，查看Python异常机制会抛出哪些异常信息
# try:
#     info_data = open ('missing.txt')
#     print(info_data.readline(),end='')
# except IOError as err:
#     print('File error' + str(err))
# finally:
#     if 'info_data' in locals():
#         info_data.close()

#使用with简化写法：
try:
    with open ('missing.txt',) as  info_data :
        print("It's...",file=info_data)
except IOError as err:
    print('File error' + str(err))