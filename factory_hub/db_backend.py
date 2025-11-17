"""
Custom PostgreSQL backend that forces IPv4 connections.
Workaround for Render's lack of IPv6 support with Supabase.
"""
import socket
from django.db.backends.postgresql import base


class DatabaseWrapper(base.DatabaseWrapper):
    """PostgreSQL database backend that forces IPv4."""
    
    def get_connection_params(self):
        params = super().get_connection_params()
        
        # Force IPv4 resolution
        if 'host' in params and params['host']:
            try:
                # Resolve hostname to IPv4 only
                hostname = params['host']
                ipv4_address = socket.getaddrinfo(
                    hostname, 
                    None, 
                    socket.AF_INET,  # Force IPv4
                    socket.SOCK_STREAM
                )[0][4][0]
                params['host'] = ipv4_address
            except (socket.gaierror, IndexError):
                # If resolution fails, keep original host
                pass
        
        return params
