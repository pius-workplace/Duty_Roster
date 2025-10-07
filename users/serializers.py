from rest_framework import serializers
from .models import Department, Role, Staff, Shift, Roster, Attendance, Notification
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Role
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    department = DepartmentSerializer()
    role = RoleSerializer()

    class Meta:
        model = Staff
        fields = '__all__'

class ShiftSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Shift
        fields = '__all__'

class RosterSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    shift = ShiftSerializer()

    class Meta:
        model = Roster
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    roster = RosterSerializer()

    class Meta:
        model = Attendance
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()

    class Meta:
        model = Notification
        fields = '__all__'
