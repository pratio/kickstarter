from django_tables2 import SingleTableView

# from kickstarter.models import Projects
# from kickstarter.tables import ProjectsTable


class FilteredTableView(SingleTableView):
    """
    Filter django tables querysets
    """
    filter_class = None
    context_filter_name = 'filter'

    def get_table_data(self):
        """
        Get table data to be filtered
        Return a filtered queryset
        """
        qs = super(FilteredTableView, self).get_table_data()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        """
        Get context data for the filterset
        Return filtered queryset
        """
        context = super(FilteredTableView, self).get_context_data(**kwargs)
        context[self.context_filter_name] = self.filter
        return context
