from rest_framework.permissions import BasePermission
from rest_framework.views import Request, View

from contents.models import Content
from students_courses.models import StudentCourse


class IsParticipantOrSuperuser(BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Content) -> bool:
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        else:
            try:
                StudentCourse.objects.get(
                    course_id=obj.course_id,
                    student_id=request.user.id
                )
                return True
            except:
                return False
