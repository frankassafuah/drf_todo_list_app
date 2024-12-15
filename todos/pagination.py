from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):

    page_size = 1
    page_size_query_param = 'count' # the name of a query parameter that allows the client to set the page size 
    max_page_size = 5