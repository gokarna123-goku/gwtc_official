from django.shortcuts import redirect, render
from django.views import generic
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
class Index(generic.CreateView):
    template_name = 'homepage/index.html'
    form_class = ContactForm
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            contact_obj = form.save(commit=False)
            contact_obj.save()
            messages.success(request, "Your Form has been submitted successfully!")
            return redirect('home')
        return render(request, self.template_name, {'form':form})


class PortfolioView(generic.TemplateView):
    template_name = 'portfolio/portfolio.html'