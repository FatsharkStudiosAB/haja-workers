package state

import (
	"github.com/FatsharkStudiosAB/haja-workers/go/internal/basefunction"
	"github.com/FatsharkStudiosAB/haja-workers/go/internal/communication"
	"github.com/FatsharkStudiosAB/haja-workers/go/internal/dispatcher"
	"github.com/FatsharkStudiosAB/haja-workers/go/internal/grpccache"
	"github.com/FatsharkStudiosAB/haja-workers/go/internal/grpcstore"
	"github.com/FatsharkStudiosAB/haja-workers/go/internal/maps"
	"github.com/FatsharkStudiosAB/haja-workers/go/internal/rpc"
)

type GlobalState struct {
	GrpcCache        *grpccache.Client
	GrpcStore        *grpcstore.Client
	ServerName       string
	Functions        *maps.SafeFunctionMap[string, basefunction.FunctionInterface]
	ResponseHandlers *maps.SafeFunctionMap[string, chan *[]byte]
	RpcClient        *rpc.RpcClient
	ExecutionState   *maps.SafeFunctionMap[string, any]
	WorkflowComm     communication.WorkflowCommunicator
	Dispatcher       *dispatcher.Dispatcher
}
