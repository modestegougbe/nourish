from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required

from nourish.views import GroupDetailView, GroupUpdateView, EventDetailView, EventGroupView, EventUpdateView, EventListView, GroupListView, SiteInviteRecipientView, EventGroupUpdateView
from nourish.views.canvas import CanvasTemplateView
from nourish.models import Event, Group

urlpatterns = patterns('',
    url('^logged-in/$', 'nourish.views.homepage_chooser', name='homepage-chooser'),
    url('^register/event/$', 'nourish.views.register_event', name='register-event' ),
    url('^home/$', 'nourish.views.homepage', name='homepage'),
    url('^$',      'nourish.views.rootpage', name='rootpage'),

    url(r'^i/$', SiteInviteRecipientView.as_view()),
    url(r'^events/$', EventListView.as_view(), name='event-list'),

    url(r'^e/(?P<pk>\d+)-(?P<slug>[^\/]*)/$', EventDetailView.as_view(), name='event-detail'),
    url(r'^e/(?P<pk>\d+)(-[^\/]*)?/edit/$', login_required(EventUpdateView.as_view())),

    url(r'^e/(?P<event_id>\d+)(-[^\/]*)?/register/guest/$', 
        'nourish.views.register_event_guest'),
    url(r'^e/(?P<event_id>\d+)(-[^\/]*)?/register/host/$', 
        'nourish.views.register_event_host'),
    url(r'^eg/(?P<pk>\d+)-(?P<slug>[^/]+)/$', 
        EventGroupView.as_view(), name='event-group-detail'),
    url(r'^eg/(?P<pk>\d+)(-[^\/]*)?/edit/$', 
        EventGroupUpdateView.as_view(), name='event-group-edit'),
    url(r'^eg/(?P<pk>\d+)(-[^\/]*)?/meals/$', 
        'nourish.views.event_guest_meals'),
    url(r'^eg/(?P<pk>\d+)(-[^\/]*)?/invite/(?P<host_eg_id>\d+)/$', 
        'nourish.views.event_guest_invite'),
    url(r'^eg/(?P<pk>\d+)(-[^\/]*)?/invites/$', 
        'nourish.views.event_host_invites'),

    url(r'^groups/$', GroupListView.as_view(), name='group-list'),
    url(r'^g/(?P<pk>\d+)-(?P<slug>[^\/]*)/$', GroupDetailView.as_view(), name='group-detail'),
    url(r'^g/(?P<pk>\d+)(-[^\/]*)?/edit/$', login_required(GroupUpdateView.as_view())),

    url(r'^fb_newgroup_options/$', CanvasTemplateView.as_view(template_name="nourish/fb_newgroup_options_page.html"), name='fb-newgroup-options'),
)
