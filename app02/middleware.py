from django.http import HttpResponse


class SimpleMiddleware1:
    def __init__(self, get_response):
        self.get_response = get_response
         # 配置和初始化

    def __call__(self, request):

        # 在这里编写视图和后面的中间件被调用之前需要执行的代码
        # 这里其实就是旧的process_request()方法的代码
        print("SimpleMiddleware1中的process_request方法被调用")

        # return HttpResponse("直接返回")

        response = self.get_response(request)
        print("SimpleMiddleware1中的process_response方法被调用")
        # 在这里编写视图调用后需要执行的代码
        # 这里其实就是旧的process_response()方法的代码

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("SimpleMiddleware1中的process_view方法被调用")

    def process_exception(self,request,exception):
        print("SimpleMiddleware1中的process_exception方法被调用")

    def process_template_response(self,request,response):
        # 默认不执行这个函数，除非views函数中返回的实例对象（注意这里这个词）中有render（）方法
        print("SimpleMiddleware1中的process_template_response方法被调用")
        return response





class SimpleMiddleware2:
    def __init__(self, get_response):
        self.get_response = get_response
         # 配置和初始化

    def __call__(self, request):

        # 在这里编写视图和后面的中间件被调用之前需要执行的代码
        # 这里其实就是旧的process_request()方法的代码
        print("SimpleMiddleware2中的process_request方法被调用")
        response = self.get_response(request)
        print("SimpleMiddleware2中的process_response方法被调用")
        # 在这里编写视图调用后需要执行的代码
        # 这里其实就是旧的process_response()方法的代码

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("SimpleMiddleware2中的process_view方法被调用")

    def process_exception(self,request,exception):
        print("SimpleMiddleware2中的process_exception方法被调用")

    def process_template_response(self,request,response):
        # 默认不执行这个函数，除非views函数中返回的实例对象（注意这里这个词）中有render（）方法
        print("SimpleMiddleware2中的process_template_response方法被调用")
        return response

