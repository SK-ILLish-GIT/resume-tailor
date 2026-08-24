#!/usr/bin/env bash
set -euo pipefail

BUILD_DIR="${1:?Build directory required}"
OUTPUT_PDF="${2:?Output PDF path required}"

IMAGE_NAME="${RESUME_TEX_IMAGE:-resume-tailor-tex}"

mkdir -p "$(dirname "$OUTPUT_PDF")"
BUILD_DIR="$(cd "$BUILD_DIR" && pwd)"

CONTAINER="$(docker create -w /work "${IMAGE_NAME}" sh -c \
  'latexmk -C >/dev/null 2>&1; latexmk -pdf -interaction=nonstopmode -f -output-directory=/work /work/main.tex; test -f /work/main.pdf')"

cleanup() {
  docker rm -f "${CONTAINER}" >/dev/null 2>&1 || true
}
trap cleanup EXIT

docker cp "${BUILD_DIR}/." "${CONTAINER}:/work/" >/dev/null

docker start -a "${CONTAINER}" >/dev/null || true

if ! docker cp "${CONTAINER}:/work/main.pdf" "${OUTPUT_PDF}" 2>/dev/null; then
  echo "LaTeX build failed: main.pdf not produced" >&2
  docker cp "${CONTAINER}:/work/main.log" - 2>/dev/null | tail -40 >&2 || true
  exit 1
fi

echo "PDF written to ${OUTPUT_PDF}"
