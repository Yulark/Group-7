#!/bin/bash
# =========================================================
# Despite Group Access Control System - Unix/Mac/Linux Launcher
# =========================================================
# Run: bash start.sh
# Or: chmod +x start.sh && ./start.sh

set -e

cd "$(dirname "$0")"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo ""
echo "========================================================="
echo "  DESPITE GROUP ACCESS CONTROL SYSTEM v2.0"
echo "  $(uname) Launcher"
echo "========================================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR]${NC} Python 3 is not installed"
    echo ""
    echo "Install Python 3.8+ using:"
    echo "  macOS:   brew install python3"
    echo "  Ubuntu:  sudo apt-get install python3 python3-venv"
    echo "  Fedora:  sudo dnf install python3"
    echo ""
    exit 1
fi

echo -e "${GREEN}[OK]${NC} Python found"
python3 --version

echo ""
echo -e "${BLUE}[*]${NC} Checking virtual environment..."

# Check if venv exists
if [ ! -d "venv" ]; then
    echo -e "${BLUE}[*]${NC} Virtual environment not found. Creating..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo -e "${RED}[ERROR]${NC} Failed to create virtual environment"
        exit 1
    fi
    echo -e "${GREEN}[OK]${NC} Virtual environment created"
fi

echo ""
echo -e "${BLUE}[*]${NC} Activating virtual environment..."
source venv/bin/activate
echo -e "${GREEN}[OK]${NC} Virtual environment activated"

echo ""
echo -e "${BLUE}[*]${NC} Installing dependencies..."
pip install -q --upgrade pip 2>/dev/null || true
pip install -q -r requirements.txt 2>/dev/null || echo -e "${YELLOW}[WARNING]${NC} Some dependencies may be missing"
echo -e "${GREEN}[OK]${NC} Dependencies ready"

echo ""
echo "========================================================="
echo -e "  ${GREEN}[OK] READY TO START${NC}"
echo "========================================================="
echo ""
echo "Server Details:"
echo "  URL: http://localhost:5000"
echo "  Status: Starting..."
echo ""
echo "Demo Credentials:"
echo "  - alice / securePass123 (Creator)"
echo "  - bob / adminPass456 (Admin)"
echo "  - diana / pr_manager123 (PR_Manager)"
echo "  - charlie / analyst789 (Analyst)"
echo ""
echo -e "${YELLOW}[!] Press CTRL+C to stop the server${NC}"
echo ""
echo "========================================================="
echo ""

# Start the application
python run_server.py

# If we get here, server stopped
echo ""
echo "========================================================="
echo "Server stopped."
echo "========================================================="
