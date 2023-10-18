aws-request-interceptor
===============================

Extension example to show how to intercept AWS requests

## Install local development version

To install the extension into localstack in developer mode, you will need Python 3.11, and create a virtual environment in the extensions project.

In the newly generated project, simply run

```bash
make install
```

Then, to enable the extension for LocalStack, run

```bash
localstack extensions dev enable .
```

You can then start LocalStack with `EXTENSION_DEV_MODE=1` to load all enabled extensions:

```bash
EXTENSION_DEV_MODE=1 localstack start
```

When you make a call to an AWS service, you should see something like this in the log:

```
2023-10-18T18:26:32.781  INFO --- [   asgi_gw_0] r.extension                : Intercepting request service=sqs operation=ListQueues account_id=000000000000 region=us-east-1
2023-10-18T18:26:37.595  INFO --- [   asgi_gw_0] r.extension                : Intercepting request service=sqs operation=CreateQueue account_id=000000000000 region=us-east-1
2023-10-18T18:27:32.855  INFO --- [   asgi_gw_0] r.extension                : Intercepting request service=cloudwatch operation=PutMetricData account_id=000000000000 region=us-east-1
2023-10-18T18:27:33.247  INFO --- [   asgi_gw_0] r.extension                : Intercepting request service=cloudwatch operation=PutMetricData account_id=000000000000 region=us-east-1
```
