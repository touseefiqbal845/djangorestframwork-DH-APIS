class PrintMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"📢 Request URL: {request.path} | Method: {request.method}")
        return self.get_response(request)
