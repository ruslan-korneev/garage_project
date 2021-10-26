from django.http import response


def parse_metric_json(data):
    data = data['metrics']

    response = 'Pokemon Metrics<br><br>'
    for metric in data:
        for sample in metric.samples:
            response += f"{sample.name}: {sample.value}<br>"
    return response
