import os
#新建两个空列表，分别作为对话的存储列表。
jack_list = []
rose_list = []
try:
    spoken_data = open('atext.txt')
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
except IOError:
    print("The Spoken_data file is missing!")

try:
    file_jack = open('file_jack.txt','w')
    file_rose = open('file_rose.txt','w')
    #使用print 写入到文件当中
    print(jack_list,file=file_jack)
    print(rose_list,file=file_rose)

except IOError:
    print('File IO error!')#文件读取错误，给以提示。
finally:
    #写入文件之后，我们需要关闭对应的文件
    file_jack.close()
    file_rose.close()
