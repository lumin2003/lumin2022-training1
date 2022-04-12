from import_export import resources
from .models import UserInfo

class UserInfoResource(resources.ModelResource):
    class Meta:
        model = UserInfo
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        fields = ('username', 'password', 'address', 'create_date','email')