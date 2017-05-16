from django.shortcuts import render

from kickstarter.utils import FilteredTableView
from kickstarter.models import *
from kickstarter.tables import *
from kickstarter.filters import *


class ProjectsView(FilteredTableView):
    """
    Renders a table of all projects
    """
    model = Kickstarter
    template_name = 'list.html'
    context_object_name = 'projects'
    ordering = ['id']
    table_class = ProjectsTable
    filter_class = ProjectsFilter


class CategoryStatusCountView(FilteredTableView):
    """
    Render a table of projects count by category
    and status
    """
    model = CategoryStatusCount
    template_name = 'list.html'
    context_object_name = 'projects'
    ordering = ['id']
    table_class = CategoryStatusCountTable
    filter_class = CategoryStatusCountFilter


class SubCategoryStatusCountView(FilteredTableView):
    """
    Render a table of projects count by sub_category
    and status
    """
    model = SubCategoryStatusCount
    template_name = 'list.html'
    context_object_name = 'projects'
    ordering = ['id']
    table_class = SubCategoryStatusCountTable
    filter_class = SubCategoryStatusCountFilter


class CountryStatusCountView(FilteredTableView):
    """
    Render a table of projects count by country
    and status
    """
    model = CountryStatusCount
    template_name = 'list.html'
    context_object_name = 'projects'
    ordering = ['id']
    table_class = CountryStatusCountTable
    filter_class = CountryStatusCountFilter


class MonthStatusCountView(FilteredTableView):
    """
    Render a table of projects count by month
    and status
    """
    model = MonthStatusCount
    template_name = 'list.html'
    context_object_name = 'projects'
    ordering = ['id']
    table_class = MonthStatusCountTable
    filter_class = MonthStatusCountFilter


class CategoryStatusPercentView(FilteredTableView):
    """
    Render a table of projects percent by category
    and status
    """
    model = CategoryStatusPercent
    template_name = 'list.html'
    context_object_name = 'projects'
    ordering = ['id']
    table_class = CategoryStatusPercentTable
    filter_class = CategoryStatusPercentFilter


class SubCategoryStatusPercentView(FilteredTableView):
    """
    Render a table of projects percent by sub_category
    and status
    """
    model = SubCategoryStatusPercent
    template_name = 'list.html'
    context_object_name = 'projects'
    ordering = ['id']
    table_class = SubCategoryStatusPercentTable
    filter_class = SubCategoryStatusPercentFilter


class CountryStatusPercentView(FilteredTableView):
    """
    Render a table of percent count by country
    and status
    """
    model = CountryStatusPercent
    template_name = 'list.html'
    context_object_name = 'projects'
    ordering = ['id']
    table_class = CountryStatusPercentTable
    filter_class = CountryStatusPercentFilter


class MonthStatusPercentView(FilteredTableView):
    """
    Render a table of projects percent by month
    and status
    """
    model = MonthStatusPercent
    template_name = 'list.html'
    context_object_name = 'projects'
    ordering = ['id']
    table_class = MonthStatusPercentTable
    filter_class = MonthStatusPercentFilter


class CategoryCountChartView(FilteredTableView):
    """
    Render a chart of Projects count by
    category
    """
    model = CategoryStatusCount
    template_name = 'charts.html'
    context_object_name = 'projects'
    ordering = ['id']
    table_class = CategoryStatusCountTable
    filter_class = CategoryStatusCountFilter
