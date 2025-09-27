
from rest_framework import permissions


class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allows access only to authenticated users who are participants
    in the conversation.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user
        # For Conversation objects
        if hasattr(obj, 'participants'):
            return user in obj.participants.all()
        # For Message objects
        if hasattr(obj, 'conversation'):
            return user in obj.conversation.participants.all()
        return False
