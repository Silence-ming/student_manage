from django.shortcuts import render,redirect,HttpResponse
import pymysql
import common.md5 as m

db=pymysql.connect('localhost','root','root','school',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
def teacher(request):
    cursor=db.cursor()
    cursor.execute('select teacher.id,teacher.name,teacher.sex,class.number from teacher left join class_teacher on teacher.id=teacherID left join class on class_teacher.classID=class.id ')
    result=cursor.fetchall()
    dir = {}
    for item in result:
        if not item['id'] in dir:
            dir[item['id']] = item
            dir[item['id']]['number'] = [item['number']]
        else:
            dir[item['id']]['number'].append(item['number'])
    arr = dir.values()
    return render(request,'teacher.html',{'data':arr})
def teacher_addPage(request):
    cursor = db.cursor()
    cursor.execute( 'select * from class')
    classes = cursor.fetchall()
    return render(request, 'teacher_addPage.html',{"classes":classes})
def teacher_add(request):
    cursor = db.cursor()
    name=request.POST.get('name')
    sex = request.POST.get('sex')
    class_ids=request.POST.getlist('class')
    cursor.execute('select * from teacher where name=%s',[name])
    data=cursor.fetchone()
    if not data:
        sql1="insert into teacher(name,sex) values (%s,%s)"
        cursor.execute(sql1,[name,sex])
        teacher_id=db.insert_id()
        arr = []
        for item in class_ids:
            arr.append((teacher_id, item))
        sql2='insert into class_teacher(teacherID,classID) values (%s,%s)'
        cursor.executemany(sql2,arr)
        db.commit()
        return redirect(teacher)
    else:
        return render(request,'error.html',{"data":"该老师已存在！","url":'/teacher_addPage.html/'})
def teacher_editPage(request,id):
    cursor=db.cursor()
    cursor.execute('select * from teacher where id='+id)
    data1=cursor.fetchall()
    cursor.execute('select * from class ')
    classes = cursor.fetchall()
    return render(request, 'teacher_editPage.html', {"teacher":data1[0],'classes':classes})
def teacher_edit(request):
    cursor = db.cursor()
    teacher_id=request.POST.get('id')
    name = request.POST.get('name')
    sex = request.POST.get('sex')
    class_ids=request.POST.getlist('cla')
    arr=[]
    for item in class_ids:
        arr.append((item,teacher_id))
    cursor.executemany('update class_teacher set classID=%s where teacherID=%s',arr)
    sql='update teacher set name=%s,sex=%s where id=%s'
    cursor.execute(sql,[name,sex,teacher_id])
    db.commit()
    return redirect(teacher)
def teacher_dels(request,id):
    cursor=db.cursor()
    sql1='delete from teacher where id='+id
    sql2='delete from class_teacher where teacherID=' + id
    try:
        cursor.execute(sql1)
        cursor.execute(sql2)
    except:
        db.callback()
    else:
        db.commit()
    return redirect(teacher)

def classes(request):
    cursor=db.cursor()
    cursor.execute('select class.id,class.number,teacher.name from class left join class_teacher on class.id=classID left join teacher on teacherID=teacher.id ')
    result=cursor.fetchall()
    dir = {}
    for item in result:
        if not item['id'] in dir:
            dir[item['id']] = item
            dir[item['id']]['name'] =[item['name']]
        else:
            dir[item['id']]['name'].append(item['name'])
    arr = dir.values()
    return render(request,'class.html',{'data':arr})
def class_addPage(request):
    return render(request, 'class_addPage.html')
def class_add(request):
    cursor = db.cursor()
    classeName=request.POST.get('class')
    cursor.execute('select * from class where number=%s',[classeName])
    data=cursor.fetchone()
    if not data:
        cursor.execute('insert into class (number) values(%s)',[classeName])
        db.commit()
        return redirect(classes)
    else:
        return render(request, 'error.html', {"data": "班级已存在！",'url':'/class_addPage.html/'})
def class_editPage(request,id):
    cursor=db.cursor()
    cursor.execute('select * from class where id='+id)
    data1=cursor.fetchall()
    cursor.execute('select * from teacher')
    teachers=cursor.fetchall()
    return render(request, 'class_editPage.html', {"classes":data1[0],'teachers':teachers})
def class_edit(request):
    cursor = db.cursor()
    class_id=request.POST.get('id')
    teacher_ids=request.POST.getlist('teacher')
    arr = []
    for item in teacher_ids:
        arr.append((item, class_id))

    cursor.execute('select * from class_teacher where classID=%s',[class_id])
    data=cursor.fetchall()
    if data:
        for item in data:
            if item['teacherID']:
                cursor.executemany('update class_teacher set teacherID=%s where classID=%s', arr)
    else:
        cursor.executemany('insert into class_teacher (teacherID,classID) values (%s,%s)', arr)
    db.commit()
    return redirect(classes)
def class_dels(request,id):
    cursor=db.cursor()
    sql1='delete from class where id='+id
    sql2 = 'delete from class_teacher where classID=' + id
    try:
        cursor.execute(sql1)
        cursor.execute(sql2)
    except:
        db.callback()
    else:
        db.commit()
    return redirect(classes)

def student(request):
    cursor=db.cursor()
    cursor.execute('select student.id,student.s_name,student.sex,class.number from student left join class on student.classID=class.id ')
    datas=cursor.fetchall()
    return render(request,'student.html',{'data':datas})
def student_addPage(request):
    cursor = db.cursor()
    cursor.execute( 'select * from class')
    classes = cursor.fetchall()
    return render(request, 'student_addPage.html',{"classes":classes})
def student_add(request):
    cursor = db.cursor()
    name=request.POST.get('name')
    sex = request.POST.get('sex')
    class_id=request.POST.get('class')
    cursor.execute('select * from student where s_name=%s',[name])
    data=cursor.fetchone()
    if not data:
        cursor.execute('insert into student (s_name,sex,classID) values (%s,%s,%s)',[name,sex,class_id])
        db.commit()
        return redirect(student)
    else:
        return render(request, 'error.html', {"data": "该学生已存在！", 'url': '/student_addPage.html/'})
def student_editPage(request,id):
    cursor=db.cursor()
    cursor.execute('select * from student where id='+id)
    data1=cursor.fetchall()
    cursor.execute('select * from class ')
    classes = cursor.fetchall()
    return render(request, 'student_editPage.html', {"student":data1[0],'classes':classes})
def student_edit(request):
    cursor = db.cursor()
    student_id=request.POST.get('id')
    name = request.POST.get('name')
    sex = request.POST.get('sex')
    class_id = request.POST.get('cla')
    cursor.execute('update student set classID=%s,s_name=%s,sex=%s where id=%s',[class_id,name,sex,student_id])
    db.commit()
    return redirect(student)
def student_dels(request,id):
    cursor=db.cursor()
    sql1='delete from student where id='+id
    cursor.execute(sql1)
    db.commit()
    return redirect(student)
def loginPage(request):
    if request.session.get('user'):
        userName=request.session.get('user')
        return render(request,'school.html',{'user':userName})
    else:
        return render(request,'login.html')
def login(request):
    name = request.POST.get('user')
    password = request.POST.get('pass')
    save=request.POST.get('save')
    cursor = db.cursor()
    cursor.execute('select * from users where username= %s and password= %s',[name,m.md5(password)])
    data=cursor.fetchall()
    if data:
        request.session['user']= name
        if save!='week':
            request.session.set_expiry(0) #浏览器关闭的时间
            cursor=db.cursor()
            cursor.execute('select img_url from users where username=%s',[name])
            img_url=cursor.fetchone()['img_url']
        return render(request, 'school.html', {'user': name,'img_url':img_url},)
    else:
        return redirect(loginPage)
def exits(request):
    del request.session['user']
    return redirect(loginPage)
def keyPage(request):
    return render(request,'keyPage.html')
def key(request):
    forward_pass=request.POST.get('forward_pass')
    new_pass = request.POST.get('new_pass')
    new_pass1 = request.POST.get('new_pass1')
    cursor = db.cursor()
    cursor.execute('select * from users where password=%s',[m.md5(forward_pass)])
    result=cursor.fetchone()
    if result and new_pass == new_pass1:
        id=result['id']
        cursor.execute('update users set password=%s where id= %s',[m.md5(new_pass),id])
        return HttpResponse('密码修改成功！')
    else:
        return HttpResponse('输入内容有误，请从新修改！')
# def registerPage(request):
#     return render(request,'register.html')
# def register(request):
#     name=request.POST.get('name')
#     password1 = request.POST.get('password1')
#     password2 = request.POST.get('password2')
#     cursor = db.cursor()
#     try:
#         cursor.execute('select * from users where username='+name)
#         cursor.fetchall()
#     except:
#         if password1 == password2 and name and password1:
#             sql='insert into users (username,password) values (%s,%s)'
#             cursor.execute(sql,[name,m.md5(password1)])
#             db.commit()
#             return redirect(loginPage)
#         else:
#             return redirect(registerPage)
#     else:
#         return redirect(registerPage)


