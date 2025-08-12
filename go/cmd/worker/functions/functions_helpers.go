package functions

import (
	"github.com/FatsharkStudiosAB/haja-workers/go/internal/basefunction"
	"github.com/FatsharkStudiosAB/haja-workers/go/internal/state"
	"github.com/FatsharkStudiosAB/haja-workers/go/internal/types"
)

func GetFunction(gs *state.GlobalState, functionName string, version string) (basefunction.FunctionInterface, bool) {
	identifier := types.FunctionKey(gs.ServerName, functionName, version)
	return gs.Functions.Load(identifier)
}

func GetIdentifier(functionName string, version string) string { return functionName + "|" + version }
