# Slack Status

This is a nagios/sensu check to announce when Slack's status page changes from the default "Smooth Sailing!"

## Installation

You need `python` and a `pip install BeautifulSoup4` to get this to work.

After you have it, run it via:

```shell
$ python slack_status.py
Smooth Sailing! # will appear if everything is working as expected
$ cp slack_status.py  /usr/lib/nagios/plugins/slack_status.py
$ chmod +x /usr/lib/nagios/plugins/slack_status.py
```

It will Error with a `Critical` (exit code 2) if `Connectivity issues for all customers` shows up on the site. Otherwise it  will throw a warning
(exit code 1) if anything other then `Smooth Sailing!` appears.

It's a very straight forward website scrape of the status page, but adding it to your nagios/sensu installation you'll get a proactive notice
when something goes other then all systems are functional status.

In your `commands.cfg` put something like:
```
define command {
   command_name check-slack-status
   command_line /usr/lib/nagios/plugins/slack_status.py
}
```

In your `services.cfg` add something like this:
```
define service {
    service_description Slack Status
    use default-service
    host nagios
    check_command  check-slack-status
}
```

## License and Authors
- Author:: JJ Asghar (jjasghar@gmail.com)

```text
Copyright 2018 JJ Asghar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
