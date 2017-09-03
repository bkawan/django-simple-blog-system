from django import template
from django.db.models import Model
from django.template.defaultfilters import urlencode

from apps.social_share.endpoints import TWEET_TO_TWITTER, FACEBOOK_ENDPOINT, GOOGLE_PLUS_ENDPOINT

register = template.Library()


def compile_text(context, text):
    ctx = template.context.Context(context)
    return template.Template(text).render(ctx)


def _compose_tweet(text, url=None):
    TWITTER_MAX_NUMBER_OF_CHARACTERS = 140
    TWITTER_LINK_LENGTH = 23  # "A URL of any length will be altered to 23 characters, even if the link itself is less than 23 characters long.

    # Compute length of the tweet
    url_length = len(' ') + TWITTER_LINK_LENGTH if url else 0
    total_length = len(text) + url_length

    # Check that the text respects the max number of characters for a tweet
    if total_length > TWITTER_MAX_NUMBER_OF_CHARACTERS:
        text = text[:(TWITTER_MAX_NUMBER_OF_CHARACTERS - url_length - 1)] + "…"  # len("…") == 1

    return "{} - {}".format(text, url) if url else text


def _build_url(request, obj_or_url):
    if obj_or_url is not None:
        if isinstance(obj_or_url, Model):
            return request.build_absolute_uri(obj_or_url.get_absolute_url())
        else:
            return request.build_absolute_uri(obj_or_url)
    return ''


@register.simple_tag(takes_context=True)
def tweet_to_twitter_url(context, text, obj_or_url=None):
    text = compile_text(context, text)
    request = context['request']

    # url = _build_url(request, obj_or_url)
    url = obj_or_url
    tweet = _compose_tweet(text, url)
    context['tweet_url'] = TWEET_TO_TWITTER.format(urlencode(tweet))
    return context


@register.inclusion_tag('social_share/tags/tweet_to_twitter.html', takes_context=True)
def tweet_to_twitter(context, text, obj_or_url=None):
    context = tweet_to_twitter_url(context, text, obj_or_url)

    request = context['request']
    url = _build_url(request, obj_or_url)
    tweet = _compose_tweet(text, url)

    context['full_text'] = tweet
    return context


@register.simple_tag(takes_context=True)
def share_to_facebook_url(context, text=None, obj_or_url=None):
    request = context['request']
    url = _build_url(request, obj_or_url)
    context['facebook_url'] = FACEBOOK_ENDPOINT.format(urlencode(url), text)
    context['content_title'] = text
    context['content_url'] = url
    return context


@register.inclusion_tag('social_share/tags/share_to_facebook.html', takes_context=True)
def share_to_facebook(context, text=None, obj_or_url=None, link_text='Post to Facebook'):
    context = share_to_facebook_url(context, text, obj_or_url)
    context['link_text'] = link_text
    return context


@register.simple_tag(takes_context=True)
def share_to_google_plus_url(context, obj_or_url=None):
    request = context['request']
    url = _build_url(request, obj_or_url)
    context['google_plus_url'] = GOOGLE_PLUS_ENDPOINT.format(urlencode(url))
    context['content_url'] = obj_or_url
    return context


@register.inclusion_tag('social_share/tags/share_to_google_plus.html', takes_context=True)
def share_to_google_plus(context, obj_or_url=None, link_text='Post to Google+'):
    context = share_to_google_plus_url(context, obj_or_url)
    context['link_text'] = link_text
    return context
