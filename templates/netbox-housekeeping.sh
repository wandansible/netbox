#!/bin/sh
# {{ ansible_managed }}
{{ netbox_root }}/netbox/venv/bin/python {{ netbox_root }}/netbox/netbox/manage.py housekeeping
