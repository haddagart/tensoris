#!/usr/bin/env bash

# ==============================================================================
# Tensoris Interactive Release & Versioning Automation Script
# ==============================================================================
# Branching Architecture Strategy:
#   • 'working' : Primary development workspace where all daily coding occurs.
#   • 'dev'     : Exclusively for Pre-Releases (alpha, beta, rc).
#   • 'main'    : Exclusively for Official Stable Releases.
#   • 'release/vX' : Major version release tracking branch.
#
# Execution Flow:
# 1. Auto-formats code & runs local verification (Ruff, Pytest, Docs, PyPI build).
# 2. Displays detailed release execution plan.
# 3. Prompts user for explicit confirmation before committing/branching/pushing.
# 4. Merges 'working' branch into 'dev' or 'main', tags PEP 440 release,
#    deploys mike multi-version docs, and returns to 'working' branch.
#
# Usage:
#   ./release.sh <VERSION>
# Examples:
#   ./release.sh 1.0.0b1       # Pre-release (merges working -> dev)
#   ./release.sh 1.0.0         # Stable release (merges working -> main)
# ==============================================================================

set -euo pipefail

# ------------------------------------------------------------------------------
# 1. Helper Functions & Colors
# ------------------------------------------------------------------------------
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

info() { echo -e "${BLUE}[INFO]${NC} $1"; }
success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; exit 1; }

