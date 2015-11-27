import json
from oauth2client.client import SignedJwtAssertionCredentials

from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

register = template.Library()

@register.inclusion_tag('otto_admin/analytics.html', takes_context=True)
def analytics(context, next = None):

    if not getattr(settings, 'OA_ANALYTICS_CREDENTIALS_JSON', None):
        raise ImproperlyConfigured('Analytics service account json path missing')

    if not getattr(settings, 'OA_ANALYTICS_VIEW_ID', None):
        raise ImproperlyConfigured('Analytics view id missing')

    # The scope for the OAuth2 request.
    SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'

    # The location of the key file with the key data.
    KEY_FILEPATH = settings.OA_ANALYTICS_CREDENTIALS_JSON

    # Load the key file's private data.
    with open(KEY_FILEPATH) as key_file:
        _key_data = json.load(key_file)

    # Construct a credentials objects from the key data and OAuth2 scope.
    _credentials = SignedJwtAssertionCredentials(
        _key_data['client_email'], _key_data['private_key'], SCOPE)

    return {
        'token': _credentials.get_access_token().access_token,
        'view_id': settings.OA_ANALYTICS_VIEW_ID
    }

@register.filter(name='otto_admin_conf')
def otto_admin_conf(name):

    defaults = {
        'OA_COPYRIGHT': '2015 otto.to.it',
        'OA_SUPPORT_EMAIL': 'mail@otto.to.it',
        'OA_POWERED_BY': 'Otto srl',
        'OA_POWERED_BY_URL': 'http://www.otto.to.it',
    }

    return getattr(settings, name, defaults.get(name))
