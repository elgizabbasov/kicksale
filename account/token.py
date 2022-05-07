from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class UserAccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp) -> str:
        return (text_type(user.pk) + text_type(timestamp) + text_type(user.is_active))
    
account_activation_token = UserAccountActivationTokenGenerator()
