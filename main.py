import json

#import matplotlib
from matplotlib import pyplot as plt
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

def create_list_of_data_CO2(d333_list,time_start, time_finish):
    res1_list = []
    for x in d333_list:
        if (x['time'] >= time_start and x['time'] <= time_finish):
            #print("time = ", x['time'], "  co2 = ", x['co2'], " ")
            #print(len(res1_list[0]))
            #print(res1_list[0])

            #print(type(len(res1_list[0])))
            #print(type([0][len(res1_list[0])-1]))
            if len(res1_list)==0:
                print("first cond")
                temp = []
                temp.append(x['time'])
                #res1_list[0].append(x['time'])
                #print(x['time'])
                #print(res1_list[0][0])
                #print(res1_list[0][1])
                temp.append(x['co2'])
                #res1_list[0].append(x['co2'])
                #print("xCO2 = ",x['co2'])
                res1_list.append(temp)
                #print(res1_list)
                #print(res1_list[0][0])
                #print(res1_list[0][1])
                #print( len(res1_list[0][0]) )
            elif  ( len(res1_list)!=0 ) and (res1_list[len(res1_list)-1][0] != x['time']) :
                #print("second cond")
                #print(res1_list[len(res1_list)-2][0])
                #print(len(res1_list)-1)
                #print("predydush = ",res1_list[len(res1_list)-1][0])
                #print(x['time'])
                temp = []
                temp.append(x['time'])
                temp.append(x['co2'])
                res1_list.append(temp)
            #print(res1_list)
            #res1_list[0][1]=1030
            #print(res1_list)
            #if (len(res1_list) > 21): #если больше чем надо, значит есть дубликаты, значит удалим последний элемент - это не самое лучшее решение, но по-другому сложнее
            #    while len(res1_list) > 21:
            #        res1_list.pop(-1)
            #if (len(res1_list) < 21 and len(res1_list) > 0 ): #если меньше чем надо, значит не хватает данных, значит продублируем последний элемент - это не самое лучшее решение, но по-другому сложнее
            #   while len(res1_list) > 21:
            #        res1_list.append(res1_list[len(res1_list) - 1 ])
    #print(res1_list[0])
    #print(res1_list[1])
    print(res1_list)
    return res1_list

def draw_grafik_of_CO2(res_lists, count_of_people):
    t_after_start = []

    for res_list_i in res_lists:
        plt.title('Уровень СO2 в D336 в зависимости от количества человек')
        if len(res_list_i)!=0:
            t_after_start = []
            data_for_draw =[]
            for i in range(len(res_list_i)):
                t_after_start.append(i * 5 - 5)
                data_for_draw.append(res_list_i[i][1])
            plt.plot(t_after_start, data_for_draw)
    plt.legend(count_of_people)
    plt.grid(True)
    plt.show()

def calc_average_betwen_40_95(res_lists):
    array_of_aver = []
    for res_list_i in res_lists:
        if len(res_list_i) != 0:
            aver = 0.
            for i in range(len(res_list_i)):
                #if (i>=9):
                    aver+=res_list_i[i][1]
            #aver /= 14.
            aver /= len(res_list_i)
            array_of_aver.append(aver)
    return (array_of_aver)



#print("new")
#with open('smartphone.json') as file:
#  smartphone_dict = json.load(file)
#print("new1")
#print(type(smartphone_dict)) # <class 'dict'>
#features = smartphone_dict['features'] # ['5G', 'HD display', 'Dual camera']
#print(features)

#print("new2")
#with open('test.json') as file:
#  test_list = json.load(file)
#print("new3")
#print(type(test_list)) # <class 'dict'>
#for i in range(2):
#    if(test_list[i]['co2']>183):
#       print (test_list[i]['co2'], " ")

#"print("new10")
#with open('d333.json') as file:
#  d333_list = json.load(file)
#print("new11")
#print(type(d333_list)) # <class 'list'>
#t_after_start = []
#for i in range(21):
#    t_after_start.append(i*5-5)
#print(t_after_start)
#print(len(t_after_start))


