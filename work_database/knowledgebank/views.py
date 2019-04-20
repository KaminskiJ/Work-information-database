from django.shortcuts import render
from django.views.generic.base import View
from django.template.response import TemplateResponse
from .forms import QuestionForm, NewClient, NewCountry, ReplyForm
from .models import CountriesData, ClientData, Question, Client, Country, Comment
from knowledgebank import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy


class Home(View):

    def get(self, request):
        return render(request, 'knowledgebank/home.html')


class AddNewCountry(View):
    def get(self, request):
        form = NewCountry()
        return render(request, 'knowledgebank/addcountry.html', {'form': form})

    def post(self, request):
        form = NewCountry(request.POST)
        if form.is_valid():
            country = form.cleaned_data.get('country')
            new_entry = Country(country=country)
            new_entry.save()
            return HttpResponseRedirect(reverse('home'))

        return render(request, 'knowledgebank/addcountry.html', {'form': form})


class AddNewClient(View):
    def get(self, request):
        form = NewClient()
        return render(request, 'knowledgebank/addclient.html', {'form': form})

    def post(self, request):
        form = NewClient(request.POST)
        if form.is_valid():
            client = form.cleaned_data.get('client')
            new_entry = Client(client=client)
            new_entry.save()
            return HttpResponseRedirect(reverse('home'))

        return render(request, 'knowledgebank/addclient.html', {'form': form})


class CountryEntryCreateView(LoginRequiredMixin, CreateView):
    model = CountriesData
    fields = ['country', 'content']
    template_name = 'knowledgebank/newcountryentry.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ClientEntryCreateView(CreateView):
    model = ClientData
    fields = ['client', 'content']
    template_name = 'knowledgebank/newcliententry.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CountriesList(View):
    def get(self, request):
        countries_list = Country.objects.all().order_by('country')
        ctx = {'countries': countries_list}
        return TemplateResponse(request, 'knowledgebank/countrieslist.html', ctx)


class ClientList(View):
    def get(self, request):
        clients_list = Client.objects.all().order_by('client')
        ctx = {'clients': clients_list}
        return TemplateResponse(request, 'knowledgebank/clientslist.html', ctx)


class ClientDetails(View):

    def get(self, request, client_id):
        client_name = Client.objects.get(pk=client_id)
        client_entries = ClientData.objects.filter(client_id=client_id)
        return render(request, 'knowledgebank/clientsview.html', {'client_entries': client_entries, 'client_name': client_name})


class CountryDetails(View):

    def get(self, request, country_id):
        country_name = Country.objects.get(pk=country_id)
        country_entries = CountriesData.objects.filter(country_id=country_id)
        return render(request, 'knowledgebank/countryview.html', {'country_entries': country_entries, 'country_name': country_name})


class PostList(View):

    def get(self, request):
        questions = Question.objects.all().order_by('-creation_date')
        return render(request, 'knowledgebank/questions.html', {'questions': questions})


class CreatePost(LoginRequiredMixin, CreateView):
    model = models.Question
    form_class = QuestionForm
    success_url = reverse_lazy('discussion')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(View):

    def get(self, request, post_id):
        form = ReplyForm()
        post = Question.objects.get(pk=post_id)
        comments = Comment.objects.filter(question=post_id).order_by('-date_comment')
        return render(request, 'knowledgebank/postdetailsview.html', {'post': post, 'form': form, 'comments': comments})

    def post(self, request, post_id):
        form = ReplyForm(request.POST)
        post = Question.objects.get(pk=post_id)
        comments = Comment.objects.filter(question=post_id).order_by('-date_comment')

        if form.is_valid():
            content = form.cleaned_data.get('content')
            author = self.request.user
            new_entry = Comment(author=author, question=Question.objects.get(pk=post_id), content=content)
            new_entry.save()
            return render(request, 'knowledgebank/postdetailsview.html', {'post': post, 'form': form, 'comments': comments})

        return render(request, 'knowledgebank/postdetailsview.html', {'post': post, 'form': form, 'comments': comments})













#to be added
class AuthorDetailView(View):

    def get(self, request, pk):
        questions = Question.objects.filter(author=pk).order_by('-creation_date')
        return render(request, 'knowledgebank/user_questions.html', {'questions': questions})
