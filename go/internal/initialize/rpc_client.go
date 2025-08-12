package initialize

import (
	"github.com/FatsharkStudiosAB/haja-workers/go/internal/rpc"
	"github.com/FatsharkStudiosAB/haja-workers/go/internal/types"
)

func RpcClient(workflowOut chan types.EventMessage) *rpc.RpcClient {
	return rpc.NewRpcClient(workflowOut)
}
