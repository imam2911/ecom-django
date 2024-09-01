from .models import Category


#This function is for show category items in the menubar

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)