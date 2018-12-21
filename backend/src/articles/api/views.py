from django.http import HttpResponse
import csv, io 
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from rest_framework.generics import ListAPIView, RetrieveAPIView
from articles.models import Article
from articles.models import Candidate
from articles.models import Company
from .serializers import ArticleSerializer


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# @permission_required('admin.can_add_log_entry')
def candidate_upload(request):
    template = "candidate_upload.html"

    prompt = {
        'order': 'Order of the CSV should be candidate_id, communication_score, coding_score, title, company_id'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Candidate.objects_update_or_create(
            candidate_id=column[0],
            communication_score=column[1],
            coding_score=column[2],
            title=column[3],
            company_id=column[4]
        )
    context = {}

    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def company_upload(request):
    template = "company_upload.html"

    prompt = {
        'order': "Order of csv should be first_name, last_name, email, ip_address, message"
    }
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This file is not a .csv file")

    data_set = csv_file.read().decode('utf-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Company.objects.update_or_create(
            company_id=column[0],
            fractal_index=column[1],
        )

    context = {}
    return render(request, template, context)




def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="score-records (1).csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C',
                     '"Testing"', "Here's a quote"])

    return response
