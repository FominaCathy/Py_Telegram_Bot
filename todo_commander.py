# добавляет в список дел новую строку
# 
#import logg as log_case

def add_str(data):
    name_file= "task_log.txt"
    with open(name_file, "a", encoding = 'utf8') as file:
        file.write(f"{data}\n")

   # log_case.add_logg_str(f"добавили задачу: {data}", "добавление") #логгируем

# достаем данные из файла 
# нужно ли их возвращать как список для дальнейшей с ними работы в модуль interface?
# дела храняться в файле. (??) имя файла поступает на вход (??)
#import x_logg as log_case


def print_case(data = "task_log.txt"):
    todo_list = ""
    with open(data, "r", encoding = 'utf8') as file:
        i = 1
        for line in file:
            todo_list = f'{todo_list} {i} - {line}'
            i += 1
            
    return todo_list
   

def delete_str(task_del):
    data = "task_log.txt"
    temp = "дела с таким номером нет"
    with open(data, "r", encoding = 'utf8') as file:
        temp_list = []
        i = 1
        for line in file:
            if i != task_del: 
                temp_list.append(line)
                
            else:
                temp = (f"дело: {line[:len(line)-2]} - удалено" )
            i += 1

        with open(data, "w", encoding = 'utf8') as file:
            for tsk in temp_list:
                file.write(tsk)

        return temp
 
