import django_tables2 as tables

from kickstarter.models import *


class ProjectsTable(tables.Table):
    """
    Create a table object from the queryset
    """

    class Meta:
        """
        Define the model for queryset, columns to be excluded and other options
        """
        model = Projects
        exclude = 'id'


class CategoryStatusCountTable(tables.Table):
    """
    Create a table object from the queryset
    """

    class Meta:
        """
        Define the model for queryset, columns to be excluded and other options
        """
        model = CategoryStatusCount
        exclude = 'id'


class SubCategoryStatusCountTable(tables.Table):
    """
    Create a table object from the queryset
    """

    class Meta:
        """
        Define the model for queryset, columns to be excluded and other options
        """
        model = SubCategoryStatusCount
        exclude = 'id'


class CountryStatusCountTable(tables.Table):
    """
    Create a table object from the queryset
    """

    class Meta:
        """
        Define the model for queryset, columns to be excluded and other options
        """
        model = CountryStatusCount
        exclude = 'id'


class MonthStatusCountTable(tables.Table):
    """
    Create a table object from the queryset
    """

    class Meta:
        """
        Define the model for queryset, columns to be excluded and other options
        """
        model = MonthStatusCount
        exclude = 'id'


class CategoryStatusPercentTable(tables.Table):
    """
    Create a table object from the queryset
    """

    class Meta:
        """
        Define the model for queryset, columns to be excluded and other options
        """
        model = CategoryStatusCount
        exclude = 'id'


class SubCategoryStatusPercentTable(tables.Table):
    """
    Create a table object from the queryset
    """

    class Meta:
        """
        Define the model for queryset, columns to be excluded and other options
        """
        model = SubCategoryStatusPercent
        exclude = 'id'


class CountryStatusPercentTable(tables.Table):
    """
    Create a table object from the queryset
    """

    class Meta:
        """
        Define the model for queryset, columns to be excluded and other options
        """
        model = CountryStatusPercent
        exclude = 'id'


class MonthStatusPercentTable(tables.Table):
    """
    Create a table object from the queryset
    """

    class Meta:
        """
        Define the model for queryset, columns to be excluded and other options
        """
        model = MonthStatusPercent
        exclude = 'id'
