from django.urls import path

from .views import *


urlpatterns = [

    path("calendar/", Calendario.as_view(), name="calendario"),
    path('calendario/', calendario_vista, name="calendario"),
    # path('calendar/', pruebacalendar, name="calendar"),
    path('listado_citas/', listar_cita, name="listado_citas"),
    path('agregar_cita/<int:id_paciente>', agregar_cita, name="agregar_cita"),
    path('modificar_cita/<int:id_cita>', modificar_cita, name="modificar_cita"),
    path('eliminar_cita/<int:id_cita>', eliminar_cita, name="eliminar_cita"),
    path('pacientes_cita/', listar_citapaciente, name="pacientes_cita"),
    # A nivel usuario
    # path('usuario_addCita/<str:pk>/', addcitaCreate.as_view(), name="usuario_addCita"),
    
    path('usuario_addCita/<str:numero_documento>/',
         addcita_usuario, name="usuario_addCita"),
]
