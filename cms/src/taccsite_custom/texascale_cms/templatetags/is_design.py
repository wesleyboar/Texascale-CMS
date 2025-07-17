import re
from django import template
from django.conf import settings

register = template.Library()

YEAR_PATTERN = re.compile(r"/(\d{4})/")
LAST_LEGACY_YEAR = 2024

@register.simple_tag(takes_context=True)
def is_design_year(context, year_comparison):
    """
    Custom Template Tag `is_design_year`

    Checks if current page is from design of a year that matches given year(s).

    Load custom filter into template:
        {% load is_design %}

    Template inline usage:
        {# Check for year 2025 or above #}
        {# given path '.../2025/...', '.../2026/...', '.../2027/...', etc. #}
        {% if is_design_year:"2025+" %}
            {# condition evaluates to True #}
        {% endif %}

        {# Check for year 2024 or below #}
        {# given path '.../2024/...', '.../2023/...', '.../2022/...', etc. #}
        {% if is_design_year:"2024-" %}
            {# condition evaluates to True #}
        {% endif %}

        {# Check for exact year #}
        {# given path '.../2025/...' #}
        {% if is_design_year:2025 %}
            {# condition evaluates to True #}
        {% endif %}
    """
    request = context.get('request')
    if not request or not year_comparison:
        return False

    year_search = YEAR_PATTERN.search(request.path)
    year_match = year_search.group(1) if year_search else False

    published_year = getattr(settings, 'TEXASCALE_PUBLISHED_YEAR', LAST_LEGACY_YEAR)
    page_year = int(year_match) if year_match else published_year

    try:
        year_comparison_str = str(year_comparison)

        if year_comparison_str.endswith('+'):
            threshold_year = int(year_comparison_str[:-1])
            return page_year >= threshold_year
        elif year_comparison_str.endswith('-'):
            threshold_year = int(year_comparison_str[:-1])
            return page_year <= threshold_year
        else:
            threshold_year = int(year_comparison_str)
            return page_year == threshold_year

    except (ValueError, TypeError):
        return False

@register.simple_tag(takes_context=True)
def is_design_legacy(context):
    """
    Custom Template Tag `is_design_legacy`

    Checks if current page should use legacy design, based on URL and settings

    Load custom filter into template:
        {% load is_design %}

    Template inline usage:
        {% if is_design_legacy %}
            {# ... #}
        {% endif %}

    Logic:
        - Returns True if TACC_CORE_STYLES_VERSION == 0 (force legacy)
        - Returns True if URL year is 2024 or earlier
        - Returns False otherwise (modern design)
    """
    core_styles_version = getattr(settings, 'TACC_CORE_STYLES_VERSION', 1)

    if core_styles_version == 0:
        return True
    if core_styles_version >= 1:
        return is_design_year(context, f"{LAST_LEGACY_YEAR}-")

    return False
