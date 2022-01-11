from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.user_login, name='login'),
    path("map/", views.map, name="map"),
    path("user/", views.user, name="user"),

    path("parkinga/", views.parkinga, name="parkinga"),
    path("parkingb/", views.parkingb, name="parkingb"),
    path("parkingc1/", views.parkingc1, name="parkingc1"),
    path("parkingc2/", views.parkingc2, name="parkingc2"),
    path("parkingd/", views.parkingd, name="parkingd"),
    path("parkinge1/", views.parkinge1, name="parkinge1"),
    path("parkinge2/", views.parkinge2, name="parkinge2"),
    path("parkinge3/", views.parkinge3, name="parkinge3"),
    path("parkinge4/", views.parkinge4, name="parkinge4"),
    path("parkingf/", views.parkingf, name="parkingf"),
    path("parkingg/", views.parkingg, name="parkingg"),
    path("parkingh/", views.parkingh, name="parkingh"),
    path("parkingi/", views.parkingi, name="parkingi"),
    path("parkingj/", views.parkingj, name="parkingj"),
    path("parkingk/", views.parkingk, name="parkingk"),
    path("parkingl/", views.parkingl, name="parkingl"),
    path("parkingm/", views.parkingm, name="parkingm"),

    path("update/<str:parking_spot>/", views.update, name="update"),
    path("updateb/<str:parkingb_spot>/", views.updateb, name="updateb"),
    path("updatec1/<str:parkingc1_spot>/", views.updatec1, name="updatec1"),
    path("updatec2/<str:parkingc2_spot>/", views.updatec2, name="updatec2"),
    path("updated/<str:parkingd_spot>/", views.updated, name="updated"),
    path("updatee1/<str:parkinge1_spot>/", views.updatee1, name="updatee1"),
    path("updatee2/<str:parkinge2_spot>/", views.updatee2, name="updatee2"),
    path("updatee3/<str:parkinge3_spot>/", views.updatee3, name="updatee3"),
    path("updatee4/<str:parkinge4_spot>/", views.updatee4, name="updatee4"),
    path("updatef/<str:parkingf_spot>/", views.updatef, name="updatef"),
    path("updateg/<str:parkingg_spot>/", views.updateg, name="updateg"),
    path("updateh/<str:parkingh_spot>/", views.updateh, name="updateh"),
    path("updatei/<str:parkingi_spot>/", views.updatei, name="updatei"),
    path("updatej/<str:parkingj_spot>/", views.updatej, name="updatej"),
    path("updatek/<str:parkingk_spot>/", views.updatek, name="updatek"),
    path("updatel/<str:parkingl_spot>/", views.updatel, name="updatel"),
    path("updatem/<str:parkingm_spot>/", views.updatem, name="updatem"),

    path("delete/<str:parking_spot>/", views.deletea, name="delete"),
    path("deleteb/<str:parkingb_spot>/", views.deleteb, name="deleteb"),
    path("deletec1/<str:parkingc1_spot>/", views.deletec1, name="deletec1"),
    path("deletec2/<str:parkingc2_spot>/", views.deletec2, name="deletec2"),
    path("deleted/<str:parkingd_spot>/", views.deleted, name="deleted"),
    path("deletee1/<str:parkinge1_spot>/", views.deletee1, name="deletee1"),
    path("deletee2/<str:parkinge2_spot>/", views.deletee2, name="deletee2"),
    path("deletee3/<str:parkinge3_spot>/", views.deletee3, name="deletee3"),
    path("deletee4/<str:parkinge4_spot>/", views.deletee4, name="deletee4"),
    path("deletef/<str:parkingf_spot>/", views.deletef, name="deletef"),
    path("deleteg/<str:parkingg_spot>/", views.deleteg, name="deleteg"),
    path("deleteh/<str:parkingh_spot>/", views.deleteh, name="deleteh"),
    path("deletei/<str:parkingi_spot>/", views.deletei, name="deletei"),
    path("deletej/<str:parkingj_spot>/", views.deletej, name="deletej"),
    path("deletek/<str:parkingk_spot>/", views.deletek, name="deletek"),
    path("deletel/<str:parkingl_spot>/", views.deletel, name="deletel"),
    path("deletem/<str:parkingm_spot>/", views.deletem, name="deletem"),

    path("leave/", views.leave, name="leave"),
]
