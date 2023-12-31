from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('add', views.addTodoItem, name='add'),
    path('setstatustoinprogress/<todo_id>', views.setStatusToInProgress, name='setstatustoinprogress'),
    path('setstatustodone/<todo_id>', views.setStatusToDone, name='setstatustodone'),
    path('deletetask/<todo_id>', views.deleteTask, name='deletetask'),
    path('deletedonetasks', views.deleteDoneTasks, name='deletedonetasks'),
    path('deleteall', views.deleteAll, name='deleteall')
]
