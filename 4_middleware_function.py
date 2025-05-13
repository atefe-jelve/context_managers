"""
    here we create a middleware with functions

"""

def first(get_response): # get_response is the view that called

    def middleware(request):
        print("before ......")
        responce = get_response(request) 
        print("after .......")

        return responce

    return middleware