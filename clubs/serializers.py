from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)
from .models import Club, GeneralClub, OptionalClub, SpecialCLub, GENERAL_CLUB, OPTIONAL_CLUB, SPECIAL_CLUB

from django.core.exceptions import ObjectDoesNotExist




class ClubListSerializer(ModelSerializer):
    detail = SerializerMethodField()
    class Meta:
        model = Club
        fields = [
            'id',
            'name',
            'description',
            'rule',
            'club_type',
            'detail',
            'updated',
            'created',
        ]

    def get_detail(self, obj):
        if obj.club_type == 1:
            try:
                return GeneralClubDetailSerializer(obj.general_club).data
            except ObjectDoesNotExist:
                GeneralClub.objects.get_or_create(club=obj)
                return GeneralClubDetailSerializer(obj.optional_club).data
        elif obj.club_type == 2:
            try:
                return OptionalClubDetailSerializer(obj.optional_club).data
            except ObjectDoesNotExist:
                OptionalClub.objects.get_or_create(club=obj)
                return OptionalClubDetailSerializer(obj.optional_club).data
        elif obj.club_type == 3:
            try:
                return SpecialClubDetailSerializer(obj.special_club).data
            except ObjectDoesNotExist:
                SpecialCLub.objects.get_or_create(club=obj)
                return SpecialCLubDetailSerializer(obj.optional_club).data
        return None
            


class GeneralClubDetailSerializer(ModelSerializer):
    class Meta:
        model = GeneralClub
        fields = '__all__'


class OptionalClubDetailSerializer(ModelSerializer):
    class Meta:
        model = OptionalClub
        fields = '__all__'


class SpecialClubDetailSerializer(ModelSerializer):
    class Meta:
        model = SpecialCLub
        fields = '__all__'


"""

class ThreadListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name="api:threads:detail_delete_update",
        read_only=True,
        lookup_field="uuid",
    )
    owner = SerializerMethodField()

    class Meta:
        model = Thread
        fields = ("url", "owner", "title", "content", "uuid")

    def get_owner(self, obj):
        return str(obj.owner.username)



class ThreadDetailSerializer(ModelSerializer):
    owner = SerializerMethodField()
    class Meta:
        model = Thread
        fields = ("id", "owner", "title", "content", "uuid", "created", "updated")
        read_only_fields = ("created", "updated")

    def get_owner(self, obj):
        return str(obj.owner.username)


from django.core.exceptions import ObjectDoesNotExist

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)
"""