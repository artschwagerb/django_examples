from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache

import json

from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q


from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.
@never_cache
@login_required
#@permission_required('tickets.view_tickets',raise_exception=True)
def index(request):
	
	ticket_assigned_list = ticket_list.filter(~(Q(status__slug="solved") | Q(status__slug="closed"))).distinct().order_by('-date_updated')

	template = loader.get_template('ticket_dashboard_test.html')
	context = RequestContext(request, {
		'ticket_assigned_list': ticket_assigned_list,
	})
	return HttpResponse(template.render(context))


@never_cache
@login_required
#@permission_required('tickets.view_tickets',raise_exception=True)
def VIEW_NAME(request,pk):
	if request.method == 'GET':
		# GET Method

		if pk:
			# Check argument passed from URL
			computer_item = Computer.objects.get(pk=pk)

		template = loader.get_template('inventory_inspection/inspect_device.html')
		context = RequestContext(request, {
			"inspect_user": inspect_user,
		})
		return HttpResponse(template.render(context))
	elif request.method == 'POST':
		# POST Method
		try:
			
			if pk:
				# Check argument passed from URL
				# check for a computer
				computer_item = Computer.objects.get(pk=pk)

				# modify object
				computer_item.name = 'new_name'

				# save object
				computer_item.save()

		except Computer.DoesNotExist:
			# object did not exist
			computer_item = None

		# set the template
		template = loader.get_template('inventory_inspection/inspect_device.html')

		# add request context(variables for template)
		context = RequestContext(request, {
			'inspect_device': computer_item,
		})

		# return the Response of the rendered template with context.
		return HttpResponse(template.render(context))

	else:
		# other methods?
		pass