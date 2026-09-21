#!/bin/bash

# Runtime directory relative to the Pixi project
export XDG_RUNTIME_DIR="${PIXI_PROJECT_ROOT}/.runtime"

mkdir -p "$XDG_RUNTIME_DIR"
chmod 700 "$XDG_RUNTIME_DIR"

