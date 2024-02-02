from mainApp.models import Option


def options(request):
    menu_options = Option.objects.all().get_descendants(include_self=True)
    return {'options': menu_options}
