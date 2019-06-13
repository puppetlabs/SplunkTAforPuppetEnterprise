# DEPRECATED

*** Please note this App has been deprecated in favour of the Splunk_hec module which can be found [here in Github](https://github.com/puppetlabs/puppetlabs-splunk_hec) and [here in the Forge](https://forge.puppet.com/puppetlabs/splunk_hec) ***

# Splunk Add-on for Puppet Enterprise

The Splunk Add-on for Puppet Enterprise collects machine data from using the PuppetDB API.

## Requirements to run this add-on

- Splunk Enterprise 7.0+
- Puppet Enterprise 2018.1.1+
- Splunk App for Puppet Enterprise (Obtain from [Github](https://github.com/puppetlabs/SplunkAppforPuppetEnterprise/)) — _This component visualises data from Puppet Enterprise collected and stored in Splunk by this add-on._

## Installation Steps

1. First generate an authentication token for Puppet Enterprise. Make sure to specify a suffeciently long lifetime for the token. We recommend at least 12 months. Detailed instructions are available from the [Puppet Enterprise documentation](https://puppet.com/docs/pe/latest/rbac_token_auth_intro.html#generate-a-token-using-the-api-endpoint).

    Sample command:

    ```shell
    curl -k -X POST -H 'Content-Type: application/json' -d '{"login": "", "password": "","lifetime": "9y" }' https://$:4433/rbac-api/v1/auth/token
    ```

    You'll get back something that looks like `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9`. Keep this handy for the next step.

1. Navigate to the Add-on within the Splunk console.
1. Select the "Create New Input" on the "Data inputs" view. Follow the instructions in the forms to connect the add-on to your Puppet Enterprise installation. It asks for things like server name, authentication token, and so on.
1. Install the companion [app](https://github.com/puppetlabs/SplunkAppforPuppetEnterprise/) into Splunk to visualize data ingested from Puppet Enterprise.

## Version history

### Version 2.0

- Support for Multiple Version of Puppet Enterprise
- Rewrite of the Factor Pull, Customer Merge Dict Feature to Only Pull certain facts.
- Added PE Metrics for MQ
- Added Compiliation Timing
- Filter for Multiple Version of Puppet Enterprise
- Integration of VictorOps for Notification and Alerting

### Version 1.0

- Includes Support for Self Signed (8081) + HTTP (8080) for PuppetDB Calls
- Rewrite of all Extraction Fields + Cleanup of Resources, Classes, and CertName
- Fixed API Key Storage
- Fixed Title to Match Pulls
- Fixed Help Text to Match Fields
- Fixed Issue with Memoryleak on Timeout API Calls

## Support

Are you a Splunk + Puppet customer who enjoys sharing knowledge and want to put some great features into an open-source project. We encourage you to [submit issues](https://github.com/puppetlabs/SplunkAppforPuppetEnterprise/issues/new) and pull requests so that we can make this Technical Addon better and help the community as a whole get better insight to their Puppet Enterprise deployments.

Feel free to leave comments or questions. We are here to make this community project more adaptive to all types of use cases.
