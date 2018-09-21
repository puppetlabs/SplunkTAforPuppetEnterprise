
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
    pe_server = helper.get_arg('puppet_enterprise_server_')

    if pe_server:
        input_source = pe_server
    else:
        input_source = pe_server
    
    #get current time
    now = datetime.datetime.now()
    
    #get checkpoint value
    ckpt = "start_time"
    ckpt_value = helper.get_check_point(ckpt)

    #if there is no checkpoint value - that means its an initial load - set start time to now - 5 Minute
    if ckpt_value == None:
        old = now - datetime.timedelta(minutes=5)
        #format the time
        # This is a timestamp in UTC-based ISO-8601 format (YYYY-MM-DDThh:mm:ssZ) 
        start_time = old.strftime("%Y-%m-%dT%H:%M:%SZ") 
    #if it does exist then checkpoint value is start time
    else:
        start_time=ckpt_value

    end_time=now.strftime("%Y-%m-%dT%H:%M:%SZ") 
    
    url = server + ":" + port + "/pdb/query/v4/nodes?order_by=[{\"field\":\"report_timestamp\",\"order\":\"desc\"}]&limit=50&offset=0&include_total=true&query=[\"extract\",[\"certname\",\"report_environment\",\"report_timestamp\",\"latest_report_hash\",\"latest_report_status\",\"latest_report_noop\",\"latest_report_noop_pending\",\"latest_report_corrective_change\",\"latest_report_job_id\"],null]"
    
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
        
        for one_dict in r:
            data = json.dumps(one_dict,sort_keys=False)
        
            event = helper.new_event(source=input_source, index=helper.get_output_index(stanza_name), sourcetype=helper .get_sourcetype(stanza_name), data=data)
            helper.log_error (response.text) 
            try:
                ew.write_event(event)
                helper.log_error (response.text) 
            except Exception as e:
                raise e
        return;
    
    #save checkpoint value to end_time which is data collection time
    ckpt_value = helper.save_check_point(ckpt, end_time)