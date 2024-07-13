
{
'name': "class room",
'summary': "Manament of students",
'description': """
managment of students
==============
Description related to students.
""",
'author': "Your name",
'website': "http://www.example.com",
'category': 'Uncategorized',
'version': '13.0.1',
'depends': ['base','mail','sale','account','product'],
'data': ['security/ir.model.access.csv',
         'view/student_view.xml',
         'reports/repots_view.xml',
         'reports/reports.xml'],
}