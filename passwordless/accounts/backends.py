from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import Students
import logging

logger = logging.getLogger('accounts')

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        logger.debug("Attempting to authenticate user with email: %s", email)
        print(f"Authenticating user with email: {email}")

        try:
            user = Students.objects.get(Email=email)
            logger.debug("User found: %s", user)
            print(f"User found: {user.Email}")
            if user.Password == password:
                logger.debug("Password matched for user: %s", user)
                print("Password matched")
                return user
            else:
                logger.debug("Password did not match for user: %s", user)
                print("Password did not match")
        except Students.DoesNotExist:
            logger.debug("User with email %s does not exist", email)
            print("User does not exist")
            return None

    def get_user(self, user_id):
        try:
            return Students.objects.get(pk=user_id)
        except Students.DoesNotExist:
            return None
