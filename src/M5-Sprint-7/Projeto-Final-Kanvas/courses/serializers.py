from rest_framework import serializers

from courses.models import Course
from accounts.models import Account
from students_courses.models import StudentCourse
from students_courses.serializers import StudentCourseSerializer
from contents.serializers import ContentSerializer


COURSE_STATUS = ("not started", "in progress", "finished")


class CourseSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)
    students_courses = StudentCourseSerializer(many=True, read_only=True)
    status = serializers.ChoiceField(choices=COURSE_STATUS, required=False)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "students_courses",
            "contents"
        ]


class CourseStudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]

    def update(self, instance: Course, validated_data: dict) -> Course:
        emails_received = []

        for student in validated_data["students_courses"]:
            email = student["student"]["email"]
            try:
                student = Account.objects.get(email=email)
                try:
                    StudentCourse.objects.get(course=instance, student=student)
                except:
                    instance.students.add(student)
                    instance.save()
                return instance
            except Account.DoesNotExist:
                emails_received.append(email)
            if len(emails_received) > 0:
                email_string = ",".join(emails_received)
                error = f"No active accounts was found: {email_string}."
                raise serializers.ValidationError({"detail": error})
