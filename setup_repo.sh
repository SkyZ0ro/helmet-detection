#!/bin/bash

# 1. Initialize Git repository
echo "Initializing Git repository..."
git init
git branch -M main

# 2. Create basic .gitignore
echo "Creating .gitignore..."
cat > .gitignore << 'EOL'
# Model files
*.pt
*.pth
*.bin

# Data files
*.zip
*.tar.gz

# Environment files
.env
venv/
EOL

# 3. Instructions for Yandex Disk
echo ""
echo "YANDEX DISK UPLOAD INSTRUCTIONS:"
echo "1. Create folder 'helmet-detection-models' on Yandex Disk"
echo "2. Upload your model files:"
echo "   - Models/detectron_best.pth"
echo "   - Models/yolov8m.pt"
echo "3. Get shareable links (Right-click → Share)"
echo "4. Update README.md with download links"

# 4. Configure Git user if needed
if [ -z "$(git config user.email)" ] || [ -z "$(git config user.name)" ]; then
    echo ""
    echo "Git configuration required:"
    read -p "Enter your email for Git: " git_email
    read -p "Enter your name for Git: " git_name
    git config user.email "$git_email"
    git config user.name "$git_name"
fi

# 5. First commit
echo ""
echo "Making initial commit..."
git add .
git commit -m "Initial project setup" || {
    echo "Commit failed - please check git configuration"
    exit 1
}

echo ""
echo "NEXT STEPS:"
echo "1. Create new repository on GitHub"
echo "2. Add remote: git remote add origin [your-github-url]"
echo "3. Push: git push -u origin main"