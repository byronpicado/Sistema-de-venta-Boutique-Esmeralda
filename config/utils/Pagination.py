
from rest_framework.pagination import PageNumberPagination

class PaginationMixin:
    pagination_class = PageNumberPagination

    def paginate_queryset(self, queryset, request, view=None):
        self.paginator = self.pagination_class()
        self.paginator.page_size = 10  # Puedes definirlo en settings si prefieres
        return self.paginator.paginate_queryset(queryset, request, view=view)

    def get_paginated_response(self, data):
        return self.paginator.get_paginated_response(data)
