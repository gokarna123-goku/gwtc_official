from django.shortcuts import redirect, render
from django.views import generic
from .forms import ContactForm
from django.contrib import messages
from .models import Portfolio, PortfolioCategory

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
    
    def get(self, request, *args, **kwargs):
        portfolio = Portfolio.objects.all()[:4]
        context = {
            'portfolio' : portfolio,
        }
        return render(request, self.template_name, context)


class PortfolioView(generic.ListView):
    template_name = 'portfolio/portfolio.html'
    def get(self, request, *args, **kwargs):
        portfolio = Portfolio.objects.all()
        # cat_id = self.kwargs.get('pk')
        # print(cat_id, " Category Id")
        # portfolio_category = PortfolioCategory.objects.all()[:4]
        # print(portfolio_category, " Category Name")
        context = {
            'portfolio' : portfolio,
            # 'portfolio_category' : portfolio_category,
        }
        return render(request, self.template_name, context)

