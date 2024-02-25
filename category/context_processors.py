from .models import Category

# custom context processor
def sub_links(request):
    links = Category.objects.all()

    return dict(links=links)



