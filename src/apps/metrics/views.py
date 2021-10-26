from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, REGISTRY
from django.http import HttpResponse


def metric_view(request):
    """Exports /metrics as a Django view.

    You can use django_prometheus.urls to map /metrics to this view.
    """
    registry = REGISTRY
    metrics_page = generate_latest(registry)
    return HttpResponse(
        metrics_page, content_type=CONTENT_TYPE_LATEST
    )
