import re

from django import template

register = template.Library()

@register.filter
def has_url_with_match(path, pattern):
    """
    Custom Template Filter `has_url_with_match`

    Use: Render string that matches given pattern from current page URL.

    Load custom filter into template:
        {% load has_url_with %}

    Template inline usage:
        {# given path '.../2019/...' #}
        {% if path|has_url_with_match:"/20\d\d/" %}
            {# condition evaluates to False #}
        {% endif %}

        {# given path '.../2020/...' #}
        {% if path|has_url_with_match:"/20\d\d/" %}
            {# condition evaluates to True #}
        {% endif %}

        {# given path '.../2021/...' #}
        {% with year_slug=path|has_url_with_match:"/(20\d\d)/" %}
            <pre>{{ year_slug }}</pre> {# prints 2021 #}
        {% endwith %}

        {# given path '.../2020/...' #}
        {% with year_path=path|has_url_with_match:"/20\d\d/" %}
            <pre>{{ year_path }}</pre> {# prints complete url #}
        {% endwith %}
    """
    result = re.search(pattern, path)

    if result:
        try:
            match = result.group(1)
        except IndexError:
            match = result[0]
    else:
        match = False

    return match

@register.filter
def has_url_with_year(path, year_comparison):
    """
    Custom Template Filter `has_url_with_year`

    Use: Check if the current page URL is a page of a given year with comparison.

    Load custom filter into template:
        {% load has_url_with %}

    Template inline usage:
        {# Check for year 2025 or above #}
        {# given path '.../2025/...', '.../2026/...', '.../2027/...', etc. #}
        {% if path|has_url_with_year:"2025+" %}
            {# condition evaluates to True #}
        {% endif %}

        {# Check for year 2024 or below #}
        {# given path '.../2024/...', '.../2023/...', '.../2022/...', etc. #}
        {% if path|has_url_with_year:"2024-" %}
            {# condition evaluates to True #}
        {% endif %}

        {# Check for exact year #}
        {# given path '.../2025/...' #}
        {% if path|has_url_with_year:2025 %}
            {# condition evaluates to True #}
        {% endif %}
    """
    year_match = has_url_with_match(path, r"/(\d{4})/")
    has_match = False

    if year_match:
        try:
            path_year = int(year_match)
            
            # Parse year_comparison parameter
            if year_comparison.endswith('+'):
                threshold_year = int(year_comparison[:-1])
                has_match = path_year >= threshold_year
            elif year_comparison.endswith('-'):
                threshold_year = int(year_comparison[:-1])
                has_match = path_year <= threshold_year
            else:
                threshold_year = int(year_comparison)
                has_match = path_year == threshold_year
        except (ValueError, TypeError):
            has_match = False

    return has_match
