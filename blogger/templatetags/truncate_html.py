from django import template
from bs4 import BeautifulSoup

register = template.Library()

@register.filter
def truncate_html(content, length=300):
    if not content:
        return ""
    
    # Convert HTML to text using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()
    
    if len(text) <= length:
        return content
    
    truncated_text = text[:length] + '...'
    
    # Use BeautifulSoup to create a new HTML string from the truncated text
    truncated_soup = BeautifulSoup(truncated_text, 'html.parser')
    
    return str(truncated_soup)
