[puppet_enterprise_extended_details://<name>]
token_ = curl -k -X POST -H 'Content-Type: application/json' -d '{"login": "", "password": "","lifetime": "9y" }' https://$:4433/rbac-api/v1/auth/token
puppet_enterprise_server_ = Put in your FQDN of your Puppet Enterprise Server so the links backs on the dashboards work correctly.
server_ = Input your Puppet Enterprise Server address.
port_ = Input your Puppet Enterprise DB Port (HTTPS 8081, HTTP: 8080)

[puppet_enterprise_metrics://<name>]
token_ = curl -k -X POST -H 'Content-Type: application/json' -d '{"login": "", "password": "","lifetime": "9y" }' https://$:4433/rbac-api/v1/auth/token
puppet_enterprise_server_ = Put in your FQDN of your Puppet Enterprise Server so the links backs on the dashboards work correctly.
server_ = Input your Puppet Enterprise Server address.
port_ = Input your Puppet Enterprise DB Port (HTTPS 8081, HTTP: 8080)

[puppet_enterprise_overview_enforcement://<name>]
puppet_enterprise_server_ = Put in your FQDN of your Puppet Enterprise Server so the links backs on the dashboards work correctly.
server_ = Input your Puppet Enterprise Server address.
token_ = curl -k -X POST -H 'Content-Type: application/json' -d '{"login": "", "password": "","lifetime": "9y" }' https://$:4433/rbac-api/v1/auth/token
port_ = Input your Puppet Enterprise DB Port (HTTPS 8081, HTTP: 8080)

[puppet_enterprise_status_overview://<name>]
puppet_enterprise_server_ = Put in your FQDN of your Puppet Enterprise Server so the links backs on the dashboards work correctly.
server_ = Input your Puppet Enterprise Server address.
token_ = curl -k -X POST -H 'Content-Type: application/json' -d '{"login": "", "password": "","lifetime": "9y" }' https://$:4433/rbac-api/v1/auth/token
port_ = Input your Puppet Enterprise DB Port (HTTPS 8081, HTTP: 8080)

[puppet_enterprise_factors://<name>]
token_ = curl -k -X POST -H 'Content-Type: application/json' -d '{"login": "", "password": "","lifetime": "9y" }' https://$:4433/rbac-api/v1/auth/token
token_generation_date_ = Input the date when you generated your token.
server_ = Input your Puppet Enterprise Server address.
puppet_enterprise_server_ = Input your Puppet Enterprise Server
port_ = Input your Puppet Enterprise DB Port (HTTPS 8081, HTTP: 8080)
environment = Puppet Enterprise Environment you want to monitor.