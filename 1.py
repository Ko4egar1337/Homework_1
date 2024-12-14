from zipfile import ZipFile
import os
import sys
from tkinter import *


print(sys.argv)
for i in sys.argv:
    print(i)

if (len(sys.argv) != 3):
    exit()

username = sys.argv[1]
archive_name = sys.argv[2]

if not os.path.isfile(archive_name):
    exit()

#username = "username"
#archive_name = "C:/Users/mashu/PycharmProjects/pythonProject1/archive.zip"


scale = 1.5
scale = str(int(650 * scale)) + "x" + str(int(320*scale))



current_dir = "root/"

zip_infolist = []
zip_namelist = []

with ZipFile(archive_name, 'a') as zip:


    zip_infolist = zip.infolist()
    zip_namelist = zip.namelist()

    print(zip_namelist)


    def ls():
        temp_str = ""
        temp_list = []
        for item in zip_namelist:
            if item.startswith(current_dir) and (item[len(current_dir):].strip()):
                i = item[len(current_dir):]
                if (i.count('/') == 1):
                    count = 0
                    for q in i:
                        if (q == '/'):
                            break
                        count += 1
                    if (count == len(item[len(current_dir):]) - 1):
                        temp_list.append(item[len(current_dir):])

                elif i.count('/') == 0:
                    temp_list.append(item[len(current_dir):])

        for i in range(len(temp_list) - 1):
            temp_str += f"{temp_list[i]}\n"
        temp_str += temp_list[-1]


        text1.insert("end-1c lineend", f"\n{temp_str}")

    def cd(path):

        if not (path in zip_namelist):
            text1.insert("end-1c lineend", f"\ndoesn't exist")
        #
        elif (path[-1] != '/'):
            text1.insert("end-1c lineend", f"\nnot a dir")
        else:
            global current_dir
            current_dir = path

    def exit():
        root.quit()

    def uniq(path):
        if not(path in zip_namelist):
            text1.insert("end-1c lineend", f"\ndoesn't exist")
        elif not (path[-3:] == "txt"):
            text1.insert("end-1c lineend", f"\nnot a txt file")
        else:
            temp_str = ""
            temp_list = []
            with zip.open(path, 'r') as txt_file:
                for item in txt_file:
                    if not(item in temp_list) and (item.strip()):
                        temp_str += item.decode('utf-8')
                    temp_list.append(item)
                text1.insert("end-1c lineend", f"\n{temp_str}")

    def wc(path):
        if not (path in zip_namelist):
            text1.insert("end-1c lineend", f"\ndoesn't exist")
        elif not (path[-3:] == "txt"):
            text1.insert("end-1c lineend", f"\nnot a txt file")
        else:
            temp_str = ""
            l_count = 0
            ch_count = 0

            with ZipFile(archive_name, 'a') as zip:
                with zip.open(path, 'r') as txt_file:
                    for line in txt_file:
                        if (line.strip()):
                            temp_str += (line.decode('utf-8'))
                            l_count += 1

                    for item in temp_str:
                        if (item.strip()):
                            ch_count += 1

            text1.insert("end-1c lineend", f"\n{l_count} {ch_count} {path}")




    #uniq("root/file1.txt")



    root = Tk()
    root.title("cmd")
    root.geometry(scale)


    text1 = Text()
    text1.pack(expand=1, fill=BOTH)

    command_list = []
    command_list_index = len(command_list)

    text1.insert("end-1c lineend", f"{username}:{current_dir} ")
    def input(event):

        lsd = len(f"{username}:{current_dir} ")
        #lsd = "end-" + str(1 + lsd) + "c linestart"


        str_input = text1.get("end-1c linestart", "end-1c lineend")

        lsd = str_input[lsd:]
        print(lsd, 1)

        command_list.append(lsd)
        global command_list_index
        command_list_index = len(command_list)

        print(str_input)
        temp_list = str_input.split(' ')
        print(temp_list)




        if len(temp_list) > 1:

            parse1 = temp_list[1]
            if parse1 == "exit":
                exit()

            elif parse1 == "cd":
                if len(temp_list) < 3:
                    text1.insert("end-1c lineend", f"\nnot enough arguments")
                elif (temp_list[2] == ''):
                    text1.insert("end-1c lineend", f"\nnot enough arguments")
                else:
                    cd(temp_list[2])

            elif parse1 == "ls":
                ls()

            elif parse1 == "uniq":
                if len(temp_list) < 3:
                    text1.insert("end-1c lineend", f"\nnot enough arguments")
                elif (temp_list[2] == ''):
                    text1.insert("end-1c lineend", f"\nnot enough arguments")
                else:
                    uniq(temp_list[2])
                    #print(temp_list[2])

            elif parse1 == "wc":
                if len(temp_list) < 3:
                    text1.insert("end-1c lineend", f"\nnot enough arguments")
                elif (temp_list[2] == ''):
                    text1.insert("end-1c lineend", f"\nnot enough arguments")
                else:
                    wc(temp_list[2])

            elif (parse1 != ''):
                text1.insert("end-1c lineend", f"\nunknown command")


        text1.insert("end-1c lineend", f"\n{username}:{current_dir} ")
        #text1.xview("lineend")
        text1.see(END)

        return 'break'

    temp_list = []
    temp_list_len = len(temp_list)
    print(temp_list_len)

    def up(event):
        global command_list_index
        #print(command_list_index)
        # if (command_list_index <= len(command_list)) and (command_list_index >= 0):
        #     print(command_list[command_list_index - 1])
        #
        #     text1.delete("end-1c linestart", "end-1c lineend")
        #     text1.insert("end-1c lineend", f"{username}:{current_dir} {command_list[command_list_index - 1]}")
        #
        #     command_list_index -= 1

       # global temp_list_len
        #print(temp_list_len)

        if (command_list_index - 1 > 0):

            command_list_index -= 1

            print(command_list[command_list_index - 1])

            text1.delete("end-1c linestart", "end-1c lineend")
            text1.insert("end-1c lineend", f"{username}:{current_dir} {command_list[command_list_index - 1]}")







        return 'break'

    def down(event):
        global command_list_index
        # global command_list_index
        # print(command_list_index)
        # if (command_list_index < len(command_list)) and (command_list_index >= 0):
        #     text1.delete("end-1c linestart", "end-1c lineend")
        #     text1.insert("end-1c lineend", f"{username}:{current_dir} {command_list[command_list_index - 1]}")
        #
        #     command_list_index +=1
        #
       # global temp_list_len
        #print(temp_list_len)


        if (command_list_index + 1 <= len(command_list)):
            command_list_index += 1

            print(command_list[command_list_index - 1])
            text1.delete("end-1c linestart", "end-1c lineend")
            text1.insert("end-1c lineend", f"{username}:{current_dir} {command_list[command_list_index - 1]}")



        return 'break'

    text1.bind('<Return>', input)

    text1.bind('<Up>', up)
    text1.bind('<Down>', down)

    root.mainloop()

