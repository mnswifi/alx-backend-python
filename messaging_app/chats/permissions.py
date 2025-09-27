from rest_framework import permissions


class IsParticipantOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation
    to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        if hasattr(obj, 'participants'):
            return user in obj.participants.all()
        if hasattr(obj, 'conversation'):
            return user in obj.conversation.participants.all()
        return False
