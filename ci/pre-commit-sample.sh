#!/usr/bin/env bash
# Sample Git pre-commit hook for local Magnetar Canon Compliance
# Install by copying to .git/hooks/pre-commit and making executable:
#   cp ci/pre-commit-sample.sh .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit

echo "Running Magnetar Canon compliance check..."
python3 scripts/magnetar_check.py --strict
if [ $? -ne 0 ]; then
  echo "Commit rejected: Repository does not satisfy Magnetar Canon compliance."
  exit 1
fi
