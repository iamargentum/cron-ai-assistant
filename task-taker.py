from constants import TASK_STATUS
from dbThings import getTasksByStatus

# yo! what's your tasks for today?

def showPendingTasks():
    pendingTasks = getTasksByStatus([TASK_STATUS.todo.name, TASK_STATUS.in_progress.name])
    if len(pendingTasks) > 0:
        print("pending tasks:")
        for task in pendingTasks:
            print(f"{task[0]}. {task[1]}")
    else:
        print("no pending tasks")

def getTasks():
    tasks = []

    print("enter tasks for today - (leave a task empty to end the list)")
    while True:
        task = input(f"{len(tasks)+1}. ")
        if task == "":
            break
        tasks.append(task)

    return tasks

print("yo! what's your tasks for today?")
print("these are pending tasks from the past - ")
showPendingTasks()
tasksToBeAdded = getTasks()