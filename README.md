# slack-dtr
DTR Slack Notification Service

Simple web service to accept incomming webhooks from Docker DTR and forward them to a Slack channel. By default, the web service listens on port 80

You can add your Slack Applicaiton URL by opening your browser and accessing the web service (i.e. http://your.service.url)

The following API endpoints have been configured for each of the supported DTR webhooks.

Tag pushed to repository	---> /push

Tag deleted on repository	---> /delete

Image promoted from repository	---> /promote

Security scan completed	 ---> /scan

Security scan failed	---> /scanfail

Manifest pushed to repository	---> /addmanifest

Manifest deleted on repository	---> /delmanifest
