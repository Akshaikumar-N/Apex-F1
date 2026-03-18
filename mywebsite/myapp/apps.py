from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import sys
        if 'runserver' in sys.argv:
            from django.contrib.auth.models import User
            try:
                if not User.objects.filter(username='akshaikumar').exists():
                    User.objects.create_superuser('akshaikumar', 'admin@example.com', "I'M BATMAN")
                    print("Successfully created superuser 'akshaikumar'")
                else:
                    # Update password if user exists
                    user = User.objects.get(username='akshaikumar')
                    user.set_password("I'M BATMAN")
                    user.is_superuser = True
                    user.is_staff = True
                    user.save()
                    print("Successfully updated password to 'I'M BATMAN' for user 'akshaikumar'")
                    
            except Exception as e:
                pass
