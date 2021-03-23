# {{ ansible_managed }}

import ldap
from django_auth_ldap.config import {{ (["LDAPSearch"] + netbox_ldap_imports) | join(", ") }}
{% if netbox_ldap_extra_imports is defined and netbox_ldap_extra_imports != "" %}
{{ netbox_ldap_extra_imports }}
{% endif %}

AUTH_LDAP_SERVER_URI = "{{ netbox_ldap_scheme }}://{{ netbox_ldap_host }}:{{ netbox_ldap_port }}"

{{ netbox_ldap_config }}
