from colorama import Fore,Style,Back,init
import time 
import sys 
import random 
import os 
import tqdm
import datetime
init()
commands=['remove.task','add.task','view.tasks','exit_program']
text_colors=[Fore.GREEN,Fore.YELLOW,Fore.RED,Fore.CYAN,Fore.BLUE,Fore.RESET]
tasks=[]
program_title='to do list'
def create_progress_bar(bar_colour,number_of_columns,delay_time,description=''):
    for x in tqdm.tqdm(list(range(1,101,1)),colour=bar_colour,ncols=number_of_columns,desc=description):
        time.sleep(delay_time)
    else:
        pass
def loop_over(sequence,delay_time,color):
    for txt in sequence:
            sys.stdout.flush()
            time.sleep(delay_time)
            sys.stdout.write(f'{color}{txt}')
    else:
        print(f'{text_colors[-3]}')
for text in program_title.upper():
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write(f'\t\t{random.choice(text_colors[0:-1])}{text}')
else:
    print(f'{Style.DIM}{text_colors[-3]}')
    time.sleep(1)
    os.system('cls')
    time.sleep(1)
    loop_over(sequence='Commands:\n\t'.upper(),delay_time=0.01,color=text_colors[0])
    time.sleep(1)
    for index_command,n in enumerate(commands,start=1): 
        print(f'{text_colors[0]}{index_command}. {n.upper()}')
        time.sleep(1)
    else:
        time.sleep(1)
    while True:
     try:
        enter_command=input(f'{text_colors[-1]}command:'.upper())
        while enter_command not in commands:
            loop_over(sequence=f'Error,{enter_command} is not recognised as a given command,pls try again.',color=text_colors[2],delay_time=0.1)
            enter_command=input('command:')
            if enter_command in commands:
                pass
        else:
            if enter_command==commands[-1]:
                time.sleep(1)
                loop_over(sequence=f'Exitting program...',delay_time=0.1,color=text_colors[2])  
                time.sleep(1)
                sys.exit(os.system('cls'))
            elif enter_command==commands[1]:
                time.sleep(1)
                add_task=input('task:')
                tasks.append(add_task)
                time.sleep(1)
                Do_you_want_to_add_more_tasks_input=input(f'{text_colors[1]}Do you want to add another task y/n?:{text_colors[-1]}')
                if Do_you_want_to_add_more_tasks_input!='y'and Do_you_want_to_add_more_tasks_input!='n':
                    time.sleep(1)
                    loop_over(sequence=f'Error,you did not enter y or n,pls enter the command,{commands[1]}, if you want to add tasks to your to do list. ',delay_time=0.1,color=text_colors[2])
                else:
                    pass
                while Do_you_want_to_add_more_tasks_input=='y':
                    time.sleep(1)
                    add_task=input('task:')
                    tasks.append(add_task)
                    time.sleep(1)
                    Do_you_want_to_add_more_tasks_input=input(f'{text_colors[1]}Do you want to add another task y/n?:{text_colors[-1]}')
                    if Do_you_want_to_add_more_tasks_input=='n':
                        time.sleep(1)
                        save_input=input('Do you want to save your to do list y/n?:')
                        if save_input=='y':
                            current_time_y_or_n=input("Do you want the tasks for the to do list to be for today or for a future day?\n(enter f for future or enter c for current time):")
                            if current_time_y_or_n=="f":
                             month=int(input("month:"))
                             day=int(input("day:"))
                             year=int(input("year:"))
                            elif current_time_y_or_n=="c":
                                current_time=datetime.datetime.now()
                            with open('to_do_list.txt','a')as a:
                              if current_time_y_or_n=="c":
                                a.write(f'To do List for {current_time.strftime("%d/%m/%y")}:')
                              elif current_time_y_or_n=="f":
                                a.write(f'To do List for {day}/{month}/{year}:')
                              a.write("\n")
                              for task in tasks:
                                    a.write(f'{task}')
                                    a.write("\n")
                              else:
                                a.write("")
                                tasks.clear()
                        elif save_input=='n':
                            tasks.clear()
                            break 
                        elif save_input!='n' or save_input!='y':
                            tasks.clear()
                            pass 
                    elif Do_you_want_to_add_more_tasks_input!='n' and Do_you_want_to_add_more_tasks_input!='y':
                        time.sleep(1)
                        loop_over(sequence='Error,you did not enter y or n,pls try again...',delay_time=0.1,color=text_colors[2]) 
                        tasks.clear()
            elif enter_command==commands[0] or enter_command==commands[2]:
                loop_over(sequence="Error the to_do_list.txt file does not exist",delay_time=0.1,color=text_colors[2])
            elif enter_command  in commands and os.path.exists("to_do_list.txt")==True and tasks==[]:
                enter_date=input("Enter a date:")
                open_txt_file=open("to_do_list.txt","rt")
                dates=[]
                dates_contents=[]
                dates_contents.extend(open_txt_file.readlines())
                for date in dates_contents:
                    if date.startswith("To do List for")==True:
                            dates.append(date[15:-2])
                    else:
                        pass
                else:
                    pass
                if enter_command==commands[2]:
                         if enter_date not in dates:
                             loop_over(sequence="Error,you did not enter a valid date",color=text_colors[1],delay_time=0.1)
                         else:
                             for my_task in dates_contents[dates_contents.index(f"To do List for {enter_date}:\n")+1:]:
                                if my_task.startswith("To do List for")==False:
                                    print(my_task)
                                else:
                                    break  
                             else:
                                 pass
                elif enter_command==commands[0]:
                    if enter_date not in dates:
                             loop_over(sequence="Error,you did not enter a valid date",color=text_colors[1],delay_time=0.1)
                    else:
                         for my_task in dates_contents[dates_contents.index(f"To do List for {enter_date}:\n")+1:]:
                                if my_task.startswith("To do List for")==False and my_task.endswith("\n"):
                                    new_task=my_task.replace("\n","")
                                    tasks.append(new_task)
                                else:
                                    break  
                         else:
                             print(tasks)
                             number_of_tasks_removed=int(input("How many tasks do you want to remove from the list above?:"))
                             for n in range(number_of_tasks_removed):
                                 task_name=input("Task name:")
                                 if task_name in tasks:
                                     create_progress_bar(bar_colour="green",number_of_columns=200,delay_time=0.01,description=f"Removing {task_name}")
                                     tasks.remove(task_name)
                                     for content in dates_contents:
                                         if content.startswith(task_name)==True:
                                             dates_contents.remove(content)
                                         else:
                                             continue
                             else:
                                 open_txt_file.close()
                                 os.remove("to_do_list.txt")
                                 with open("to_do_list.txt","a") as w:
                                    for contents in dates_contents:
                                        w.write(contents)
     except ValueError:
         pass
