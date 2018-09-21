
# encoding = utf-8

import os
import sys
import time
import datetime
import json
import jsonpath_rw
from datetime import datetime

def validate_input(helper, definition):
    """Implement your own validation logic to validate the input stanza configurations"""
    # This example accesses the modular input variable
    # server = definition.parameters.get('server', None)
    # port = definition.parameters.get('port', None)
    pass

def validate_input(helper, definition):
    """Implement your own validation logic to validate the input stanza configurations"""
    # This example accesses the modular input variable
    # server = definition.parameters.get('server', None)
    # port = definition.parameters.get('port', None)
    pass

def collect_events(helper, ew):
   
    import datetime
    import json
    import jsonpath_rw
    
    method = 'GET'
    api_request = 'application/json' 
    
    api_token = helper.get_global_setting("token_")
    server = helper.get_arg('server_')
    port = helper.get_arg('port_')
    pe_token = helper.get_arg('token_')
    pe_link = helper.get_arg('puppet_enterprise_server_')

    
    url = server + ":" + port + "/metrics/v1/mbeans/puppetlabs.puppetdb.mq%3Aname%3Dglobal.processing-time"
    
    if pe_link:
        input_source = pe_link
    else:
        input_source = pe_link
    
    
    headers = {
           'X-Authentication': pe_token, 
           'Content-type': api_request
           }
           
    response = helper.send_http_request(url, 
                                        method, 
                                        parameters=None, 
                                        payload=None,
                                        headers=headers, 
                                        cookies=None, 
                                        verify=False, 
                                        cert=None,
                                        timeout=None, 
                                        use_proxy=True)
     
    r_status = response.status_code
    response.raise_for_status()
    helper.log_error (response.text) 
    
    r= response.json()
     
    input_type = helper.get_input_type()
    
    for stanza_name in helper.get_input_stanza_names():
        
        data = json.dumps(r, sort_keys=False)
        
        event = helper.new_event(source=input_source, index=helper.get_output_index(stanza_name), sourcetype=helper .get_sourcetype(stanza_name), data=data)
        helper.log_error (response.text) 
        try:
            ew.write_event(event)
            helper.log_error (response.text) 
        except Exception as e:
            raise e
        return;