from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Try to fetch the user by username
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            try:
                # If username fails, try to fetch the user by email
                user = UserModel.objects.get(email=username)
            except UserModel.DoesNotExist:
                return None  # Return None if no user is found

        # Check the password
        if user.check_password(password):
            return user