from django import template

# Create an instance of the template.Library object
register = template.Library()

# Define a custom filter called 'split_by_comma'
@register.filter
def split_by_comma(value):
    """
    Splits a string by commas and returns a list of trimmed tags.
    If the string is empty or None, returns an empty list.
    """
    if value:
        # Split the string by commas and remove any leading/trailing spaces from each tag
        return [tag.strip() for tag in value.split(',')]
    return []
