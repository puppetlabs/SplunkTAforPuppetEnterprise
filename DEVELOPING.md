## Developing addon builders

In order to load this module properly into the Splunk Add-On builder for development, the following needs to happen:

- Checkout the branch you want to work on
- tar.gz the directory
- Go to the splunk addon builder
- Delete a previous version of the add-on if it exists
- Import this version

```
$ git checkout -b 'my working branch'
$ tar --exclude=".git" --exclude="tmpdir" -czvf tmpdir/SplunkTAforPuppetEnterprise.tar.gz ./*
```

To add your finished work back to the repo:
- Export the build from the Splunk Add-On tool
- Move the 