from blog_api import models
from blog_api import serializers

def fetch_stories_by_action(storyid):
    if storyid:
        story = models.Story.objects.filter(verified=True).filter(id=storyid)
        comment = models.Comment.objects.filter(story_on=storyid)
        comment_serializer = serializers.CommentItemSerializer(comment, many=True)
        story_serializer = serializers.StoryFeedItemSerializer(story, many=True)
        response = {
            'story':story_serializer.data,
            'comments': comment_serializer.data
        }
    else:
        story = models.Story.objects.filter(verified=True)
        story_serializer = serializers.StoryFeedItemSerializer(story, many=True)
        response = {
            'story':story_serializer.data
        }
    return response
