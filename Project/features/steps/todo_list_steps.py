from behave import given, when, then
from todo_list import TodoList

@given('the to-do list is empty')
def step_impl_empty_list(context):
    context.todo_list = TodoList()

@when('the user adds a task "{task_name}"')
def step_impl_add_task(context, task_name):
    context.todo_list.add_task(task_name)

@then('the to-do list should contain "{task_name}"')
def step_impl_check_task_exists(context, task_name):
    tasks = context.todo_list.list_tasks()
    assert any(task["name"] == task_name for task in tasks), f"Task '{task_name}' not found"

@given('the to-do list contains tasks:')
def step_impl_given_tasks(context):
    context.todo_list = TodoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'])

@when('the user lists all tasks')
def step_impl_list_tasks(context):
    context.listed_tasks = context.todo_list.list_tasks()

@then('the output should contain:')
def step_impl_check_task_output(context):
    expected_output = context.text.strip().splitlines()
    actual_output = ["Tasks:"]
    actual_output.extend([f"- {task['name']}" for task in context.listed_tasks])
    assert expected_output == actual_output, f"Expected: {expected_outout}, but got: {actual_output}"

@when('the user marks task "{task_name}" as completed')
def step_impl_mark_task_completed(context, task_name):
    context.todo_list.mark_task_as_completed(task_name)

@then('the to-do list should show task "{task_name}" as completed')
def step_impl_check_task_completed(context, task_name):
    task = next((task for task in context.todo_list.list_tasks() if task["name"] == task_name), None)
    assert task and task["status"] == "Completed", f"Task '{task_name}' is not completed"

@when('the user clears the to-do list')
def step_impl_clear_tasks(context):
    context.todo_list.clear_tasks()

@then('the to-do list should be empty')
def step_impl_check_empty_list(context):
    assert len(context.todo_list.list_tasks()) == 0, "The to-do list is not empty"

@when('the user deletes task "{task_name}"')
def step_impl_delete_task(context, task_name):
    context.todo_list.delete_task(task_name)

@then('the to-do list should not contain "{task_name}"')
def step_impl_check_task_not_exists(context, task_name):
    tasks = context.todo_list.list_tasks()
    assert not any(task["name"] == task_name for task in tasks), f"Task '{task_name}' should not be in the to-do list"

@when('the user edits task "{old_name}" to "{new_name}"')
def step_impl_edit_task(context, old_name, new_name):
    context.todo_list.edit_task(old_name, new_name)

@then('the to-do list should contain task "{new_name}"')
def step_impl_check_task_renamed(context, new_name):
    tasks = context.todo_list.list_tasks()
    assert any(task["name"] == new_name for task in tasks), f"Task '{new_name}' not found in the to-do list"
