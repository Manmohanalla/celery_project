from celery import Celery
from celery.schedules import crontab



app = Celery('tasks', backend='amqp', broker='amqp://guest:guest@localhost')

x = 1
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.gen_prime',
        'schedule': 5.0,
        'args': [100]
    },
}
app.conf.timezone = 'UTC'

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(5.0, print_hello.s(), name='add every 5 amazon')
    sender.add_periodic_task(5.0, print_hello.s(), name='add every 5 ebay')

    # # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )

@app.task
def print_hello():
    print 'hello there'

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)

#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         test.s('Happy Mondays!'),
#     )

@app.task
def test(arg):
    print arg

@app.task
def gen_prime(x):
    multiples = []
    results = []
    print 'hello there asss'
    for i in xrange(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in xrange(i*i, x+1, i):
                multiples.append(j)
    print 'hello there'
    return results

	
# celery -A tasks worker --loglevel=info -B
