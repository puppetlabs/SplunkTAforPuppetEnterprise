
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


def merge_dicts(dict1, dict2):
    for k in set(dict1.keys()).union(dict2.keys()):
        if k in dict1 and k in dict2:
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                yield (k, dict(merge_dicts(dict1[k], dict2[k])))
            else:
                # If one of the values is not a dict, you can't continue merging it.
                # Value from second dict overrides one in first and we move on.
                yield (k, dict2[k])
                # Alternatively, replace this with exception raiser to alert you of value conflicts
        elif k in dict1:
            yield (k, dict1[k])
        else:
            yield (k, dict2[k])

def collect_events(helper, ew):
   
    import datetime
    import json
    import jsonpath_rw
    
    method = 'GET'
    api_request = 'application/json'
    
    api_token = helper.get_global_setting("token_")
    server = helper.get_arg('server_')
    port = helper.get_arg('port_')
    type_of_environment = helper.get_arg('environment')
    pe_server_url = helper.get_arg('puppet_enterprise_server_')
    pe_token = helper.get_arg('token_')
    pe_expiration = helper.get_arg('token_generation_date_')
    
    input_source = helper.get_input_stanza_names()
    
    url = server + ":" + port + "/pdb/query/v4/inventory?query= [\"=\",\"environment\",\"" + type_of_environment + "\"]"
    
    if pe_link:
        input_source = pe_server_url
    else:
        input_source = pe_server_url
    
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
            temp_one_dict1 = one_dict['facts']['trusted']
            temp_one_dict2 = one_dict['facts']['ruby']

            # temp_one_dict = merge_dicts(temp_one_dict1, temp_one_dict2)
            
            for key, value in temp_one_dict1.iteritems():
                temp_one_dict2[key] = value
                temp_one_dict2['hostname'] = one_dict['facts']['hostname']
                temp_one_dict2['aio_agent_build'] = one_dict['facts']['aio_agent_build']
                temp_one_dict2['aio_agent_version'] = one_dict['facts']['aio_agent_version']
                temp_one_dict2['clientversion'] = one_dict['facts']['clientversion']
                temp_one_dict2['architecture'] = one_dict['facts']['architecture']
                temp_one_dict2['bios_release_date'] = one_dict['facts']['bios_release_date']
                temp_one_dict2['bios_vendor'] = one_dict['facts']['bios_vendor']
                temp_one_dict2['hostname'] = one_dict['facts']['hostname']
                temp_one_dict2['macaddress'] = one_dict['facts']['macaddress']
                temp_one_dict2['facterversion'] = one_dict['facts']['facterversion']
                temp_one_dict2['filesystems'] = one_dict['facts']['filesystems']
                temp_one_dict2['osfamily'] = one_dict['facts']['osfamily']
                temp_one_dict2['operatingsystem'] = one_dict['facts']['operatingsystem']
                temp_one_dict2['operatingsystemmajrelease'] = one_dict['facts']['operatingsystemmajrelease']
                temp_one_dict2['operatingsystemrelease'] = one_dict['facts']['operatingsystemrelease']
                temp_one_dict2['selinux'] = one_dict['facts']['selinux']
                temp_one_dict2['fqdn'] = one_dict['facts']['fqdn']
                temp_one_dict2['ipaddress'] = one_dict['facts']['ipaddress']
                temp_one_dict2['ipaddress6'] = one_dict['facts']['ipaddress6']
                temp_one_dict2['is_virtual'] = one_dict['facts']['is_virtual']
                temp_one_dict2['puppetversion'] = one_dict['facts']['puppetversion']
                temp_one_dict2['processorcount'] = one_dict['facts']['processorcount']
                temp_one_dict2['processors'] = one_dict['facts']['processors']
                temp_one_dict2['kernel'] = one_dict['facts']['kernel']
                temp_one_dict2['kernelmajversion'] = one_dict['facts']['kernelmajversion']
                temp_one_dict2['kernelrelease'] = one_dict['facts']['kernelrelease']
                temp_one_dict2['selinux'] = one_dict['facts']['selinux']
                temp_one_dict2['serialnumber'] = one_dict['facts']['serialnumber']
                temp_one_dict2['uptime'] = one_dict['facts']['uptime']
                temp_one_dict2['uptime_days'] = one_dict['facts']['uptime_days']
                temp_one_dict2['uptime_hours'] = one_dict['facts']['uptime_hours']
                temp_one_dict2['uptime_seconds'] = one_dict['facts']['uptime_seconds']
                temp_one_dict2['uuid'] = one_dict['facts']['uuid']
                temp_one_dict2['virtual'] = one_dict['facts']['virtual']
                temp_one_dict2['uptime'] = one_dict['facts']['uptime']
                temp_one_dict2['pe_server_url_'] = pe_server_url
                temp_one_dict2['expiration'] = pe_expiration
            
            one_dict = temp_one_dict2
            
            data = json.dumps(one_dict,sort_keys=True)

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
    
    
