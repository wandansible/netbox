Ansible role: Netbox
====================

Install and configure NetBox and create a PostgreSQL database
for NetBox. This role will also upgrade NetBox when a new
version is selected. It is recommended to stop the
netbox.service, netbox-rq.service and netbox-
housekeeping.timer systemd units, and backup the database
before upgrading NetBox.

Role Variables
--------------

```
ENTRY POINT: main - Install and configure Netbox

        Install and configure NetBox and create a PostgreSQL database
        for NetBox. This role will also upgrade NetBox when a new
        version is selected. It is recommended to stop the
        netbox.service, netbox-rq.service and netbox-
        housekeeping.timer systemd units, and backup the database
        before upgrading NetBox.

OPTIONS (= is mandatory):

- netbox_allowed_hosts
        List of valid fully-qualified domain names (FQDNs) and/or IP
        addresses that can be used to reach the netbox service,
        usually set to the hostname of the server
        [Default: ['localhost']]
        elements: str
        type: list

- netbox_checksum
        Checksum of the tarball download
        [Default: (null)]
        type: str

- netbox_checksum_type
        Checksum type of netbox_checksum
        [Default: sha256]
        type: str

- netbox_config
        Extra netbox configuration
        [Default: (null)]
        type: dict

- netbox_database
        Name for the netbox postgresql database
        [Default: netbox]
        type: str

- netbox_database_conn_max_age
        Max postgresql database connection age in seconds
        [Default: 300]
        type: int

- netbox_database_host
        Hostname for postgresql connections
        [Default: localhost]
        type: str

- netbox_database_password
        Password for the netbox postgresql user. If defined, the
        password will be set for the netbox postgresql user and
        database connections are created via TCP to
        netbox_database_host. Otherwise, database connections are
        created via the postgresql unix socket
        (netbox_database_socket).
        [Default: (null)]
        type: str

- netbox_database_port
        Port for postgresql connections
        [Default: 5432]
        type: int

- netbox_database_socket
        Path to postgresql unix socket
        [Default: /var/run/postgresql]
        type: str

- netbox_database_user
        Name for the netbox postgresql user
        [Default: netbox]
        type: str

- netbox_group
        Name for the netbox unix group
        [Default: netbox]
        type: str

- netbox_housekeeping_time
        Time for running housekeeping in the systemd calendar event
        format, see https://www.freedesktop.org/software/systemd/man/s
        ystemd.time.html#Calendar%20Events
        [Default: Mon..Sun 01:00]
        type: str

- netbox_ldap_config
        Python code for LDAP configuration, excluding imports and URI
        for LDAP (AUTH_LDAP_SERVER_URI). For configuration options
        see: https://docs.netbox.dev/en/stable/installation/6-ldap/#co
        nfiguration.
        [Default: (null)]
        type: str

- netbox_ldap_enabled
        If true, enable LDAP authentication for netbox
        [Default: False]
        type: bool

- netbox_ldap_extra_imports
        Python code for extra python imports in LDAP configuration
        [Default: (null)]
        type: str

- netbox_ldap_host
        LDAP server hostname
        [Default: (null)]
        type: str

- netbox_ldap_imports
        List of extra python functions to import from
        django_auth_ldap.config in LDAP configuration
        [Default: (null)]
        elements: str
        type: list

- netbox_ldap_packages
        List of packages to install for LDAP
        [Default: ['libldap2-dev', 'libsasl2-dev', 'libssl-dev']]
        elements: str
        type: list

- netbox_ldap_port
        LDAP server port
        [Default: 636]
        type: int

- netbox_ldap_python_packages
        List of python packages to install for LDAP
        [Default: ['django-auth-ldap']]
        elements: str
        type: list

- netbox_ldap_scheme
        URI scheme for LDAP connections
        [Default: ldaps]
        type: str

- netbox_ldap_template
        Template file for LDAP configuration
        [Default: ldap_config.py]
        type: str

- netbox_listen
        Listen address and port
        [Default: localhost:8001]
        type: str

- netbox_log_dir
        Path for log directory
        [Default: /var/log/netbox]
        type: str

- netbox_media_root
        Directory for netbox media
        [Default: /var/lib/netbox/media]
        type: str

- netbox_napalm_enabled
        If true, enable NAPALM
        [Default: False]
        type: bool

- netbox_napalm_python_packages
        List of python packages to install for NAPALM
        [Default: ['napalm']]
        elements: str
        type: list

- netbox_packages
        List of packages to install
        [Default: ['python3-pip', 'python3-venv', 'python3-dev',
        'build-essential', 'libxml2-dev', 'libxslt1-dev', 'libffi-
        dev', 'libpq-dev', 'libssl-dev', 'zlib1g-dev']]
        elements: str
        type: list

- netbox_redis_cache_database
        Redis database ID for caching
        [Default: 1]
        type: int

- netbox_redis_cache_default_timeout
        Default redis connection timeout, in seconds, for caching
        [Default: 300]
        type: int

- netbox_redis_cache_host
        Redis server hostname for caching
        [Default: localhost]
        type: str

- netbox_redis_cache_password
        Password for authentication with redis for caching. Set this
        to an empty string for no password. Defaults to
        netbox_redis_password.
        [Default: (null)]
        type: str

- netbox_redis_cache_port
        Redis server port for caching
        [Default: 6379]
        type: int

- netbox_redis_cache_ssl
        If true, connect to redis server over SSL for caching
        [Default: False]
        type: bool

- netbox_redis_database
        Redis database ID for task queuing
        [Default: 0]
        type: int

- netbox_redis_default_timeout
        Default redis connection timeout, in seconds, for task queuing
        [Default: 300]
        type: int

- netbox_redis_host
        Redis server hostname for task queuing
        [Default: localhost]
        type: str

= netbox_redis_password
        Password for authentication with redis for task queuing. Set
        this to an empty string for no password.

        type: str

- netbox_redis_port
        Redis server port for task queuing
        [Default: 6379]
        type: int

- netbox_redis_ssl
        If true, connect to redis server over SSL for task queuing
        [Default: False]
        type: bool

- netbox_reports
        List of template files for custom report scripts
        [Default: (null)]
        elements: str
        type: list

- netbox_reports_root
        Directory for custom report scripts
        [Default: /opt/netbox/netbox/netbox/reports]
        type: str

- netbox_root
        Netbox install directory
        [Default: /opt/netbox]
        type: str

- netbox_scripts
        List of template files for custom scripts
        [Default: (null)]
        elements: str
        type: list

- netbox_scripts_root
        Directory for custom scripts
        [Default: /opt/netbox/netbox/netbox/scripts]
        type: str

= netbox_secret_key
        Random string used to assist in creating cryptographic hashes
        for passwords and HTTP cookies, see
        https://docs.netbox.dev/en/stable/configuration/required-
        parameters/#secret_key

        type: str

- netbox_superuser_email
        Email for the superuser
        [Default: (null)]
        type: str

- netbox_superuser_password
        Password for the superuser, if left empty the superuser is not
        created
        [Default: (null)]
        type: str

- netbox_superuser_username
        Username for the superuser
        [Default: netbox]
        type: str

- netbox_user
        Name for the netbox unix user
        [Default: netbox]
        type: str

- netbox_venv_python_packages
        List of python packages to upgrade in the virtual environment
        [Default: ['pip', 'setuptools', 'wheel']]
        elements: str
        type: list

- netbox_version
        Version to download and install
        [Default: (null)]
        type: str

- netbox_wsgi_extra
        Extra gunicorn configuration
        [Default: (null)]
        type: dict

- netbox_wsgi_max_requests
        Max number of requests a WSGI worker will process before
        restarting
        [Default: 5000]
        type: int

- netbox_wsgi_max_requests_jitter
        Max jitter to add to the netbox_wsgi_max_requests setting
        [Default: 500]
        type: int

- netbox_wsgi_threads
        Number of threads per WSGI workers
        [Default: 3]
        type: int

- netbox_wsgi_timeout
        Timeout, in seconds, for WSGI workers
        [Default: 120]
        type: int

- netbox_wsgi_workers
        Number of WSGI worker processes for handling requests,
        defaults to the number of threads on the host
        [Default: (null)]
        type: int

- postgresql_user
        Name of the postgresql unix user
        [Default: postgres]
        type: str
```

