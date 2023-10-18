import logging

from localstack import config
from localstack.extensions.api import Extension, http, aws

LOG = logging.getLogger(__name__)


class RequestInterceptor(aws.RequestHandler):
    def __call__(self, chain: aws.HandlerChain, context: aws.RequestContext, response: http.Response):
        if not context.service:
            return

        LOG.info(
            "Intercepting request service=%s operation=%s account_id=%s region=%s",
            context.service.service_name,
            context.operation.name,
            context.account_id,
            context.region,
        )

        # TODO: you can do anything you want with the request here. the parsed request is stored in
        #  ``context.service_request``..for instance, you could proxy the request by using boto3 to call another backend
        #  with the parsed request, and use ``chain.respond()`` to return immediately


class RequestInterceptorExtension(Extension):
    name = "localstack-extension-aws-request-interceptor"

    def on_extension_load(self):
        LOG.setLevel(level=logging.DEBUG if config.DEBUG else logging.INFO)
        LOG.info("AWS request interceptor: extension is loaded")

    def update_gateway_routes(self, router: http.Router[http.RouteHandler]):
        """Here you can patch generic HTTP routes that are execute before the service request parser"""

    def update_request_handlers(self, handlers: aws.CompositeHandler):
        """Here you can patch handlers that are executed before the parsed request goes into a service."""
        handlers.append(RequestInterceptor())

    def update_response_handlers(self, handlers: aws.CompositeResponseHandler):
        """Here you can patch handlers that are executed after the request has gone through a service."""
