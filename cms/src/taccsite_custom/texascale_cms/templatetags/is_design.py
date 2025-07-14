import re
from django import template

register = template.Library()

YEAR_PATTERN = re.compile(r"/(\d{4})/")

@register.simple_tag(takes_context=True)
def is_design_year(context, year_comparison):
    """
    Custom Template Tag `is_design_year`

    Use: Check if current page URL contains year that matches given comparison.

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

    if not year_match:
        return False

    try:
        path_year = int(year_match)
        year_comparison_str = str(year_comparison)

        # Parse year_comparison parameter
        if year_comparison_str.endswith('+'):
            threshold_year = int(year_comparison_str[:-1])
            return path_year >= threshold_year
        elif year_comparison_str.endswith('-'):
            threshold_year = int(year_comparison_str[:-1])
            return path_year <= threshold_year
        else:
            threshold_year = int(year_comparison_str)
            return path_year == threshold_year

    except (ValueError, TypeError):
        return False

@register.simple_tag(takes_context=True)
def is_design_legacy(context, cutoff_year=2024):
    """
    Custom Template Tag `is_design_legacy`

    Use: Check if current page URL is from legacy design period (2018–2024).

    Load custom filter into template:
        {% load is_design %}

    Template inline usage:
        {# Check if page uses legacy design (default cutoff 2024) #}
        {# given path '.../2018/...' — '.../2024/...' #}
        {% if is_design_legacy %}
            {# condition evaluates to True #}
        {% endif %}

        {# Check with custom cutoff #}
        {# given path '.../2018/...' — '.../2023/...' #}
        {% if is_design_legacy:"2023" %}
            {# condition evaluates to True #}
        {% endif %}
    """
    return is_design_year(context, f"{cutoff_year}-")
