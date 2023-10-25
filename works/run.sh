#!/bin/bash

# Function to run TCP server
run_tcp_server() {
    local host="$1"
    local port="$2"
    echo "Running TCP server on host $host and port $port..."
    python -m sockets.tcp.server --host "$host" --port "$port"
}

# Function to run TCP client
run_tcp_client() {
    local host="$1"
    local port="$2"
    echo "Running TCP client on host $host and port $port..."
    python -m sockets.tcp.client --host "$host" --port "$port"
}

# Function to run UDP server
run_udp_server() {
    local host="$1"
    local port="$2"
    echo "Running UDP server on host $host and port $port..."
    python -m sockets.udp.server --host "$host" --port "$port"
}

# Function to run UDP client
run_udp_client() {
    local host="$1"
    local port="$2"
    echo "Running UDP client on host $host and port $port..."
    python -m sockets.udp.client --host "$host" --port "$port"
}

# Parse command-line arguments for each command
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        tcp-server)
            run_tcp_server "$2" "$3"
            shift 3
            ;;
        tcp-client)
            run_tcp_client "$2" "$3"
            shift 3
            ;;
        udp-server)
            run_udp_server "$2" "$3"
            shift 3
            ;;
        udp-client)
            run_udp_client "$2" "$3"
            shift 3
            ;;
        *)
            echo "Unknown argument: $1"
            exit 1
            ;;
    esac
done
