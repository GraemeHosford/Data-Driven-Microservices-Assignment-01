# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import redditreader_pb2 as redditreader__pb2


class RedditReaderStub(object):
    """Reddit reader service docs
    """

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.getRedditPosts = channel.unary_stream(
            '/redditreader.RedditReader/getRedditPosts',
            request_serializer=redditreader__pb2.RedditRequest.SerializeToString,
            response_deserializer=redditreader__pb2.RedditInfo.FromString,
        )


class RedditReaderServicer(object):
    """Reddit reader service docs
    """

    def getRedditPosts(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RedditReaderServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'getRedditPosts': grpc.unary_stream_rpc_method_handler(
            servicer.getRedditPosts,
            request_deserializer=redditreader__pb2.RedditRequest.FromString,
            response_serializer=redditreader__pb2.RedditInfo.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'redditreader.RedditReader', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))