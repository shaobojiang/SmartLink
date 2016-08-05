#!/usr/bin/env python
import os
import sys
from MyHttpServer.socketServerInit import socketInit
from MyHttpServer.gl import isSocketRunning


if __name__ == "__main__":  

    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SmartLink.settings")
    socketInit()
    
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    
    
    
