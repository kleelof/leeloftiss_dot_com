from .models import Projects


def _get_project_by_id(id):
    projects = Projects.objects.filter(id=id)
    return projects[0] if projects else None


def _get_project_by_slug(slug):
    projects = Projects.objects.filter(slug=slug)
    return projects[0] if projects else None