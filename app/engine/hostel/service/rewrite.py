from hostel.models import Student


def rewrite_room():
    print('!!!!!!!!!!!!!!!!!!!!!!            !!!!!!!!!!!!!!!!!!!!!!!!!!')
    students = Student.objects.all()
    for student in students:
        new_room = int(student.room[:student.room.find('.')])
        student.room = new_room
        student.save()

