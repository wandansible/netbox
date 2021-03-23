# {{ ansible_managed }}

ALLOWED_HOSTS = {{ netbox_allowed_hosts | to_nice_json }}

DATABASE = {
    "NAME": "{{ netbox_database }}",
    "USER": "{{ netbox_database_user }}",
{% if netbox_database_password is defined and netbox_database_password != "" %}
    "PASSWORD": {{ netbox_database_password | string | to_json }},
    "HOST": "{{ netbox_database_host }}",
{% else %}
    "HOST": "{{ netbox_database_socket }}",
{% endif %}
    "PORT": "{{ netbox_database_port }}",
    "CONN_MAX_AGE": {{ netbox_database_conn_max_age }}
}

REDIS = {
    "tasks": {
        "HOST": "{{ netbox_redis_host }}",
        "PORT": {{ netbox_redis_port }},
        "PASSWORD": {{ netbox_redis_password | string | to_json }},
        "DATABASE": {{ netbox_redis_database }},
        "DEFAULT_TIMEOUT": {{ netbox_redis_default_timeout }},
        "SSL": {{ netbox_redis_ssl }}
    },
    "caching": {
        "HOST": "{{ netbox_redis_cache_host }}",
        "PORT": {{ netbox_redis_cache_port }},
        "PASSWORD": {{ netbox_redis_cache_password | string | to_json }},
        "DATABASE": {{ netbox_redis_cache_database }},
        "DEFAULT_TIMEOUT": {{ netbox_redis_cache_default_timeout }},
        "SSL": {{ netbox_redis_cache_ssl }}
    }
}

SECRET_KEY = {{ netbox_secret_key | string | to_json }}

MEDIA_ROOT = "{{ netbox_media_root }}"
REPORTS_ROOT = "{{ netbox_reports_root }}"
SCRIPTS_ROOT = "{{ netbox_scripts_root }}"

{% for key, value in netbox_config | dictsort %}
{% if value in [True, False] %}
{{ key }} = {{ "True" if value else "False" }}
{% else %}
{{ key }} = {{ value | to_nice_json | regex_replace('true,?\n', 'True,\n') | regex_replace('false,?\n', 'False,\n') }}
{% endif %}
{% endfor %}
