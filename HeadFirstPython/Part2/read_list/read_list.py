def read_list(clist):
    for each_item in clist :
        if isinstance(each_item,list):
            read_list(each_item)
        else:
            print(each_item)
