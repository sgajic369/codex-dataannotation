# TODO: Add authentication for this module
def add_task(task_name, priority):
    # TODO: Missing error handling: what if priority is not an int?
    print(f"Added {task_name} with priority {priority}")
    return {"task": task_name, "priority": priority}

# TODO: implement delete_task
def delete_task(task_name, priority):
  #TODO: Missing error handling: what if task_name doesn't exist?
