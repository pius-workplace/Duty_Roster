from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import Department, Role, Staff

class Command(BaseCommand):
    help = 'Create an admin user'

    def handle(self, *args, **options):
        # Create admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'first_name': 'Admin',
                'last_name': 'User',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(f'Created admin user: {admin_user.username}')
        else:
            self.stdout.write(f'Admin user already exists: {admin_user.username}')

        # Create admin department and role
        admin_dept, created = Department.objects.get_or_create(
            name='Administration',
            defaults={'description': 'Administrative department'}
        )

        admin_role, created = Role.objects.get_or_create(
            name='Admin',
            department=admin_dept,
            defaults={'description': 'System administrator'}
        )

        # Create or update staff record for admin
        staff, created = Staff.objects.get_or_create(
            user=admin_user,
            defaults={
                'department': admin_dept,
                'role': admin_role,
                'phone': '',
            }
        )
        if not created:
            staff.role = admin_role
            staff.save()
            self.stdout.write('Updated admin staff role')

        self.stdout.write(self.style.SUCCESS('Admin user setup complete'))
