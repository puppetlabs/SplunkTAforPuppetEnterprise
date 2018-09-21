# Splunk Add-on for Puppet Enterprise - Docs
----
- Splunk Add-on Community Supported (Puppet & Splunk Customers)
### - Requirements to Run App
- Splunk Enterprise 7.0+
- Puppet Enterprise 2018.1.1+

### - Installation Steps
----
- First generate a token from Puppet Enterprise in the shell. Make sure to take into account how long you have the token generated. We recommend to at least set it too 12 Months. We will be putting this in the Add-on Menu to help you alert when it about to expire. 
```
curl -k -X POST -H 'Content-Type: application/json' -d '{"login": "", "password": "","lifetime": "9y" }' https://$:4433/rbac-api/v1/auth/token
```
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

### Todos
----
 - Adding Test for TravisCI for Splunk App-Inspect

### Version History 
----
**Version 1.0**
- Includes Support for Self Signed (8081) + HTTP (8080) for PuppetDB Calls
- Rewrite of all Extraction Fields + Cleanup of Resources, Classes, and CertName
- Fixed API Key Storage
- Fixed Title to Match Pulls
- Fixed Help Text to Match Fields
- Fixed Issue with Memoryleak on Timeout API Calls

**Version 2.0**
- Support for Multiple Version of Puppet Enterprise
- Rewrite of the Factor Pull, Customer Merge Dict Feature to Only Pull certain facts. 
- Added PE Metrics for MQ
- Added Compiliation Timing
- Filter for Multiple Version of Puppet Enterprise
- Integration of VictorOps for Notification and Alerting

### License
----
[Splunk Third Party](http://docs.splunk.com/Documentation/AddonBuilder/2.2.0/UserGuide/Validate#Credit_third-party_libraries)

##### MIT License
Copyright (c) [2017] [Splunk]
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Support
----
Are you a Splunk + Puppet customer who enjoys sharing knowledge and want to put some great feature into an opensource project. We encourage you to submit issues and pull request so that we can make this Technical Addon better and help the community as a whole get better insight to their Puppet Enterprise deployments.

Feel free to leave comments or questions. We are here to make this community project more adaptive to all types of use cases.
