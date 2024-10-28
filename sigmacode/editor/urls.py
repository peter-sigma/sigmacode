from django.urls import path
from .views import CodeEditorView

urlpatterns = [
    path('', CodeEditorView.as_view(), name='code_editor'),
]