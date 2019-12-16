from mdrm.mdrm import MDRMResource
from mdrm.resources.client_account.models import Profile


class ClientAccountResource(MDRMResource):

    @classmethod
    def get_profile(self, user_id):
        profiles = Profile.object.filter(id=user_id)
        return profiles[0] if profiles else None

    @classmethod
    def set_profile(self, user_data):
        pass
