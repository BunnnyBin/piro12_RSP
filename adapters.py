from allauth.account.utils import user_username, user_email, user_field
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.utils import valid_email_or_none




class SocialAccountAdapter(DefaultSocialAccountAdapter):
    # def save_user(self, request, sociallogin, form=None):
#     #
#     #     user = super(SocialAccountAdapter, self).save_user(request, sociallogin, form)
#     #
#     #     social_app_name = sociallogin.account.provider.upper()
#     #     # extra_data = user.extra_data()
#     #
#     #     if social_app_name == "GOOGLE":
#     #         User.objects.get_or_create_google_user(user_pk=user.pk, extra_data = extra_data)  #extra_data
#     #
#     #     elif social_app_name == "KAKAO":
#     #         User.objects.get_or_create_kakao_user(user_pk=user.pk, extra_data = extra_data)
    def populate_user(self,
                      request,
                      sociallogin,
                      data):
        social_app_name = sociallogin.account.provider.upper()
        if social_app_name == "GOOGLE":
            username = data.get('last_name') + data.get('first_name')

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        name = data.get('name')
        user = sociallogin.user
        user_username(user, username or '')
        user_email(user, valid_email_or_none(email) or '')
        name_parts = (name or '').partition(' ')
        user_field(user, 'first_name', first_name or name_parts[0])
        user_field(user, 'last_name', last_name or name_parts[2])
        return user