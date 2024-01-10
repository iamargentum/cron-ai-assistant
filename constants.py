from enum import Enum

TASK_STATUS = Enum('TASK_STATUS', [
    "todo",
    "in_progress",
    "complete",
    "deleted",
    "parked"
])