#d333_time_start =  ["23-05-03 10:05:05", "23-05-04 13:25:05", "23-06-10 15:05:05","23-06-10 13:25:05","23-06-10 10:05:05","23-06-04 16:45:05","23-06-04 19:00:05","23-06-13 11:45:05","23-06-14 11:45:05","23-06-13 15:05:05","23-06-13 16:45:05","23-06-14 13:25:05","23-06-15 13:25:05","23-06-16 13:25:05","23-06-16 15:05:05","23-06-16 16:45:05"] #, , ,  , "23-06-10 8:25:05"
#d333_time_finish = ["23-05-03 11:45:05", "23-05-04 15:05:05", "23-06-10 16:45:05","23-06-10 15:05:05","23-06-10 11:45:05","23-06-04 18:25:05","23-06-04 20:40:05","23-06-13 13:25:05","23-06-14 13:25:05","23-06-13 16:45:05","23-06-13 18:25:05","23-06-14 15:05:05","23-06-15 15:05:05","23-06-16 15:05:05","23-06-16 16:45:05","23-06-16 18:25:05"] #, ,   , "23-06-10 10:05:05"
#n = len(d333_time_start)
#первый граф+
#второй граф+
#3+
#4+
#5-
#d333_count_of_people = ['12','18-2-1', '0-0-+','21-1-1','23-0-1','26-2-0','0-0-1','16-0-1','0-0-0','17-2-0','20-2-1','1-0-0','19-2-1','18-2-0','17-2-1','0-2-1'] #,,,,'4-0-0'
#d333_res_list = [[]]*n
#for i in range (n):
#    d333_res_list[i]= create_list_of_data_CO2(d333_list,d333_time_start[i], d333_time_finish[i])

#d333_res_list = []
#d333_res_list.append(create_list_of_data_CO2(d333_list,d333_time_start[0], d333_time_finish[0]))
#for i in range (n-1):
#    d333_res_list.append(create_list_of_data_CO2(d333_list,d333_time_start[i+1], d333_time_finish[i+1]))
#d333_res_list[1] = create_list_of_data_CO2(d333_list,"23-05-04 13:25:05", "23-05-04 15:05:05")
#d333_res_list[2] = create_list_of_data_CO2(d333_list,"23-05-30 11:45:05", "23-05-30 13:25:05") нет данных на это время
#d333_res_list[1] = create_list_of_data_CO2(d333_list,"23-05-04 13:25:05", "23-05-04 15:05:05")

#print(len(d333_res_list[0]))
#print(len(d333_res_list[1]))
#print(len(d333_res_list[2]))
#array_of_average = calc_average_betwen_40_95(d333_res_list)
#print(array_of_average)
#draw_grafik_of_CO2(d333_res_list, d333_count_of_people)


#for x in d333_list:
#    if(x['time']>="23-05-03 10:05:05" and x['time']<="23-05-03 11:45:05"):
#        print ("time = ",x['time'], "  co2 = ", x['co2'], " ")
#        res1_list.append(x['co2'])
#    elif(x['time']>="23-05-04 13:25:05" and x['time']<="23-05-04 15:05:05"):
#        res2_list.append(x['co2'])
#        print("time = ", x['time'], "  co2 = ", x['co2'], " ")

#plt.title('My first plot')
#plt.plot([1,2,3,4])
#plt.show()
#print(len(res1_list))
#if (len(res1_list)>21):
#    while len(res1_list) > 21:
#        res1_list.pop(-1)


#if (len(res1_list)>21):
#    while len(res1_list) > 21:
#        res1_list.pop(-1)
#plt.title('My first CO2 plot')
#plt.plot(t_after_start, res_list[0])
#plt.plot(t_after_start, res_list[1])
#plt.legend(['12','18'])
#plt.grid(True)
#plt.show()

#print('23-06-04 16:45:05'!='23-06-04 16:45:05')

#print("new10")
#with open('D331.json') as file:
#  d331_list = json.load(file)
#print("new11")
#print(type(d333_list)) # <class 'list'>
#t_after_start = []
#for i in range(21):
#    t_after_start.append(i*5-5)
#print(t_after_start)
#print(len(t_after_start))


#d331_time_start =  ["23-05-03 10:05:05","23-05-04 13:25:05","23-06-14 13:25:05"] #, , ,  , "23-06-10 8:25:05"
#d331_time_finish = ["23-05-03 11:45:05","23-05-04 15:05:05","23-06-14 15:05:05"] #, ,   , "23-06-10 10:05:05"
#n = len(d331_time_start)

#d331_count_of_people = ['0','0','10-1-0'] #,,,,'4-0-0'

