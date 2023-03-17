from django.urls import path

from myschoolapp import views, adminview, teacherview, studentview, parentview

urlpatterns = [
    path('',views.index,name='index'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('logoutview',views.logoutview,name='logoutview'),
    path('treg',views.treg,name='treg'),
    path('sreg',views.sreg,name='sreg'),
    path('preg',views.preg,name='preg'),
    path('adindex',views.adindex,name='adindex'),
    path('tindex',views.tindex,name='tindex'),
    path('sindex',views.sindex,name='sindex'),
    path('pindex',views.pindex,name='pindex'),
    path('tcgindex',views.tcgindex,name='tcgindex'),
    path('scgindex',views.scgindex,name='scgindex'),
    path('pcgindex',views.pcgindex,name='pcgindex'),
    path('teacherview',adminview.teacherview,name='teacherview'),
    path('teacherat',adminview.teacherat,name='teacherat'),
    path('dele/<int:id>/',adminview.dele,name='dele'),



    # path('add_attendance',adminview.add_attendance,name='add_attendance'),
    # path('teacherattendanceview',adminview.teacherattendanceview,name='teacherattendanceview'),
    path('mark/<int:id>',adminview.mark,name='mark'),
    path('view_attendance',adminview.view_attendance,name='view_attendance'),
    path('day_attendance/<date>',adminview.day_attendance,name='day_attendance'),
    # path('day_attendance',adminview.day_attendance,name='day_attendance'),
    # path('upteacherattendance/<int:id>/',teacherview.upteacherattendance,name='upteacherattendance'),
    # path('deleteacherattendance/<int:id>/',teacherview.deleteacherattendance,name='deleteacherattendance'),





    path('studentview',teacherview.studentview,name='studentview'),
    path('delestudent/<int:id>/',teacherview.delestudent,name='delestudent'),
    path('deleparent/<int:id>/',teacherview.deleparent,name='deleparent'),


    path('parentview',teacherview.parentview,name='parentview'),

    path('tstaffmeetingview',teacherview.tstaffmeetingview,name='tstaffmeetingview'),
    path('tdutyview',teacherview.tdutyview,name='tdutyview'),
    path('communitygroupview',teacherview.communitygroupview,name='communitygroupview'),


    path('addcourse',adminview.addcourse,name='addcourse'),
    path('upcourse/<int:id>/',adminview.upcourse,name='upcourse'),
    path('delecourse/<int:id>/',adminview.delecourse,name='delecourse'),

    path('courseview',adminview.courseview,name='courseview'),
    path('addsyllabus',adminview.addsyllabus,name='addsyllabus'),
    path('syllabusview',adminview.syllabusview,name='syllabusview'),
    path('upsyllabus/<int:id>/',adminview.upsyllabus,name='upsyllabus'),
    path('delesyllabus/<int:id>/',adminview.delesyllabus,name='delesyllabus'),



    path('addtimetable',adminview.addtimetable,name='addtimetable'),
    path('timetableview',adminview.timetableview,name='timetableview'),
    path('uptimetable/<int:id>/',adminview.uptimetable,name='uptimetable'),
    path('deletimetable/<int:id>/',adminview.deletimetable,name='deletimetable'),



    path('addexamtable',adminview.addexamtable,name='addexamtable'),
    path('examtableview',adminview.examtableview,name='examtableview'),
    path('upexamtable/<int:id>/',adminview.upexamtable,name='upexamtable'),
    path('deleexamtable/<int:id>/',adminview.deleexamtable,name='deleexamtable'),




    path('addduty',adminview.addduty,name='addduty'),
    path('dutyview',adminview.dutyview,name='dutyview'),
    path('upduty/<int:id>/',adminview.upduty,name='upduty'),
    path('deleduty/<int:id>/',adminview.deleduty,name='deleduty'),


    path('addexamresult',adminview.addexamresult,name='addexamresult'),
    path('examresultview',adminview.examresultview,name='examresultview'),
    path('upexamresult/<int:id>/',adminview.upexamresult,name='upexamresult'),
    path('deleexamresult/<int:id>/',adminview.deleexamresult,name='deleexamresult'),



    path('addstaffmeeting',adminview.addstaffmeeting,name='addstaffmeeting'),
    path('staffmeetingview',adminview.staffmeetingview,name='staffmeetingview'),
    path('upstaffmeeting/<int:id>/',adminview.upstaffmeeting,name='upstaffmeeting'),
    path('delestaffmeeting/<int:id>/',adminview.delestaffmeeting,name='delestaffmeeting'),


    path('addparentsmeeting',adminview.addparentsmeeting,name='addparentsmeeting'),
    path('parentsmeetingview',adminview.parentsmeetingview,name='parentsmeetingview'),
    path('upparentsmeeting/<int:id>/',adminview.upparentsmeeting,name='upparentsmeeting'),
    path('deleparentsmeeting/<int:id>/',adminview.deleparentsmeeting,name='deleparentsmeeting'),

    path('addcommunitygroup',adminview.addcommunitygroup,name='addcommunitygroup'),
    path('admincommunitygroupview',adminview.admincommunitygroupview,name='admincommunitygroupview'),
    path('upcommunitygroup/<int:id>/',adminview.upcommunitygroup,name='upcommunitygroup'),
    path('delecommunitygroup/<int:id>/',adminview.delecommunitygroup,name='delecommunitygroup'),
    path('managecommunitygroup',adminview.managecommunitygroup,name='managecommunitygroup'),


    path('tsyllabusview',teacherview.tsyllabusview,name='tsyllabusview'),
    path('texamtableview',teacherview.texamtableview,name='texamtableview'),
    path('ttimetableview',teacherview.ttimetableview,name='ttimetableview'),
    path('tparentsmeetingview',teacherview.tparentsmeetingview,name='tparentsmeetingview'),


    path('addstudymaterial',teacherview.addstudymaterial,name='addstudymaterial'),
    path('studymaterialview',teacherview.studymaterialview,name='studymaterialview'),
    path('upstudymaterial/<int:id>/',teacherview.upstudymaterial,name='upstudymaterial'),
    path('delestudymaterial/<int:id>/',teacherview.delestudymaterial,name='delestudymaterial'),


    path('addmark',teacherview.addmark,name='addmark'),
    path('markview',teacherview.markview,name='markview'),
    path('upmark/<int:id>/',teacherview.upmark,name='upmark'),
    path('delemark/<int:id>/',teacherview.delemark,name='delemark'),

    path('texamresultview',teacherview.texamresultview,name='texamresultview'),
    path('tprojectview',teacherview.tprojectview,name='tprojectview'),
    path('addprojectmark/<int:id>/',teacherview.addprojectmark,name='addprojectmark'),
    path('tassignmentview',teacherview.tassignmentview,name='tassignmentview'),
    path('addassignmentmark/<int:id>/',teacherview.addassignmentmark,name='addassignmentmark'),
    path('tseminarview',teacherview.tseminarview,name='tseminarview'),
    path('addseminarmark/<int:id>/',teacherview.addseminarmark,name='addseminarmark'),
    path('thwview',teacherview.thwview,name='thwview'),
    path('addhwmark/<int:id>/',teacherview.addhwmark,name='addhwmark'),


    path('ssyllabusview',studentview.ssyllabusview,name='ssyllabusview'),
    path('sexamtableview',studentview.sexamtableview,name='sexamtableview'),
    path('stimetableview',studentview.stimetableview,name='stimetableview'),
    path('sstudymaterialview',studentview.sstudymaterialview,name='sstudymaterialview'),
    path('smarkview',studentview.smarkview,name='smarkview'),
    path('sexamresultview',studentview.sexamresultview,name='sexamresultview'),

    path('addnote',studentview.addnote,name='addnote'),
    path('noteview',studentview.noteview,name='noteview'),
    path('upnote/<int:id>/',studentview.upnote,name='upnote'),
    path('delenote/<int:id>/',studentview.delenote,name='delenote'),


    path('addcomplaint',studentview.addcomplaint,name='addcomplaint'),
    path('complaintview',studentview.complaintview,name='complaintview'),
    path('upcomplaint/<int:id>/',studentview.upcomplaint,name='upcomplaint'),
    path('delecomplaint/<int:id>/',studentview.delecomplaint,name='delecomplaint'),


    path('addproject',studentview.addproject,name='addproject'),
    path('projectview',studentview.projectview,name='projectview'),
    path('upproject/<int:id>/',studentview.upproject,name='upproject'),
    path('deleproject/<int:id>/',studentview.deleproject,name='deleproject'),

    path('addassignment',studentview.addassignment,name='addassignment'),
    path('assignmentview',studentview.assignmentview,name='assignmentview'),
    path('upassignment/<int:id>/',studentview.upassignment,name='upassignment'),
    path('deleassignment/<int:id>/',studentview.deleassignment,name='deleassignment'),

    path('addseminar',studentview.addseminar,name='addseminar'),
    path('seminarview',studentview.seminarview,name='seminarview'),
    path('upseminar/<int:id>/',studentview.upseminar,name='upseminar'),
    path('deleseminar/<int:id>/',studentview.deleseminar,name='deleseminar'),


    path('addhw',studentview.addhw,name='addhw'),
    path('hwview',studentview.hwview,name='hwview'),
    path('uphw/<int:id>/',studentview.uphw,name='uphw'),
    path('delehw/<int:id>/',studentview.delehw,name='delehw'),

    path('appointment_admin',adminview.appointment_admin,name='appointment_admin'),
    path('appointment_view',teacherview.appointment_view,name='appointment_view'),
    path('join_community/<int:id>/',teacherview.join_community,name='join_community'),
    path('approve_appointment/<int:id>/',adminview.approve_appointment,name='approve_appointment'),
    path('reject_appointment/<int:id>/',adminview.reject_appointment,name='reject_appointment'),



    path('pexamtableview',parentview.pexamtableview,name='pexamtableview'),
    path('ptimetableview',parentview.ptimetableview,name='ptimetableview'),
    path('pmarkview',parentview.pmarkview,name='pmarkview'),
    path('pexamresultview',parentview.pexamresultview,name='pexamresultview'),
    path('pparentsmeetingview',parentview.pparentsmeetingview,name='pparentsmeetingview'),

    path('scommunitygroupview',studentview.scommunitygroupview,name='scommunitygroupview'),
    path('appointment_teacher',teacherview.appointment_teacher,name='appointment_teacher'),
    # path('studentappointments',teacherview.studentappointments,name='studentappointments'),
    path('sappointment_view',studentview.sappointment_view,name='sappointment_view'),
    path('sjoin_community/<int:id>/',studentview.sjoin_community,name='sjoin_community'),
    path('tapprove_appointment/<int:id>/',teacherview.tapprove_appointment,name='tapprove_appointment'),
    path('treject_appointment/<int:id>/',teacherview.treject_appointment,name='treject_appointment'),


    path('pcommunitygroupview',parentview.pcommunitygroupview,name='pcommunitygroupview'),
    path('pjoin_community/<int:id>/',parentview.pjoin_community, name='pjoin_community'),
    path('pappointment_view',parentview.pappointment_view,name='pappointment_view'),
    path('appointment_parent',teacherview.appointment_parent,name='appointment_parent'),
    path('papprove_appointment/<int:id>/',teacherview.papprove_appointment,name='papprove_appointment'),
    path('preject_appointment/<int:id>/',teacherview.preject_appointment,name='preject_appointment'),



    path('pnotificationview',parentview.pnotificationview,name='pnotificationview'),
    path('payment_details',adminview.payment_details,name='payment_details'),
    path('pay_bill/<int:id>/',parentview.pay_bill,name='pay_bill'),
    path('pay_in_direct/<int:id>/',parentview.pay_in_direct,name='pay_in_direct'),
    path('pay_history_view',parentview.pay_history_view,name='pay_history_view'),
    path('tpay_history_view',teacherview.tpay_history_view,name='tpay_history_view'),

    path('snotificationview',studentview.snotificationview,name='snotificationview'),
    # path('payment_details',studentview.payment_details,name='payment_details'),
    path('spay_bill/<int:id>/',studentview.spay_bill,name='spay_bill'),
    path('spay_in_direct/<int:id>/',studentview.spay_in_direct,name='spay_in_direct'),
    path('spay_history_view', studentview.spay_history_view, name='spay_history_view'),
    path('apayment_history_view', adminview.apayment_history_view, name='apayment_history_view'),
    # path('addpay',parentview.addpay,name='addpay'),
    # path('pay_in_direct',parentview.pay_in_direct,name='pay_in_direct'),
    # path('addpayment',parentview.addpayment,name='addpayment'),
    # path('adddetails',parentview.adddetails,name='adddetails'),
    # path('viewdetails',parentview.viewdetails,name='viewdetails'),
    # path('onlinepayment',parentview.onlinepayment,name='onlinepayment'),
    # path('directpay',parentview.directpay,name='directpay'),

    # path('newpay',parentview.newpay,name='newpay'),

    path('paddcomplaint',parentview.paddcomplaint, name='paddcomplaint'),
    path('pcomplaintview',parentview.pcomplaintview, name='pcomplaintview'),
    path('pupcomplaint/<int:id>/',parentview.pupcomplaint, name='pupcomplaint'),
    path('pdelecomplaint/<int:id>/',parentview.pdelecomplaint, name='pdelecomplaint'),


    path('tpcomplaintview',teacherview.tpcomplaintview, name='tpcomplaintview'),
    path('addpreplay/<int:id>/',teacherview.addpreplay,name='addpreplay'),
    path('apcomplaintview',adminview.apcomplaintview, name='apcomplaintview'),

    path('tscomplaintview',teacherview.tscomplaintview, name='tscomplaintview'),
    path('addsreplay/<int:id>/',teacherview.addsreplay,name='addsreplay'),
    path('ascomplaintview',adminview.ascomplaintview, name='ascomplaintview'),


    path('addnotification',teacherview.addnotification,name='addnotification'),
    path('anotificationview',teacherview.anotificationview,name='anotificationview'),
    path('upnotification/<int:id>/',teacherview.upnotification,name='upnotification'),
    path('delenotification/<int:id>/',teacherview.delenotification,name='delenotification'),



    # path('addbill',adminview.addbill,name='addbill'),
    # path('viewbill',adminview.viewbill,name='viewbill'),

    path('addschat',studentview.addschat,name='addschat'),
    path('schatview',studentview.schatview,name='schatview'),

    path('addtschat',teacherview.addtschat,name='addtschat'),
    path('tschatview',teacherview.tschatview,name='tschatview'),

    path('addpchat',parentview.addpchat,name='addpchat'),
    path('pchatview',parentview.pchatview,name='pchatview'),

    path('addtpchat', teacherview.addtpchat, name='addtpchat'),
    path('tpchatview', teacherview.tpchatview, name='tpchatview'),


]