# {{ ansible_managed }}

bind = "{{ netbox_listen }}"
workers = {{ netbox_wsgi_workers }}
threads = {{ netbox_wsgi_threads }}
timeout = {{ netbox_wsgi_timeout }}
max_requests = {{ netbox_wsgi_max_requests }}
max_requests_jitter = {{ netbox_wsgi_max_requests_jitter }}
{% for key, value in netbox_wsgi_extra | dictsort %}
{% if value in [True, False] %}
{{ key }} = {{ "True" if value else "False" }}
{% else %}
{{ key }} = {{ value | to_nice_json | regex_replace('true,?\n', 'True,\n') | regex_replace('false,?\n', 'False,\n') }}
{% endif %}
{% endfor %}
