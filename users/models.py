from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    hire_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.role.name}"

class Shift(models.Model):
    SHIFT_TYPES = [
        ('morning', 'Morning'),
        ('evening', 'Evening'),
        ('night', 'Night'),
        ('on_call', 'On Call'),
    ]
    name = models.CharField(max_length=100)
    shift_type = models.CharField(max_length=20, choices=SHIFT_TYPES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.shift_type})"

class Roster(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    date = models.DateField()
    is_assigned = models.BooleanField(default=True)

    class Meta:
        unique_together = ('staff', 'shift', 'date')

    def __str__(self):
        return f"{self.staff} - {self.shift} on {self.date}"

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('on_leave', 'On Leave'),
    ]
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    roster = models.OneToOneField(Roster, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='absent')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.staff} - {self.roster.date} - {self.status}"

class Notification(models.Model):
    TYPE_CHOICES = [
        ('shift_reminder', 'Shift Reminder'),
        ('absence_alert', 'Absence Alert'),
        ('shift_change', 'Shift Change'),
        ('leave_approval', 'Leave Approval'),
    ]
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.staff} - {self.notification_type} - {self.created_at}"
