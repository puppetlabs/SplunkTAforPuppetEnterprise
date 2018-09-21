# encoding = utf-8
import json
import urllib2
import sys
def process_event(helper, *args, **kwargs):
    """
    # IMPORTANT
    # Do not remove the anchor macro:start and macro:end lines.
    # These lines are used to generate sample code. If they are
    # removed, the sample code will not be updated when configurations
    # are updated.

    [sample_code_macro:start]

    # The following example gets the setup parameters and prints them to the log
    victor_ops_token = helper.get_global_setting("victor_ops_token")
    helper.log_info("victor_ops_token={}".format(victor_ops_token))

    # The following example gets and sets the log level
    helper.set_log_level(helper.log_level)

    # The following example gets the alert action parameters and prints them to the log
    dropdown_list = helper.get_param("dropdown_list")
    helper.log_info("dropdown_list={}".format(dropdown_list))

    alert_entity_id = helper.get_param("alert_entity_id")
    helper.log_info("alert_entity_id={}".format(alert_entity_id))

    state_message = helper.get_param("state_message")
    helper.log_info("state_message={}".format(state_message))


    # The following example adds two sample events ("hello", "world")
    # and writes them to Splunk
    # NOTE: Call helper.writeevents() only once after all events
    # have been added
    helper.addevent("hello", sourcetype="sample_sourcetype")
    helper.addevent("world", sourcetype="sample_sourcetype")
    helper.writeevents(index="summary", host="localhost", source="localhost")

    # The following example gets the events that trigger the alert
    events = helper.get_events()
    for event in events:
        helper.log_info("event={}".format(event))

    # helper.settings is a dict that includes environment configuration
    # Example usage: helper.settings["server_uri"]
    helper.log_info("server_uri={}".format(helper.settings["server_uri"]))
    [sample_code_macro:end]
    """
    
    victor_ops_token = helper.get_global_setting("victor_ops_token")
    alert_entity_id = helper.get_param("alert_entity_id")
    dropdown_list = helper.get_param("dropdown_list")
    state_message = helper.get_param("state_message")
    view_report = helper.get_param("dropdown_list")
    
    url = "https://alert.victorops.com/integrations/generic/20131114/alert/" + victor_ops_token + ""
    
    search_name = helper.get_events()
    entity_id = "Puppet Enterprise Alert: %s" % search_name
    
    view_report = helper.get_param('results_link')
    
    helper.log_info("Alert action Puppet Enterprise VictorOps Alert Action started.")
    
    data = dict(
        message_type=dropdown_list,
        monitoring_tool='Puppet Enterprise',
        state_message=state_message,
        entity_id=alert_entity_id,
        view_report=view_report
    )
    
    body = json.dumps(data)
    
    req = urllib2.Request(url, body, {"Content-Type": "application/json"})
    
    try:
        res = urllib2.urlopen(req)
        body = res.read()
        print >> sys.stderr, "INFO VictorOps server responded with HTTP status=%d" % res.code
        print >> sys.stderr, "DEBUG VictorOps server response: %s" % json.dumps(body)
        return 200 <= res.code < 300
    except urllib2.HTTPError, e:
        print >> sys.stderr, "ERROR Error sending message: %s (%s)" % (e, str(dir(e)))
        print >> sys.stderr, "ERROR Server response: %s" % e.read()
        return False
     
   

    # TODO: Implement your alert action logic here
    return 0
