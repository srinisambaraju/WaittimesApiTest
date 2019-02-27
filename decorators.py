import aftership

def new_decorator(original_func):

    def wrap_func():

        print('Some extra code, before the original function')

        original_func()

        print('Some extra code after the original function')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print('I want to be decorated')

func_needs_decorator()

#decorated_func = new_decorator(func_needs_decorator)

#decorated_func

#decorated_func()

def TestAPI():
    api = aftership.APIv4('33ab0b24-106a-40e3-8220-4e5945d57c5e')
    # couriers = api.couriers.all.get()
    onetwo = ''
    slug = 'ups'
    number = '1Z6962EX0237423973'
    api.trackings.post(tracking=dict(slug=slug, tracking_number=number))
    tracking = api.trackings[slug][number].get()['tracking']
    test = 'asdfas'

TestAPI()