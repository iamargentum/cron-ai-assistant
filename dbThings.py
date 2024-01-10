import sqlite3
import functools
from constants import TASK_STATUS

conn = sqlite3.connect('assistantThings.db')
cursor = conn.cursor()

# create task
def createTask(task):
    cursor.execute(f"INSERT INTO tasks (task) VALUES ('{task}')")
    conn.commit()

# delete task
def deleteTask(task):
    cursor.execute(f"DELETE FROM tasks WHERE task = '{task}'")
    conn.commit()

# get pending tasks
def getPendingTasks():
    cursor.execute(f"SELECT * FROM tasks WHERE status = '{TASK_STATUS.todo.name}'")
    return cursor.fetchall()

# get in-progress tasks
def getInProgressTasks():
    cursor.execute(f"SELECT * FROM tasks WHERE status = '{TASK_STATUS.in_progress.name}'")
    return cursor.fetchall()

# get completed tasks
def getCompletedTasks():
    cursor.execute(f"SELECT * FROM tasks WHERE status = '{TASK_STATUS.complete.name}'")
    return cursor.fetchall()

# get parked tasks
def getParkedTasks():
    cursor.execute(f"SELECT * FROM tasks WHERE status = '{TASK_STATUS.parked.name}'")
    return cursor.fetchall()

# get deleted tasks
def getDeletedTasks():
    cursor.execute(f"SELECT * FROM tasks WHERE status = '{TASK_STATUS.deleted.name}'")
    return cursor.fetchall()

# update task status
def updateTaskStatus(task, status):
    cursor.execute(f"UPDATE tasks SET status = '{status}' WHERE task = '{task}'")
    conn.commit()

# get task status
def getTaskStatus(task):
    cursor.execute(f"SELECT status FROM tasks WHERE task = '{task}'")
    return cursor.fetchone()[0]

# get tasks by status
def getTasksByStatus(statusList: list):
    statusList = functools.reduce(lambda x, y: f"{x}, {y}", statusList)
    cursor.execute(f"SELECT * FROM tasks WHERE status in ({statusList})")
    return cursor.fetchall()

# create tasks in bulk
def createTasks(tasks: list):
    cursor.executemany("INSERT INTO tasks (task) VALUES (?)", [(task,) for task in tasks])
    conn.commit()