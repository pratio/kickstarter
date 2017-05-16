"""kickstarter_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView


from kickstarter.views import *


urlpatterns = [
    url(r"^$",CategoryCountChartView.as_view(), name='Category_Count'),
    url(r'^kickstarter/projects', ProjectsView.as_view(), name='Projects'),
    url(r'^kickstarter/count/category', CategoryStatusCountView.as_view(), name='Category_Count'),
    url(r'^kickstarter/count/subcategory', SubCategoryStatusCountView.as_view(), name='Sub_Category_Count'),
    url(r'^kickstarter/count/country', CountryStatusCountView.as_view(), name='Country_Count'),
    url(r'^kickstarter/count/monthly', MonthStatusCountView.as_view(), name='Monthly_Count'),
    url(r'^kickstarter/percent/category', CategoryStatusPercentView.as_view(), name='Category_Percent'),
    url(r'^kickstarter/percent/subcategory', SubCategoryStatusPercentView.as_view(), name='Sub_Category_Percent'),
    url(r'^kickstarter/percent/country', CountryStatusPercentView.as_view(), name='Country_Percent'),
    url(r'^kickstarter/percent/monthly', MonthStatusPercentView.as_view(), name='Monthly_Percent'),
    url(r'^kickstarter/charts/count/category', CategoryCountChartView.as_view(), name='Category_Count'),

    url(r'^admin/', admin.site.urls),

]