#d331_res_list = []
#d331_res_list.append(create_list_of_data_CO2(d331_list,d331_time_start[0], d331_time_finish[0]))
#for i in range (n-1):
#    d331_res_list.append(create_list_of_data_CO2(d331_list,d331_time_start[i+1], d331_time_finish[i+1]))


#print(len(d331_res_list[0]))

#array_of_average = calc_average_betwen_40_95(d331_res_list)
#print(array_of_average)
#draw_grafik_of_CO2(d331_res_list, d331_count_of_people)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#print("new335")
#with open('D335.json') as file:
#  d335_list = json.load(file)
#print("new11")
#print(type(d333_list)) # <class 'list'>
#t_after_start = []
#for i in range(21):
#    t_after_start.append(i*5-5)
#print(t_after_start)
#print(len(t_after_start))


#d335_time_start =  ["23-06-14 11:25:05","23-06-14 13:05:05"] #, , ,  , "23-06-10 8:25:05"
#d335_time_finish = ["23-06-14 13:05:05","23-06-14 14:45:05"] #, ,   , "23-06-10 10:05:05"
#n = len(d335_time_start)

#d335_count_of_people = ['1-0-0','1-0-0'] #,,,,'4-0-0'

#d335_res_list = []
#d335_res_list.append(create_list_of_data_CO2(d335_list,d335_time_start[0], d335_time_finish[0]))
#for i in range (n-1):
#    d335_res_list.append(create_list_of_data_CO2(d335_list,d335_time_start[i+1], d335_time_finish[i+1]))


#rint(len(d335_res_list[0]))

#array_of_average = calc_average_betwen_40_95(d335_res_list)
#print(array_of_average)
#draw_grafik_of_CO2(d335_res_list, d335_count_of_people)

#print("new336")
#with open('D336.json') as file:
#  d336_list = json.load(file)
#print("new11")
#print(type(d333_list)) # <class 'list'>
#t_after_start = []
#for i in range(21):
#    t_after_start.append(i*5-5)
#print(t_after_start)
#print(len(t_after_start))


#d336_time_start =  ["23-06-14 11:45:05","23-06-14 13:25:05","23-06-14 15:05:05","23-06-15 13:25:05","23-06-16 13:25:05","23-06-16 16:45:05"] #, , ,  , "23-06-10 8:25:05"
#d336_time_finish = ["23-06-14 13:25:05","23-06-14 15:05:05","23-06-14 16:45:05","23-06-15 15:05:05","23-06-16 15:05:05","23-06-16 18:20:05"] #, ,   , "23-06-10 10:05:05"
#n = len(d336_time_start)

#d336_count_of_people = ['11','0-1-1','5','17-2-1','21-2-1','0-0-2'] #,,,,'4-0-0'

#d336_res_list = []
#d336_res_list.append(create_list_of_data_CO2(d336_list,d336_time_start[0], d336_time_finish[0]))
#for i in range (n-1):
#    d336_res_list.append(create_list_of_data_CO2(d336_list,d336_time_start[i+1], d336_time_finish[i+1]))


#print(len(d336_res_list[0]))

#array_of_average = calc_average_betwen_40_95(d336_res_list)
#print(array_of_average)
#draw_grafik_of_CO2(d336_res_list, d336_count_of_people)

print("new338")
with open('D339.json') as file:
  d336_list = json.load(file)
print("new11")
#print(type(d333_list)) # <class 'list'>
t_after_start = []
#for i in range(21):
#    t_after_start.append(i*5-5)
#print(t_after_start)
#print(len(t_after_start))


d336_time_start =  ["23-06-10 8:25:05","23-06-10 13:25:05"] #, , ,  , "23-06-10 8:25:05"
d336_time_finish = ["23-06-10 10:05:05","23-06-10 15:05:05"] #, ,   , "23-06-10 10:05:05"
n = len(d336_time_start)

d336_count_of_people = ['0-0-0','1-0-0'] #,,,,'4-0-0'

d336_res_list = []
d336_res_list.append(create_list_of_data_CO2(d336_list,d336_time_start[0], d336_time_finish[0]))
for i in range (n-1):
    d336_res_list.append(create_list_of_data_CO2(d336_list,d336_time_start[i+1], d336_time_finish[i+1]))


print(len(d336_res_list[0]))

array_of_average = calc_average_betwen_40_95(d336_res_list)
print(array_of_average)
draw_grafik_of_CO2(d336_res_list, d336_count_of_people)
