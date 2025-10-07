import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import Department, Role, Staff, Shift, Roster
from datetime import date

class Command(BaseCommand):
    help = 'Import duty roster from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        roster_date = date(2025, 10, 1)  # Assuming the date from file name

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            for row in reader:
                if len(row) < 3:
                    continue
                unit = row[0].strip()
                consultant = row[1].strip()
                phone = row[2].strip()

                if not unit or not consultant:
                    continue

                # Create or get department
                department, created = Department.objects.get_or_create(
                    name=unit,
                    defaults={'description': f'Department for {unit}'}
                )

                # Create or get role (Consultant)
                role, created = Role.objects.get_or_create(
                    name='Consultant',
                    department=department,
                    defaults={'description': 'Consultant on call'}
                )

                # Create or get shift (On Call)
                shift, created = Shift.objects.get_or_create(
                    name='On Call',
                    shift_type='on_call',
                    department=department,
                    defaults={
                        'start_time': '00:00:00',
                        'end_time': '23:59:59'
                    }
                )

                # Handle multiple consultants separated by /
                consultants = [c.strip() for c in consultant.split('/') if c.strip()]
                phones = [p.strip() for p in phone.split('/') if p.strip()]

                for i, cons in enumerate(consultants):
                    # Create user if not exists
                    username = cons.lower().replace(' ', '_').replace('.', '')
                    user, created = User.objects.get_or_create(
                        username=username,
                        defaults={
                            'first_name': cons.split()[1] if len(cons.split()) > 1 else cons,
                            'last_name': cons.split()[0] if cons.split() else '',
                        }
                    )

                    # Create staff
                    staff, created = Staff.objects.get_or_create(
                        user=user,
                        defaults={
                            'department': department,
                            'role': role,
                            'phone': phones[i] if i < len(phones) else '',
                        }
                    )

                    # Create roster
                    Roster.objects.get_or_create(
                        staff=staff,
                        shift=shift,
                        date=roster_date,
                        defaults={'is_assigned': True}
                    )

        self.stdout.write(self.style.SUCCESS('Successfully imported roster data'))
