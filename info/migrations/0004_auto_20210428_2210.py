# Generated by Django 3.2 on 2021-04-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_attendance_attendanceclass_attendancetotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendanceclass',
            name='assign',
        ),
        migrations.AlterUniqueTogether(
            name='attendancetotal',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='attendancetotal',
            name='course',
        ),
        migrations.RemoveField(
            model_name='attendancetotal',
            name='student',
        ),
        migrations.AddField(
            model_name='class',
            name='courses',
            field=models.ManyToManyField(default=1, to='info.Course'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='name',
            field=models.CharField(choices=[('LAB 1', 'LAB 1'), ('LAB 2', 'LAB 2'), ('LAB 3', 'LAB 3'), ('MID SEM - I', 'MID SEM - I'), ('Project', 'Project'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='marksclass',
            name='name',
            field=models.CharField(choices=[('LAB 1', 'LAB 1'), ('LAB 2', 'LAB 2'), ('LAB 3', 'LAB 3'), ('MID SEM - I', 'MID SEM - I'), ('Project', 'Project'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='AttendanceClass',
        ),
        migrations.DeleteModel(
            name='AttendanceTotal',
        ),
    ]
