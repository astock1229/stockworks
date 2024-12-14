# Tech Blog

A personal blog documenting coding, machine learning, and AI projects using Pelican static site generator.

## Setup Instructions

1. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create new content:
- Add Markdown files to the `content` directory
- Add images to `content/images`
- Configure site settings in `pelicanconf.py`

4. Build the site:
```bash
pelican content
```

5. Preview locally:
```bash
pelican --listen
```

6. Deploy to GitHub Pages:
```bash
ghp-import output -b gh-pages
git push origin gh-pages
```
