module github.com/FatsharkStudiosAB/haja-workers/go/worker

go 1.23.1

require github.com/joho/godotenv v1.5.1

require (
	github.com/dlclark/regexp2 v1.10.0 // indirect
	github.com/google/go-cmp v0.7.0 // indirect
	github.com/google/uuid v1.6.0 // indirect
	github.com/pkoukk/tiktoken-go v0.1.6 // indirect
	github.com/spaolacci/murmur3 v1.1.0 // indirect
	github.com/stretchr/testify v1.10.0 // indirect
	github.com/tmc/langchaingo v0.1.13 // indirect
	golang.org/x/net v0.25.0 // indirect
	golang.org/x/sys v0.27.0 // indirect
	golang.org/x/text v0.20.0 // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20240604185151-ef581f913117 // indirect
	google.golang.org/protobuf v1.34.1 // indirect
)

require (
	github.com/FatsharkStudiosAB/haja-workers/go/internal v0.0.0
	github.com/FatsharkStudiosAB/haja-workers/go/sdk v0.0.0
	google.golang.org/grpc v1.64.0
)

replace github.com/FatsharkStudiosAB/haja-workers/go/sdk => ../../sdk

replace github.com/FatsharkStudiosAB/haja-workers/go/internal => ../../internal
