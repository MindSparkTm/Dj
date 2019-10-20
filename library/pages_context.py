from user.models import UserStatus

def show_active_users(context):
    user_list = UserStatus.objects.select_related('current_user').filter(status__gte=1)
    return {'user_list': user_list}