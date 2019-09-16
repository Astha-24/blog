from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from blog_api import serializers
from blog_api import models
from blog_api import permissions
from blog_api import utils
import json
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class StoryFeedViewSet(viewsets.ModelViewSet):
    """Handles creating , reading and updating story """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.StoryFeedItemSerializer
    queryset = models.Story.objects.all()
    def list(self, request):
        """Return all verified and unverified story of logged in User"""
        queryset = models.Story.objects.filter(author=request.user.id)
        serializer = serializers.StoryFeedItemSerializer(queryset, many=True)
        return Response({'stories': serializer.data})

    permission_classes = (permissions.UpdateOwnStory,IsAuthenticated)

    def perform_create(self,serializer):
        """"Sets the user profile to the logged in user"""
        serializer.save(author=self.request.user)

class ViewAllVerifiedStory(APIView):
    serializer_class = serializers.CommentItemSerializer
    def get(self,request,format=None):
        """Returns all or one verified stories"""
        storyid = self.request.query_params.get('storyid')
        respose_payload = utils.fetch_stories_by_action(storyid)
        return Response(respose_payload)
    def post(self, request):
        """Create a comment for a story"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(comment_by=request.user)
            return Response({
                'message':'Comment posted successfully'
            })
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
