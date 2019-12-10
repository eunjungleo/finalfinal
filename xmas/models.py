from django.db import models

#class comment for both GuestBook and HostPost
class Comment(models.Model):
#    post = models.ForeignKey('GuestBook','HostPost', on_delete=models.PROTECT)
    name = models.CharField(max_length=50, null=True)
    words = models.TextField(max_length=300)

#Guestposts from guests
class GuestBook(models.Model):
    name = models.CharField(max_length=100, null=False)
    words = models.TextField(max_length=200, null=True)
    rsvp = models.BooleanField(default=True) #guests' rsvp - false:absent, true:present
#    comment = models.ForeignKey(related_name='Comment')

    def __str__(self):
        return self.name

#pick which host: Rina or Eunjung ?
class HostNameChoice(models.Model):
    pass

#hostpost from hosts
class HostPost(models.Model):
#    name = models.ForeignKey('HostNameChoice')
    title = models.CharField(max_length=200, null=True)
    words = models.TextField(null=True)
    image = models.ImageField(null=True, upload_to='images')
#    comment = models.ForeignKey(related_name='Comment')

    def __str__(self):
        return self.title
    