# ------------------------------------------------------------------------------
# 2. Input Validation & Workspace Setup
# ------------------------------------------------------------------------------
if [[ $# -ne 1 || "$1" == "-h" || "$1" == "--help" ]]; then
    echo "Usage: ./release.sh <VERSION>"
    echo ""
    echo "Branching Policy:"
    echo "  • 'working' branch is the primary workspace for all daily development."
    echo "  • 'dev', 'main', and 'release/vX' branches are reserved strictly for releases."
    echo ""
    echo "Examples:"
    echo "  ./release.sh 1.0.0a1    (Alpha pre-release)"
    echo "  ./release.sh 1.0.0b1    (Beta pre-release)"
    echo "  ./release.sh 1.0.0rc1   (Release Candidate)"
    echo "  ./release.sh 1.0.0      (Stable Official Release)"
    exit 0
fi

INPUT_VER="$1"
RAW_VER="${INPUT_VER#v}"
TAG="v${RAW_VER}"

# Ensure 'working' branch exists and is checked out
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

if ! git rev-parse --verify working >/dev/null 2>&1; then
    info "Creating primary development branch 'working'..."
    git checkout -b working
elif [[ "$CURRENT_BRANCH" != "working" ]]; then
    info "Switching to primary development branch 'working'..."
    git checkout working
fi

# ------------------------------------------------------------------------------
# 3. PEP 440 & Branch Resolution
# ------------------------------------------------------------------------------
MAJOR_NUM=$(echo "$RAW_VER" | cut -d'.' -f1)
MAJOR_BRANCH="release/v${MAJOR_NUM}"

if [[ "$RAW_VER" =~ [a-zA-Z] ]]; then
    IS_PRERELEASE=true
    REL_TYPE="Pre-Release (PEP 440)"
    TARGET_BRANCH="dev"
else
    IS_PRERELEASE=false
    REL_TYPE="Stable Official Release"
    TARGET_BRANCH="main"
fi

# ------------------------------------------------------------------------------
# 4. Local Pre-Commit Verification (Simulating GitHub Actions)
# ------------------------------------------------------------------------------
echo -e "\n${BOLD}${CYAN}======================================================================${NC}"
echo -e "${BOLD}${CYAN} 🧪 Step 1: Running Auto-Formatting & Local CI Verification Checks ${NC}"
echo -e "${BOLD}${CYAN}======================================================================${NC}\n"

info "1/5 Auto-formatting code & sorting imports (ruff)..."
uv run ruff format . >/dev/null 2>&1 || true
uv run ruff check --fix . >/dev/null 2>&1 || true
success "Code formatting & import sorting completed."

info "2/5 Running Ruff Linter Verification..."
uv run ruff check . || error "Ruff linting failed! Fix errors before releasing."
success "Ruff linter passed cleanly."

info "3/5 Running Pytest Unit Test Suite..."
uv run pytest tests/unit || error "Unit tests failed! Fix test assertions before releasing."
success "All unit tests passed."

info "4/5 Verifying Documentation Build (properdocs)..."
uv run properdocs build --site-dir site || error "Documentation build failed! Fix mkdocs/docstrings."
success "Documentation build verified."

info "5/5 Verifying PyPI Distribution Package Build (uv build)..."
uv build || error "PyPI build failed! Check pyproject.toml configuration."
success "PyPI package build verified."

echo -e "\n${BOLD}${GREEN}✔ All local CI verification tests passed successfully!${NC}\n"

# ------------------------------------------------------------------------------
# 5. Display Release Plan & Prompt User Confirmation
# ------------------------------------------------------------------------------
echo -e "${BOLD}${YELLOW}======================================================================${NC}"
echo -e "${BOLD}${YELLOW} 📋 Step 2: Proposed Release Execution Plan ${NC}"
echo -e "${BOLD}${YELLOW}======================================================================${NC}"
echo -e "  • ${BOLD}Target Version:${NC}      ${RAW_VER}"
echo -e "  • ${BOLD}Git Release Tag:${NC}     ${TAG}"
echo -e "  • ${BOLD}Release Type:${NC}        ${REL_TYPE}"
echo -e "  • ${BOLD}Source Branch:${NC}       working"
echo -e "  • ${BOLD}Target Branch:${NC}       ${TARGET_BRANCH}"
echo -e "  • ${BOLD}Major Release Branch:${NC} ${MAJOR_BRANCH}"
echo -e "${YELLOW}----------------------------------------------------------------------${NC}"
echo -e "${BOLD}Actions to be executed:${NC}"
if [[ "$IS_PRERELEASE" == true ]]; then
    echo -e "  1. Stage working changes & commit on 'working' branch ('CHORE: Prepare release for ${TAG}')"
    echo -e "  2. Ensure release branches ('dev' and '${MAJOR_BRANCH}') exist"
    echo -e "  3. Merge 'working' branch into 'dev'"
    echo -e "  4. Create annotated git tag '${TAG}' on 'dev'"
    echo -e "  5. Push 'dev', 'working', '${MAJOR_BRANCH}', and tag '${TAG}' to remote (origin)"
    echo -e "  6. Deploy multi-version documentation under 'dev' alias via mike"
    echo -e "  7. Return active git branch to 'working'"
else
    echo -e "  1. Stage working changes & commit on 'working' branch"
    echo -e "  2. Checkout 'main' and merge 'working' into 'main'"
    echo -e "  3. Also merge 'working' into 'dev'"
    echo -e "  4. Create/update major version branch '${MAJOR_BRANCH}'"
    echo -e "  5. Create annotated git tag '${TAG}' on branch 'main'"
    echo -e "  6. Push 'main', 'dev', 'working', '${MAJOR_BRANCH}', and tag '${TAG}' to remote (origin)"
    echo -e "  7. Deploy multi-version documentation under '${RAW_VER}' and set 'latest' alias"
    echo -e "  8. Return active git branch to 'working'"
fi
echo -e "${BOLD}${YELLOW}======================================================================${NC}\n"

read -p "Do you want to execute these release steps now? [y/N]: " CONFIRM
case "$CONFIRM" in
    [yY][eE][sS]|[yY])
        info "User confirmed. Proceeding with release execution..."
        ;;
    *)
        warn "Release execution cancelled by user. No git changes or pushes were made."
        exit 0
        ;;
esac

