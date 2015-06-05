from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MODEL_NAME(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(null=True,blank=True)
	slug = models.SlugField(max_length=50)
	enabled = models.BooleanField(default=True)
	another_char = models.CharField(max_length=50,null=True,blank=True)
	notifications = models.ManyToManyField(User,related_name='status_notifications',null=True,blank=True)
	author = models.ForeignKey(User,related_name='author')
	date_added = models.DateTimeField('date_added',auto_now_add=True, editable=False)
	date_updated = models.DateTimeField('date_updated',auto_now_add=True, auto_now=True, editable=False)

	def __unicode__(self):
		return u'%s' % (self.name)

	class Meta:
		verbose_name_plural = "statuses"
		ordering = ['name']
		permissions = (
						("search_model", "Can search model"),
						("open_tickets", "Can open tickets"),
						("close_tickets", "Can close tickets"),
						("modify_tickets", "Can modify tickets"),
						("search_tickets", "Can search tickets"),
						("no_auto_watcher", "Create tickets without Watchers"),
						("report_tickets", "Can report tickets"),
						("review_tickets", "Can review tickets"),
						("change_user", "Can change user on existing tickets"),
					)