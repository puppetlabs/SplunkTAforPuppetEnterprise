- Custom Factor Pull Setup (Option Step) - Make PR if you want to add a default to the pull.
```
 for key, value in temp_one_dict1.iteritems():
                temp_one_dict2[key] = value
                temp_one_dict2['hostname'] = one_dict['facts']['hostname']
                temp_one_dict2['aio_agent_build'] = one_dict['facts']['aio_agent_build]'
```          
- Setup Dictonary Key and then Reference back to API to see how you can browse for specific custom field. Reference Link to API: https://puppet.com/docs/puppetdb/5.2/api/query/v4/resources.html

### - Output of Factors in Json
----
```
aio_agent_build:	 5.5.6	
  	 aio_agent_version:	 5.5.6	
  	 architecture:	 x86_64	
  	 authenticated:	 remote	
  	 bios_release_date:	 11/29/2017	
  	 bios_vendor:	 Xen	
  	 certname:	 testing1234	
  	 clientversion:	 5.5.6	
  	 domain:	 null	
  	 expiration:	 09/11/2018	
  	 extensions:	{	[-]	
  	}	
  	 facterversion:	 3.11.4	
  	 filesystems:	 xfs	
  	 fqdn:	 testing1234	
  	 hostname:	 testing1234	
  	 ipaddress:	 10.1.2,0	
  	 ipaddress6:	 fe80::f48a:3947:7787:7775	
  	 is_virtual:	 true	
  	 kernel:	 Linux	
  	 kernelmajversion:	 3.10	
  	 kernelrelease:	 3.10.0-693.21.1.el7.x86_64	
  	 macaddress:	 f2:64:33:78:12:24	
  	 operatingsystem:	 CentOS	
  	 operatingsystemmajrelease:	 7	
  	 operatingsystemrelease:	 7.4.1708	
  	 osfamily:	 RedHat	
  	 pe_server_url_:	 automate01	
  	 platform:	 x86_64-linux	
  	 processorcount:	 8	
  	 processors:	{	[-]	
    	 count:	 8	
    	 isa:	 x86_64	
    	 models:	[	[-]	
      	 Intel(R) Xeon(R) Gold 5115 CPU @ 2.40GHz	
      	 Intel(R) Xeon(R) Gold 5115 CPU @ 2.40GHz	
      	 Intel(R) Xeon(R) Gold 5115 CPU @ 2.40GHz	
      	 Intel(R) Xeon(R) Gold 5115 CPU @ 2.40GHz	
      	 Intel(R) Xeon(R) Gold 5115 CPU @ 2.40GHz	
      	 Intel(R) Xeon(R) Gold 5115 CPU @ 2.40GHz	
      	 Intel(R) Xeon(R) Gold 5115 CPU @ 2.40GHz	
      	 Intel(R) Xeon(R) Gold 5115 CPU @ 2.40GHz	
    	]	
    	 physicalcount:	 4	
  	}	
  	 puppetversion:	 5.5.6	
  	 selinux:	 true	
  	 serialnumber:	 bc383f9f-c537-9c11-78f1-2274faf798ec	
  	 sitedir:	 /opt/puppetlabs/puppet/lib/ruby/site_ruby/2.4.0	
  	 uptime:	 116 days	
  	 uptime_days:	 116	
  	 uptime_hours:	 2784	
  	 uptime_seconds:	 10022871	
  	 uuid:	 BC383F9F-C537-9C11-78F1-2274FAF798EC	
  	 version:	 2.4.4	
  	 virtual:	 xenhvm	
```

### Extended Details Pull Feature Explanation
----
```
certname:	 testing1234	
  	 configuration_version:	 1537159231	
  	 containing_class:	 Motd	
  	 containment_path:	[	[+]	
  	]	
  	 corrective_change:	 false	
  	 environment:	 production	
  	 file:	 /etc/puppetlabs/code/environments/production/modules/motd/manifests/init.pp	
  	 line:	 84	
  	 message:	 content changed '{md5}91e9830c08a9c585a061401389e48e38' to '{md5}c89ef7290d4031def9b9a4b419ad33a1'	
  	 new_value:	 {md5}c89ef7290d4031def9b9a4b419ad33a1	
  	 old_value:	 {md5}91e9830c08a9c585a061401389e48e38	
  	 property:	 content	
  	 report:	 6e6b17efc5043981131145fc5593a3dc6602d2cb	
  	 report_receive_time:	 2018-09-17T04:41:02.934Z	
  	 resource_title:	 /etc/motd	
  	 resource_type:	 File	
  	 run_end_time:	 2018-09-17T04:41:02.364Z	
  	 run_start_time:	 2018-09-17T04:40:27.861Z	
  	 status:	 success	
  	 timestamp:	 2018-09-17T04:40:38.709Z	
```

- Configuration state in Pull and reference fields are pulled from the following API. Reference Link to API: https://docs.puppet.com/puppetdb/4.0/api/query/v4/reports.html
