from django.db.models import Q

class SearchFeatures:
    def __init__(self, queryset, query_params):
        self.queryset = queryset
        self.query_params = query_params

    def search(self):
        keyword = self.query_params.get("keyword", "")
        if keyword:
            self.queryset = self.queryset.filter(
                Q(name__icontains=keyword) |
                Q(career__icontains=keyword) |
                Q(speciality__icontains=keyword)
            )
        return self

    def filter(self):
        filter_params = self.query_params.copy()
        remove_fields = ["keyword", "page", "limit"]
        
        for field in remove_fields:
            filter_params.pop(field, None)
        
        if filter_params:
            self.queryset = self.queryset.filter(**filter_params)
        return self

    def pagination(self, result_per_page):
        page = int(self.query_params.get("page", 1))
        start = (page - 1) * result_per_page
        end = start + result_per_page
        self.queryset = self.queryset[start:end]
        return self

    def get_queryset(self):
        return self.queryset
