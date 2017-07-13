import os
#新建两个空列表，分别作为对话的存储列表。
jack_list = []
rose_list = []
try:
    with open('atext.txt') as spoken_data:
        for each_line in spoken_data:
            try:
                (role,line_spoken) = each_line.split(':',1)
                line_spoken = line_spoken.strip() #去除不必要的空格
                if role == 'JACK':
                    jack_list.append(line_spoken) #将对应回话添加到jack的列表中
                elif role =='ROSE':
                    rose_list.append(line_spoken)
            except ValueError:
                pass
        spoken_data.close() #读取文件完毕，关闭该文件。
except IOError as err:
    print("The Spoken_data file is missing:" + str(err))

try:
    #使用print 写入到文件当中
    with open('file_jack.txt','w') as file_jack:
        print(jack_list, file=file_jack)
    with open('file_rose.txt','w') as file_rose:
        print(rose_list, file=file_rose)
except IOError as err:
    print('File IO error!' + str(err))#文件读取错误，给以提示。
finally:
    #写入文件之后，我们需要关闭对应的文件
    file_jack.close()
    file_rose.close()
