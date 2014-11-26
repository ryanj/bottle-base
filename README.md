# A basic Bottle quickstart 
*With support for serving easy APIs and static content*

[![Build Status](http://img.shields.io/travis/ryanj/bottle-base.svg)](https://travis-ci.org/ryanj/bottle-base)

[![LAUNCH ON OpenShift](https://launch-shifter.rhcloud.com/launch/LAUNCH ON.svg)](https://launch-shifter.rhcloud.com/r?url=https%3A%2F%2Fopenshift.redhat.com%2Fapp%2Fconsole%2Fapplication_type%2Fcustom%3F%26cartridges%5B%5D%3Dpython%26initial_git_url%3Dhttps%3A%2F%2Fgithub.com%2Fryanj%2Fbottle-base.git%26name%3Dbottle)

To deploy a clone of this application using the [`rhc` command line tool](http://rubygems.org/gems/rhc):

    rhc app create bottle python-2.7 --from-code=https://github.com/ryanj/bottle-base.git
    
Or [link to a web-based clone+deploy](https://openshift.redhat.com/app/console/application_type/custom?cartridges%5B%5D=python-2.7&initial_git_url=https%3A%2F%2Fgithub.com%2Fryanj%2Fbottle-base.git) on [OpenShift Online](http://OpenShift.com) or on [your own OpenShift cloud](http://openshift.github.io): 

    https://openshift.redhat.com/app/console/application_type/custom?cartridges%5B%5D=python-2.7&initial_git_url=https%3A%2F%2Fgithub.com%2Fryanj%2Fbottle-base.git

## Local server
Start a local webserver by running:

```bash
python app.py
```

## License
This code is dedicated to the public domain to the maximum extent permitted by applicable law, pursuant to CC0 (http://creativecommons.org/publicdomain/zero/1.0/)
