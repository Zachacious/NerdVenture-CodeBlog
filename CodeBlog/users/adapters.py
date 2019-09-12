from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    
    # handle all validations on the frontend --
    def clean_password(self, password):
        return password

    # def save_user(self, request, user, form, commit=False):
    #     user = super().save_user(request, user, form, commit)
    #     data = form.cleaned_data
    #     user.first_name = data.get('first_name')
    #     user.last_name = data.get('last_name')
    #     user.save()
    #     return user