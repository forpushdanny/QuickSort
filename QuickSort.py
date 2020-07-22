MyDebug = False
'''
    請將要排序的資料存在test1.txt
    資料之間以空格隔開
    例如： 3.23 5.34 3.45 1.1 5.2 9.0 -23 5.8
'''
def partition(mydata, pivot_index, lower_index, higher_index):
    #取基準值
    pivot= mydata[pivot_index]
    #移到最後面
    temp_value=mydata[pivot_index]
    mydata[pivot_index] = mydata[higher_index]
    mydata[higher_index] = temp_value
    #從左邊開始
    pivot_new_index = lower_index
    
    for i in range(lower_index, higher_index, 1):
        #比基準值小，交換資料
        
        if (mydata[i] <= pivot):
            temp_value = mydata[pivot_new_index]
            mydata[pivot_new_index] = mydata[i]
            mydata[i] = temp_value
            pivot_new_index +=1
    #將基準值移回中間值的位置
    temp_value = mydata[pivot_new_index]
    mydata[pivot_new_index] = mydata[higher_index]
    mydata[higher_index] = temp_value
    if MyDebug:
        print()
        for rd in mydata:
            print(rd,end=' ')
    return pivot_new_index


def quicksort(mydata, pivot_index, lower_index, higher_index):
    if higher_index > lower_index:
        pivot_new_index = partition(mydata, pivot_index, lower_index, higher_index)
        quicksort(mydata, lower_index, lower_index, pivot_new_index-1)
        quicksort(mydata, pivot_new_index+1, pivot_new_index+1, higher_index)

def quicksort_test():
    try:
        read_file = open('test1.txt', 'r')
    except:
        print("讀取 test1.txt 錯誤")
    #讀取資料，當以空格為分隔符號split不加入參數
    read_data = read_file.read().split()
    #轉成浮點數
    mydata= [float(rd) for rd in read_data]
    #確認資料讀取無誤
    if MyDebug:
        for rd in mydata:
            print(rd,end=' ')

    # 取第一個數當基準
    pivot_index=0
    quicksort(mydata, pivot_index, pivot_index, len(mydata)-1)
    try:
        save_file = open("test1_sort.txt",'w')
        
        print("所有數的個數：", len(mydata))
        save_file.write("所有數的個數：")
        save_file.write(str(len(mydata)))
        save_file.write('\n')
        
        print("最大的數：",  mydata[len(mydata)-1])
        save_file.write("最大的數：")
        save_file.write(str(mydata[len(mydata)-1]))
        save_file.write('\n')

        print("最小的數：", mydata[0])
        save_file.write("最小的數：")
        save_file.write(str(mydata[0]))
        save_file.write('\n')

        print("QuickSort排序後的結果:")
        save_file.write("QuickSort排序後的結果:")
        save_file.write('\n')

        for sd in mydata:
            print(sd, end = " ")
            save_file.write(str(sd))
            save_file.write(" ")
        
        #關閉檔案
        save_file.close()
    except:
        print("存檔失敗")
    print()

if __name__ == "__main__":
    quicksort_test()



