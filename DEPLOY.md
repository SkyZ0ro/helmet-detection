# Deployment Instructions

## 0. Automated Setup
- Run the setup script:
  ```bash
  ./setup_repo.sh
  ```
- This will:
  - Initialize git repository
  - Create .gitignore
  - Set up basic directory structure

## 1. GitHub Setup

1. Create new repository on GitHub
2. If not using automated setup, initialize manually:
```bash
git init
git remote add origin [your-github-repo-url]
```

3. Create .gitignore file to exclude large files:
```bash
cat > .gitignore <<EOL
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
```

## 2. Yandex Disk for Large Files

1. Upload model files to Yandex Disk:
   - Create folder "helmet-detection-models"
   - Upload your model files (.pt, .pth)

2. Get shareable links:
   - Right-click on file → "Share"
   - Copy public link

3. Add download instructions to README.md:
```markdown
## Model Download

Download pretrained models from Yandex Disk:

- [Faster R-CNN Model](your-link-here)
- [YOLOv8 Model](your-link-here)

Place downloaded models in `models/` directory
```

## 3. First Commit

If using automated setup:
```bash
./setup_repo.sh
```

Manual setup:
```bash
# Configure Git user if needed
git config user.email "your@email.com"
git config user.name "Your Name"

# Make first commit
git add .
git commit -m "Initial commit"
git push -u origin main
```

## 4. GitHub Repository Setup

1. Create new repository on GitHub (without README/license)
2. Set remote and push:
```bash
git remote add origin https://github.com/your-username/helmet-detection.git
git push -u origin main
```

## 5. For Collaborators

1. Clone repository:
```bash
git clone https://github.com/your-username/helmet-detection.git
```

2. Download models from Yandex Disk
3. Place models in correct directory
4. Install requirements:
```bash
pip install -r requirements.txt