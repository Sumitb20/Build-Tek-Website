import re

with open('pharma-vista.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Head Styles
style_addition = """
    /* --- Media Partner Logos & Cards --- */
    .media-partners-strip {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1.5rem;
      flex-wrap: wrap;
      padding: 1.25rem 2rem;
      position: relative;
      z-index: 10;
      width: 100%;
    }
    .media-partners-label {
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 2.5px;
      color: rgba(255, 255, 255, 0.75);
      font-weight: 600;
      margin-right: 0.5rem;
    }
    .media-partners-grid {
      display: flex;
      align-items: center;
      gap: 1.25rem;
      flex-wrap: wrap;
      justify-content: center;
    }
    .media-partner-card {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.9);
      border-radius: 12px;
      padding: 10px 24px;
      min-height: 54px;
      min-width: 140px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
      transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
      text-decoration: none;
    }
    .media-partner-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
      border-color: var(--accent-teal);
    }
    .media-partner-logo {
      max-height: 32px;
      width: auto;
      max-width: 160px;
      object-fit: contain;
      display: block;
    }

    /* --- Summit Agenda BST + ET Timeline --- */
    .agenda-inner {
      max-width: 960px;
      margin: 0 auto;
    }
    .tl-item {
      display: grid;
      grid-template-columns: 210px 1fr;
      gap: 2rem;
      align-items: start;
      padding: 1.85rem 0;
      border-top: 1px solid var(--border);
      transition: background-color 0.2s ease;
    }
    .tl-item:hover {
      background-color: rgba(10, 107, 94, 0.02);
    }
    .tl-time-box {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }
    .tl-time-bst {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--accent-teal);
      letter-spacing: 0.3px;
      line-height: 1.3;
    }
    .tl-time-et {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      font-weight: 600;
      color: #b58900;
      letter-spacing: 0.2px;
      line-height: 1.3;
    }
    .tz-label {
      display: inline-block;
      font-size: 0.65rem;
      font-weight: 800;
      padding: 1px 5px;
      border-radius: 4px;
      margin-left: 4px;
      vertical-align: middle;
    }
    .tl-time-bst .tz-label {
      background: rgba(10, 107, 94, 0.12);
      color: var(--accent-teal);
    }
    .tl-time-et .tz-label {
      background: rgba(200, 164, 78, 0.16);
      color: #996e00;
    }
    .tl-tag-keynote {
      color: #0d9488 !important;
      background: rgba(13, 148, 136, 0.12) !important;
      border: 1px solid rgba(13, 148, 136, 0.3) !important;
    }
    .tl-tag-panel {
      color: #6366f1 !important;
      background: rgba(99, 102, 241, 0.12) !important;
      border: 1px solid rgba(99, 102, 241, 0.3) !important;
    }
    .tl-tag-net {
      color: #c9a84c !important;
      background: rgba(201, 168, 76, 0.15) !important;
      border: 1px solid rgba(201, 168, 76, 0.35) !important;
    }
    .tl-tag-open {
      color: #0284c7 !important;
      background: rgba(2, 132, 199, 0.12) !important;
      border: 1px solid rgba(2, 132, 199, 0.3) !important;
    }
    .tl-tag-close {
      color: #d97706 !important;
      background: rgba(217, 119, 6, 0.12) !important;
      border: 1px solid rgba(217, 119, 6, 0.3) !important;
    }
    .tl-speaker-info {
      font-size: 0.9rem;
      color: var(--text-secondary);
      line-height: 1.55;
      margin-top: 0.4rem;
    }
    .tl-speaker-name {
      font-weight: 700;
      color: var(--text-primary);
    }
    .tl-speaker-role {
      color: var(--text-secondary);
    }
    .tl-panel-structure {
      margin-top: 0.75rem;
      padding: 0.9rem 1.25rem;
      background: #fbfbf9;
      border-left: 3px solid var(--accent-teal);
      border-radius: 0 8px 8px 0;
    }
    .tl-role-tag {
      display: inline-block;
      font-size: 0.65rem;
      font-weight: 800;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--accent-teal);
      margin-bottom: 0.35rem;
    }
    .tl-panel-mod {
      margin-bottom: 0.75rem;
      font-size: 0.88rem;
      line-height: 1.5;
    }
    .tl-panel-panellists {
      margin-top: 0.4rem;
    }
    .tl-panellist-list {
      list-style: none;
      padding: 0;
      margin: 0.25rem 0 0;
    }
    .tl-panellist-list li {
      font-size: 0.88rem;
      color: var(--text-secondary);
      line-height: 1.6;
      padding-left: 1rem;
      position: relative;
      margin-bottom: 0.35rem;
    }
    .tl-panellist-list li::before {
      content: "•";
      position: absolute;
      left: 0;
      color: var(--accent-teal);
      font-weight: bold;
      font-size: 1.1rem;
    }
    .tl-panellist-list li strong {
      color: var(--text-primary);
      font-weight: 600;
    }
    .tl-break-item {
      display: grid;
      grid-template-columns: 210px 1fr;
      gap: 2rem;
      align-items: center;
      padding: 1.35rem 0;
      border-top: 1px solid var(--border);
      background: rgba(200, 164, 78, 0.04);
    }
    .tl-break-content {
      display: flex;
      flex-direction: column;
    }

    /* --- Speaker Section Structure Subheaders --- */
    .speaker-category-block {
      margin-bottom: 4rem;
    }
    .speaker-category-block:last-child {
      margin-bottom: 0;
    }
    .speaker-cat-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 1.65rem;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    .speaker-cat-badge {
      font-family: var(--font-sans, sans-serif);
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      padding: 0.2rem 0.65rem;
      border-radius: 20px;
    }
    .badge-keynote-cat {
      background: rgba(13, 148, 136, 0.12);
      color: var(--accent-teal);
      border: 1px solid rgba(13, 148, 136, 0.25);
    }
    .badge-mod-cat {
      background: rgba(99, 102, 241, 0.12);
      color: #6366f1;
      border: 1px solid rgba(99, 102, 241, 0.25);
    }
    .badge-panel-cat {
      background: rgba(200, 164, 78, 0.15);
      color: #92400e;
      border: 1px solid rgba(200, 164, 78, 0.3);
    }
    .speaker-cat-desc {
      font-size: 0.9rem;
      color: var(--text-secondary);
      margin-bottom: 1.75rem;
      line-height: 1.6;
    }
    .avatar-protofine {
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #0b1f3a 0%, #1e3a5f 100%);
      color: #ffffff;
      padding: 2rem;
      text-align: center;
    }
    .avatar-initials {
      width: 84px;
      height: 84px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.1);
      border: 2px solid var(--accent-teal);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 1rem;
    }

    /* Responsive Timeline & Media Partners */
    @media (max-width: 768px) {
      .tl-item, .tl-break-item {
        grid-template-columns: 1fr;
        gap: 0.65rem;
        padding: 1.4rem 0;
      }
      .tl-time-box {
        flex-direction: row;
        flex-wrap: wrap;
        align-items: center;
        gap: 0.4rem 1rem;
        padding-bottom: 0.35rem;
        border-bottom: 1px dashed rgba(0,0,0,0.1);
      }
      .tl-time-bst { font-size: 0.95rem; }
      .tl-time-et { font-size: 0.85rem; }
      .media-partners-strip {
        flex-direction: column;
        gap: 0.85rem;
        padding: 1rem 1rem;
      }
      .media-partners-grid {
        gap: 0.75rem;
        width: 100%;
      }
      .media-partner-card {
        padding: 8px 18px;
        min-height: 48px;
        flex: 1 1 140px;
        max-width: 200px;
      }
      .media-partner-logo {
        max-height: 28px;
        max-width: 130px;
      }
    }
    @media (max-width: 480px) {
      .media-partners-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.65rem;
        width: 100%;
      }
      .media-partner-card {
        width: 100%;
        max-width: none;
        padding: 8px 12px;
        min-height: 46px;
      }
      .media-partner-logo {
        max-height: 24px;
        max-width: 110px;
      }
    }
"""

if '</style>' in html:
    html = html.replace('</style>', style_addition + '\n  </style>', 1)
    print("Added styles")

with open('pharma-vista.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated pharma-vista.html styles")
