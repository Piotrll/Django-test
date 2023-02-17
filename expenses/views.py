from django.views.generic.list import ListView
from datetime import datetime
from .forms import ExpenseSearchForm, DateSearchForm
from .models import Expense, Category, Date
from .reports import summary_per_category, search_by_date


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        def dateform():
            return super().get_context_data(
                form=datef,
                object_list=queryset,
                summary_per_category=search_by_date(queryset),
                **kwargs)

        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        datef = DateSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()

            if name:
                queryset = queryset.filter(name__icontains=name)
        if datef.is_valid():
            date1 = datef.cleaned_data.get('date1', '')
            date2 = datef.cleaned_data.get('date2', '')
            if date1 and date2:
                queryset = queryset.filter(date__range=[date1, date2])
                dateform()

        return super().get_context_data(form=form,
                                        object_list=queryset,
                                        summary_per_category=summary_per_category(queryset),
                                        **kwargs)

#Got it working only for exact date in similar way done above but havent saved it. But still I have a partial uderstanding of how django works after 3 evenings
class CategoryListView(ListView):
    model = Category
    paginate_by = 5
