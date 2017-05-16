import django_filters

from kickstarter.models import *


class ProjectsFilter(django_filters.FilterSet):
    """
    Create a query set of activations with plan,type,channel,status,owner etc
    """

    class Meta:
        """
        Fields to be filtered
        """
        model = Projects
        fields = ['name', 'category', 'sub_category']


class CategoryStatusCountFilter(django_filters.FilterSet):
    """
    Create a query set of Project count by Category and status
    """

    class Meta:
        """
        Fields to be filtered
        """
        model = CategoryStatusCount
        fields = ['category']


class SubCategoryStatusCountFilter(django_filters.FilterSet):
    """
    Create a query set of Project count by Category and status
    """

    class Meta:
        """
        Fields to be filtered
        """
        model = SubCategoryStatusCount
        fields = ['sub_category']


class CountryStatusCountFilter(django_filters.FilterSet):
    """
    Create a query set of Project count by Category and status
    """

    class Meta:
        """
        Fields to be filtered
        """
        model = CountryStatusCount
        fields = ['country']

    @property
    def count(self):
        """
        Count all activations
        """
        queryset = super(CategoryStatusCountFilter, self).qs
        return queryset


class MonthStatusCountFilter(django_filters.FilterSet):
    """
    Create a query set of Project count by Category and status
    """

    class Meta:
        """
        Fields to be filtered
        """
        model = MonthStatusCount
        fields = ['month']


class CategoryStatusPercentFilter(django_filters.FilterSet):
    """
    Create a query set of Project count by Category and status
    """

    class Meta:
        """
        Fields to be filtered
        """
        model = CategoryStatusPercent
        fields = ['category']


class SubCategoryStatusPercentFilter(django_filters.FilterSet):
    """
    Create a query set of Project count by Category and status
    """

    class Meta:
        """
        Fields to be filtered
        """
        model = SubCategoryStatusPercent
        fields = ['sub_category']


class CountryStatusPercentFilter(django_filters.FilterSet):
    """
    Create a query set of Project count by Category and status
    """

    class Meta:
        """
        Fields to be filtered
        """
        model = CountryStatusPercent
        fields = ['country']


class MonthStatusPercentFilter(django_filters.FilterSet):
    """
    Create a query set of Project count by Category and status
    """

    class Meta:
        """
        Fields to be filtered
        """
        model = MonthStatusPercent
        fields = ['month']
