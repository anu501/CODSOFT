tasks=[]
def add_task():
    task=input("enter a new task:")
    tasks.append(task)
    print("task added successfully:")
def view_tasks():
    if len(tasks)==0:
        print("no tasks")
    else:
        print('list of tasks:')
        for i, task in enumerate(tasks):
            print(f'{i+1},{task}')
def delete_task():
    if len(tasks)==0:
        print("no tasks to delete")
    else:
        print('tasks:')
        for i, task in enumerate(tasks):
            print(f'{i+1},{task}')
        choice=int(input('enter the task number to delete:'))
        if 0 < choice<= len(tasks):
            del tasks[choice-1]
            print("task deleted successfully")
        else:
            print("invalid task number")
def main():
    while True:
        print("\n------TO-DO-list Application------")
        print("1. add task")
        print("2. view task")
        print("3. delete task")
        print("4. exit task")
        choice=int(input("enteryour choice:"))
        if choice==1:
            add_task()
        elif choice==2:
            view_tasks()
        elif choice==3:
            delete_task()
        elif choice==4:
            print(" to-do list applicatom success")
            break
        else:
            print("invalid choice you entered")

if __name__=="__main__":
   main()




            
        