#! /usr/bin/env bash

set -eu -o pipefail

if docker help compose &>/dev/null; then
  docker="docker compose"
else
  docker="docker-compose"
fi

files=""
variant=""
args=""

if [ -z "${BUILD:-}" ] && git diff --name-only 0.2.0 | egrep '^((.+\.)?Dockerfile|nodesource\.gpg|poetry-requirements\.txt|poetry\.lock|pyproject\.toml|ui/package.json|ui/package-lock.json|ui/patches/[^/]+\.patch)$' >/dev/null; then
  BUILD=1
fi

if [ -n "${STREAMLIT:-}" ]; then
  variant="streamlit"
fi

if [ -n "${TORCH:-}" ]; then
  if [ -n "${STREAMLIT:-}" ]; then
    echo "Cannot specify both STREAMLIT and TORCH"
    exit 1
  fi
  variant="torch"
fi

# If the user has specified a variant, we add the corresponding compose file to
# the list of compose files to use.
if [ -n "${variant}" ]; then
  files="${files} -f docker-compose.${variant}.yml"
  if [ -n "${BUILD:-}" ]; then
    files="${files} -f docker-compose.build-${variant}.yml"
  fi

# If the user has specified a build, we add the corresponding compose file to
# the list of compose files to use.
elif [ -n "${BUILD:-}" ]; then
  files="${files} -f docker-compose.build.yml"
fi

# If the user has specified a build, we add the --build flag to the docker
# compose command.
if [ -n "${BUILD:-}" ]; then
  args="${args} --build"
fi

# Finally, we run the docker compose command with the list of compose files and
# the list of arguments.``
$docker -f docker-compose.yml $files up $args "$@"