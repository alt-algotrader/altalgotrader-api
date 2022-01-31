from tasks.celery_app import app


@app.task(name='alt.ex_task')
def ex_task():
    print('hello world')


if __name__ == '__main__':
    ex_task.delay()
