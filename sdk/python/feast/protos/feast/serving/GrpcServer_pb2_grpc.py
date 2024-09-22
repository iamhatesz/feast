# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from feast.protos.feast.serving import GrpcServer_pb2 as feast_dot_serving_dot_GrpcServer__pb2
from feast.protos.feast.serving import ServingService_pb2 as feast_dot_serving_dot_ServingService__pb2


class GrpcFeatureServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Push = channel.unary_unary(
                '/GrpcFeatureServer/Push',
                request_serializer=feast_dot_serving_dot_GrpcServer__pb2.PushRequest.SerializeToString,
                response_deserializer=feast_dot_serving_dot_GrpcServer__pb2.PushResponse.FromString,
                )
        self.WriteToOnlineStore = channel.unary_unary(
                '/GrpcFeatureServer/WriteToOnlineStore',
                request_serializer=feast_dot_serving_dot_GrpcServer__pb2.WriteToOnlineStoreRequest.SerializeToString,
                response_deserializer=feast_dot_serving_dot_GrpcServer__pb2.WriteToOnlineStoreResponse.FromString,
                )
        self.GetOnlineFeatures = channel.unary_unary(
                '/GrpcFeatureServer/GetOnlineFeatures',
                request_serializer=feast_dot_serving_dot_ServingService__pb2.GetOnlineFeaturesRequest.SerializeToString,
                response_deserializer=feast_dot_serving_dot_ServingService__pb2.GetOnlineFeaturesResponse.FromString,
                )


class GrpcFeatureServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Push(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteToOnlineStore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOnlineFeatures(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GrpcFeatureServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Push': grpc.unary_unary_rpc_method_handler(
                    servicer.Push,
                    request_deserializer=feast_dot_serving_dot_GrpcServer__pb2.PushRequest.FromString,
                    response_serializer=feast_dot_serving_dot_GrpcServer__pb2.PushResponse.SerializeToString,
            ),
            'WriteToOnlineStore': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteToOnlineStore,
                    request_deserializer=feast_dot_serving_dot_GrpcServer__pb2.WriteToOnlineStoreRequest.FromString,
                    response_serializer=feast_dot_serving_dot_GrpcServer__pb2.WriteToOnlineStoreResponse.SerializeToString,
            ),
            'GetOnlineFeatures': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOnlineFeatures,
                    request_deserializer=feast_dot_serving_dot_ServingService__pb2.GetOnlineFeaturesRequest.FromString,
                    response_serializer=feast_dot_serving_dot_ServingService__pb2.GetOnlineFeaturesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GrpcFeatureServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GrpcFeatureServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Push(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcFeatureServer/Push',
            feast_dot_serving_dot_GrpcServer__pb2.PushRequest.SerializeToString,
            feast_dot_serving_dot_GrpcServer__pb2.PushResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteToOnlineStore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcFeatureServer/WriteToOnlineStore',
            feast_dot_serving_dot_GrpcServer__pb2.WriteToOnlineStoreRequest.SerializeToString,
            feast_dot_serving_dot_GrpcServer__pb2.WriteToOnlineStoreResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOnlineFeatures(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GrpcFeatureServer/GetOnlineFeatures',
            feast_dot_serving_dot_ServingService__pb2.GetOnlineFeaturesRequest.SerializeToString,
            feast_dot_serving_dot_ServingService__pb2.GetOnlineFeaturesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
