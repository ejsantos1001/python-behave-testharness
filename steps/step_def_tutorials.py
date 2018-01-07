from behave import *
import endpoints
import db


@when('a user gets all posts')
def step_impl(context):
    r = endpoints.get_posts()
    print (r.text)


@When('get user number {n}')
def step_impl(context,n):
    r = endpoints.get_n_post(n)
    data = db.query("select * from employees limit 3")
    print (data[2])
    print (r.text)











