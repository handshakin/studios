# Studios at Parkway — site rebuild

Plain static HTML/CSS. No build step, no framework, no dependencies.

## Structure
- index.html, forms.html, operating-documents.html, businesses.html, contact.html — top-level pages
- blog/ — blog index + 4 posts
- assets/style.css — all styling
- build.py — regenerates every page from the content defined inside it (used to build this from the live site's original text; not required to just host the site)

## Still needed (see build.py's OPERATING DOCS section and businesses.html)
- Real photos (currently placeholder frames)
- The 3 legal PDFs for Operating Documents (currently placeholder links under /documents/)
- Confirm Businesses page + blog completeness with Jason

## Hosting
Once pushed to GitHub: Settings → Pages → Deploy from branch → main /(root). Point studiosatparkway.com's DNS at GitHub Pages when ready to cut over (not done yet — this is still a draft).