Installation
------------

This role can either be installed manually with the ansible-galaxy CLI tool:

    ansible-galaxy install git+https://github.com/wandansible/netbox,main,wandansible.netbox
     
Or, by adding the following to `requirements.yml`:

    - name: wandansible.netbox
      src: https://github.com/wandansible/netbox

Roles listed in `requirements.yml` can be installed with the following ansible-galaxy command:

    ansible-galaxy install -r requirements.yml

Example Playbook
----------------

    - hosts: netbox_servers
      roles:
         - role: wandansible.netbox
           become: true
           vars:
             netbox_version: 3.2.3
             netbox_checksum: 78fc3cac957f9d5a671301e0146d0cc8664231e4852774d41b1a17ac20dcf65f
             netbox_listen: localhost:8001
             netbox_superuser_username: admin
             netbox_superuser_password: CHANGEME
             netbox_secret_key: CHANGEME
             netbox_allowed_hosts:
               - ipam.example.org
             netbox_mail_username: netbox@example.org
             netbox_mail_password: password
             netbox_redis_password: CHANGEME
             netbox_config:
               LOGIN_REQUIRED: true
               LOGIN_TIMEOUT: 3600
               EMAIL:
                 SERVER: localhost
                 PORT: 587
                 FROM_EMAIL: "{{ netbox_mail_username }}"
                 USERNAME: "{{ netbox_mail_username }}"
                 PASSWORD: "{{ netbox_mail_password }}"
                 USE_TLS: true
               ADMINS:
                 -
                   - Systems Administrators
                   - "sysadmin@example.org"
               TIME_ZONE: Pacific/Auckland
               LOGGING:
                 version: 1
                 disable_existing_loggers: false
                 handlers:
                   netbox:
                     level: DEBUG
                     class: logging.handlers.RotatingFileHandler
                     filename: /var/log/netbox/netbox.log
                     maxBytes: 512000
                     backupCount: 5
                   netbox_auth_ldap:
                     level: DEBUG
                     class: logging.handlers.RotatingFileHandler
                     filename: /var/log/netbox/netbox-auth-ldap.log
                     maxBytes: 512000
                     backupCount: 5
                 loggers:
                   django:
                     handlers:
                       - netbox
                     level: INFO
