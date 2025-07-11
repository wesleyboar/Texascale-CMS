from django.urls import include, re_path

custom_urls = [
    # To support `taggit_autosuggest` (from `djangocms-blog`)
    re_path(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
]
