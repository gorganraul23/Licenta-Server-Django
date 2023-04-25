from django.urls import path

from api.views import save_sensor_data, start_session, sensor_data_list, sensor_data_by_session, \
    sensor_data_object, end_session, session_list

urlpatterns = [

    path('start-session', start_session),
    path('end-session/<int:id>', end_session),
    path('session', session_list),

    path('save-sensor-data', save_sensor_data),
    path('sensor-data/session/<int:session>/', sensor_data_by_session),
    path('sensor-data', sensor_data_list),
    path('sensor-data/<int:id>/', sensor_data_object),
]
