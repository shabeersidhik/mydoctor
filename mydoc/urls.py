from django.urls import path
from .import views

urlpatterns=[

    path('',views.fn_home),
    path('login/',views.fn_login),
    path('load/',views.fn_load),
    path('userreg/',views.fn_userregister),
    path('docreg/',views.fn_doctorregister),
    path('admin/',views.fn_admin),
    path('adminlog/',views.fn_adminlog),
    path('userreglog/',views.fn_ureglog),
    path('docreglog/',views.fn_dreglog),
    path('about/',views.fn_about),
    path('adddep/',views.fn_add),
    path('adddepartment/',views.fn_adddep),
    path('adminhome/',views.fn_adminhome),
    path('editdepartment/',views.fn_editdep),
    path('deptadd/',views.fn_depadd),
    path('listdoctor/',views.fn_listdoc),
    path('doctorprofile/',views.fn_doctprofile),
    path('ldbkng/',views.fn_loadbkng),
    path('mybooking/',views.fn_mybooking),
    path('myappoinments/',views.fn_myappoinments),
    path('mypatients/',views.fn_patient),
    path('editpatient/',views.fn_editpat),
    path('doctorlist/',views.fn_doctor),
    path('doctorprofilelist/',views.fn_doctprofilelist),
    path('homes/',views.fn_homes),
    path('editdoctor/',views.fn_editdoctor),
    path('change/',views.fn_change),
    path('changes/',views.fn_changes),
    path('editdoc/',views.fn_editdoc),
    path('edituser/',views.fn_edituser),
    path('saveuser/',views.fn_saveuser),
    path('passsuccess/',views.fn_passwordchange),
    path('dochome/',views.fn_dochome),
    path('savedoc/',views.fn_savedoctor),
    
   
    
]