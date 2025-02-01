from django.urls import path

from .views import save_sensor_data, start_session, sensor_data_all, sensor_data_by_session, \
    sensor_data_by_id, end_session, session_all, session_by_id, set_ref_hrv_for_session, session_running, \
    save_ppg_green_data

urlpatterns = [

    path('start-session/<int:id>', start_session),
    path('set-reference', set_ref_hrv_for_session),
    path('end-session/<int:id>', end_session),

    path('session', session_all),
    path('session/<int:id>/', session_by_id),

    path('save-sensor-data', save_sensor_data),
    path('save-ppg-green-data', save_ppg_green_data),

    path('sensor-data/session/<int:id>/', sensor_data_by_session),
    path('sensor-data', sensor_data_all),
    path('sensor-data/<int:id>/', sensor_data_by_id),

    path('session/running', session_running),
]
