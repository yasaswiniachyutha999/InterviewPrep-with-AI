from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Optional editable display name separate from auth user's first/last
    full_name = models.CharField(max_length=255, blank=True, null=True)
    # Image and resume uploads
    photo = models.ImageField(upload_to='profiles/photos/', blank=True, null=True)
    resume_file = models.FileField(upload_to='profiles/resumes/', blank=True, null=True)
    # Extracted text from uploaded resume
    extracted_text = models.TextField(blank=True, null=True)
    # Legacy fields kept for backward compatibility
    profile_picture_url = models.URLField(blank=True, null=True)
    resume_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)  # create profile
    else:
        # Only update if profile exists
        if hasattr(instance, "userprofile"):
            instance.userprofile.save()
