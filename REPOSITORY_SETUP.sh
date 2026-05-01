#!/bin/bash

# DiJones Training Repository Setup Script
# Run this after creating the repository on GitHub

echo "🚀 DiJones Training Repository Setup"
echo "======================================"
echo ""

# Check if we're in the right directory
if [ ! -f "README.md" ]; then
    echo "❌ Error: README.md not found. Are you in the dijones-training-repo folder?"
    exit 1
fi

echo "✅ Found training repository files"
echo ""

# Initialize git if needed
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git branch -M main
    echo "✅ Git initialized"
else
    echo "✅ Git already initialized"
fi

echo ""
echo "📝 Next steps:"
echo ""
echo "1. Create repository on GitHub:"
echo "   - Go to https://github.com/organizations/DiJonesBusinessSolutions/repositories/new"
echo "   - Name: dijones-training-repo"
echo "   - Description: Developer training for Business Solutions team"
echo "   - Private (recommended)"
echo "   - Do NOT initialize with README (we have one)"
echo ""
echo "2. Connect this folder to GitHub:"
echo "   git remote add origin https://github.com/DiJonesBusinessSolutions/dijones-training-repo.git"
echo ""
echo "3. Push to GitHub:"
echo "   git add ."
echo "   git commit -m 'Initial commit: Training course materials'"
echo "   git push -u origin main"
echo ""
echo "4. Configure repository:"
echo "   - Settings → Manage access → Add Business Solutions team (Read)"
echo "   - Settings → General → Enable Discussions (optional)"
echo "   - Settings → General → Allow forking"
echo ""
echo "5. Announce to team:"
echo "   - Share repository URL"
echo "   - Send QUICKSTART.md to new students"
echo "   - Schedule kickoff meeting"
echo ""
echo "📚 Documentation:"
echo "   - QUICKSTART.md - For students (send this first!)"
echo "   - docs/SETUP.md - Detailed setup guide"
echo "   - docs/TEAM_LEAD.md - Your implementation guide"
echo ""
echo "🎉 Ready to launch! Good luck with the program!"
