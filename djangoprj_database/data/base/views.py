from django.shortcuts import render
from .models import Book
import nltk
nltk.download('punkt')



def parse_query(query):
    tokens = nltk.word_tokenize(query)
    return tokens

def generate_sql_query(tokens):
    query = Book.objects.all()
    for token in tokens:
        query = query.filter(title__icontains=token)
    return query

def query_books(request):
    query = request.GET.get('query')
    if query:
        tokens = parse_query(query)
        results = generate_sql_query(tokens)
    else:
        results = Book.objects.all()
    return render(request, 'results.html', {'results': results})

def htm(request):
    return render(request,'results.html',{})