# ------------------------------------------------------------------------------
# 6. Execute Release Workflow
# ------------------------------------------------------------------------------
echo -e "\n${BOLD}${BLUE}======================================================================${NC}"
echo -e "${BOLD}${BLUE} 🚀 Step 3: Executing Git Release & Deployment ${NC}"
echo -e "${BOLD}${BLUE}======================================================================${NC}\n"

# Stage & Commit working directory changes on working branch
if [[ -n $(git status --porcelain) ]]; then
    info "Staging working changes on 'working' branch and creating release commit..."
    git add .
    git commit -m "CHORE: Prepare release for ${TAG}" || true
fi

# Ensure Major Version Branch exists locally
if ! git rev-parse --verify "${MAJOR_BRANCH}" >/dev/null 2>&1; then
    info "Creating major release branch '${MAJOR_BRANCH}'..."
    git branch "${MAJOR_BRANCH}"
fi

if [[ "$IS_PRERELEASE" == true ]]; then
    # --- Pre-release Workflow (working -> dev) ---
    info "Merging 'working' branch into 'dev' for pre-release..."
    if ! git rev-parse --verify dev >/dev/null 2>&1; then
        git checkout -b dev
    else
        git checkout dev
    fi
    git merge working -m "MERGE: Integrate working branch into dev for ${TAG}" || true

    if git rev-parse "${TAG}" >/dev/null 2>&1; then
        warn "Tag '${TAG}' already exists locally. Overwriting tag..."
        git tag -d "${TAG}"
    fi
    git tag -a "${TAG}" -m "RELEASE: ${TAG}"

    info "Pushing 'dev', 'working', '${MAJOR_BRANCH}', and tag '${TAG}' to origin..."
    git push origin dev working --tags -f
    git push origin "HEAD:${MAJOR_BRANCH}" -f

    info "Fetching gh-pages and deploying multi-version documentation for 'dev'..."
    git fetch origin gh-pages:gh-pages 2>/dev/null || true
    uv run mike deploy --push --force --ignore-remote-status --update-aliases dev

else
    # --- Stable Release Workflow (working -> main & dev) ---
    info "Merging 'working' branch into 'main' and 'dev'..."
    
    # Merge into main
    git checkout main
    git pull origin main || true
    git merge working -m "MERGE: Integrate working branch into main for ${TAG}" || true

    # Sync dev branch as well
    if git rev-parse --verify dev >/dev/null 2>&1; then
        git checkout dev
        git merge working -m "MERGE: Integrate working branch into dev for ${TAG}" || true
        git checkout main
    fi

    # Sync Major Branch
    git checkout "${MAJOR_BRANCH}" || git checkout -b "${MAJOR_BRANCH}"
    git merge main -m "MERGE: Update ${MAJOR_BRANCH} with ${TAG}" || true
    git checkout main

    if git rev-parse "${TAG}" >/dev/null 2>&1; then
        warn "Tag '${TAG}' already exists locally. Overwriting tag..."
        git tag -d "${TAG}"
    fi
    git tag -a "${TAG}" -m "RELEASE: ${TAG}"

    info "Pushing 'main', 'dev', 'working', '${MAJOR_BRANCH}', and tag '${TAG}' to origin..."
    git push origin main dev working --tags -f
    git push origin "main:${MAJOR_BRANCH}" -f

    info "Fetching gh-pages and deploying multi-version documentation for '${RAW_VER}' and setting 'latest' alias..."
    git fetch origin gh-pages:gh-pages 2>/dev/null || true
    uv run mike deploy --push --force --ignore-remote-status --update-aliases "${RAW_VER}" latest
    uv run mike set-default --push --force latest
fi

# Always return developer workspace to 'working' branch
info "Returning active git branch to 'working'..."
git checkout working

success "======================================================================"
success " Release ${TAG} successfully executed and published!"
success " Active development branch set to 'working'."
success " GitHub Actions pipeline will now handle PyPI and GitHub Releases."
success "======================================================================"
