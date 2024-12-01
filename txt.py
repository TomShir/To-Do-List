from colorama import Fore 
import time 
import sys 
import random 
import os 
import tqdm
import datetime
commands=['remove.task','add.task','view_all.tasks','exit_program']
colors=[Fore.GREEN,Fore.YELLOW,Fore.RED,Fore.CYAN,Fore.BLUE,Fore.RESET]
count=0
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
        print(f'{colors[-1]}')
    
for text in program_title.upper():
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write(f'\t\t{random.choice(colors[0:-1])}{text}')
else:
    print(f'{colors[-1]}')
    time.sleep(1)
    os.system('cls')
    time.sleep(1)
    loop_over(sequence='Commands:\n\t',delay_time=0.01,color=colors[0])
    time.sleep(1)
    for n in commands:
        count+=1 
        print(f'{colors[3]}{count}. {n}')
        time.sleep(1)
    else:
        time.sleep(1)
    while True:
        enter_command=input(f'{colors[-1]}command:')
        while enter_command not in commands:
            loop_over(sequence=f'Error,{enter_command} is not recognised as a given command,pls try again.',color=colors[2],delay_time=0.1)
            enter_command=input('command:')
            if enter_command in commands:
                pass
            else:
                time.sleep(1)
                loop_over(sequence=f'Error,{enter_command} is not recognised as a given command,pls try again.',color=colors[2],delay_time=0.1)
        else:
            if enter_command==commands[-1]:
                time.sleep(1)
                loop_over(sequence=f'Exitting program...',delay_time=0.1,color=colors[2])  
                time.sleep(1)
                sys.exit(os.system('cls'))
            elif enter_command==commands[1]:
                time.sleep(1)
                add_task=input('task:')
                tasks.append(add_task)
                time.sleep(1)
                Do_you_want_to_add_more_tasks_input=input(f'{colors[1]}Do you want to add another task y/n?:{colors[-1]}')
                if Do_you_want_to_add_more_tasks_input!='y'and Do_you_want_to_add_more_tasks_input!='n':
                    time.sleep(1)
                    loop_over(sequence=f'Error,you did not enter y or n,pls enter the command,{commands[1]}, if you want to add tasks to your to do list. ',delay_time=0.1,color=colors[2])
                else:
                    pass
                while Do_you_want_to_add_more_tasks_input=='y':
                    time.sleep(1)
                    add_task=input('task:')
                    tasks.append(add_task)
                    time.sleep(1)
                    Do_you_want_to_add_more_tasks_input=input(f'{colors[1]}Do you want to add another task y/n?:{colors[-1]}')
                    if Do_you_want_to_add_more_tasks_input=='n':
                        time.sleep(1)
                        #Asking the user whether they want to save their to do list or not 
                        save_input=input('Do you want to save your to do list y/n?:')
                        if save_input=='y':
                            current_time=datetime.datetime.now()
                            with open('to_do_list.','w')as a:
                                a.write('To do List:\n\n')
                                count=0
                                for task in tasks:
                                    count+=1
                                    a.write(f'{count}. {task}- set at {current_time.strftime("%d/%m/%y")}\n')
                                else:
                                    pass 
                        elif save_input=='n':
                            break 
                        elif save_input!='n' or save_input!='y':
                            pass 
                    elif Do_you_want_to_add_more_tasks_input!='n' and Do_you_want_to_add_more_tasks_input!='y':
                        time.sleep(1)
                        loop_over(sequence='Error,you did not enter y or n,pls try again...',delay_time=0.1,color=colors[2]) 
            elif enter_command==commands[0] and tasks==[]:
                loop_over(sequence='Error,You did not have any tasks added to your to do list',delay_time=0.1,color=colors[2])
            elif enter_command==commands[2] and tasks==[]:
                loop_over(sequence='Error,You did not have any tasks added to your to do list',delay_time=0.1,color=colors[2])
            elif enter_command==commands[2]:
                loop_over(sequence='tasks:\n'.title(),delay_time=0.1,color=colors[-2])
                while count>0:
                    count-=1 
                else:
                    pass
                for task in tasks:
                    count+=1 
                    print(f'{count}. {task}')
                    time.sleep(1)
                else:
                    pass
            elif enter_command==commands[0]:
                def task_remover():
                    try:
                     time.sleep(1)
                     #Prompting the user to enter how many tasks they are going to enter
                     how_many_tasks_user_wants_removed=int(input('How many tasks do you want to remove:')) 
                     for n in range(how_many_tasks_user_wants_removed):
                         task_name=input('What is the name of the task you want deleted?:')
                         if task_name not in tasks: 
                             time.sleep(1)
                             loop_over(sequence=f'Error,{task_name} is not present in {tasks}',delay_time=0.1,color=colors[2])
                         else:
                             create_progress_bar(bar_colour='RED',number_of_columns=200,delay_time=0.01,description=f'Removing task,{task_name} from {tasks}')
                             tasks.remove(task_name)
                             os.remove("to_do_list")
                             with open("to_do_list","a") as a:
                                 a.write("To do list:\n")
                                 for position,task in enumerate(tasks):
                                     position+=1
                                     a.write(f'  {position}. {task} - set at {current_time.strftime("%d/%m/%y")}\n')
                     else:
                        loop_over(sequence=f'The current state of your to do list:\n{tasks}',delay_time=0.1,color=colors[-1])                    
                    except ValueError:
                        loop_over(sequence='Error,you did not enter a numerical value,please try again',delay_time=0.1,color=colors[2])                             
                task_remover()
