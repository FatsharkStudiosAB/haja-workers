package main

import (
	"log"

	worker "github.com/FatsharkStudiosAB/haja-workers/go"
	"github.com/FatsharkStudiosAB/haja-workers/go/cmd/worker/examples"

	"github.com/joho/godotenv"
)

func main() {
	err := godotenv.Load()
	if err != nil {
		log.Println("Error loading .env file")
	}

	// Create server with custom configuration
	server, err := worker.New()
	if err != nil {
		log.Fatal("Failed to create server:", err)
	}

	// Register example functions using the SDK interface
	server.RegisterFunction(examples.InputFunction())
	server.RegisterFunction(examples.StoreChatHistoryFunction())

	// Start server (this will handle all initialization and block forever)
	log.Println("Starting server with SDK...")
	if err := server.Start(); err != nil {
		log.Fatal("Server failed:", err)
	}
}
