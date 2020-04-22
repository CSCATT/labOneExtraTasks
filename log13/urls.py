from django.urls import path
from log13.views import IndexView

urlpatterns = [
	path('', IndexView.as_view())
	]