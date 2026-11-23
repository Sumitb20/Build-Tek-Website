/**
 * BuildTek Events — Official Media Partner Popup: BioSeedin JPM 2027
 * Injected across all website pages
 * Target: https://www.bioseedin.com/JPM2027/#/home?origin=buildtekevent
 */
(function() {
  // Prevent duplicate injection
  if (document.getElementById('bioseedin-partner-popup-wrap')) return;

  // Check if dismissed in this session
  if (sessionStorage.getItem('bioseedin_popup_dismissed') === 'true') return;

  const targetUrl = 'https://www.bioseedin.com/JPM2027/#/home?origin=buildtekevent';

  const styles = `
    #bioseedin-partner-popup-wrap {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 999999;
      max-width: 390px;
      width: calc(100vw - 32px);
      opacity: 0;
      transform: translateY(24px) scale(0.97);
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      pointer-events: none;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Inter, Helvetica, Arial, sans-serif;
    }
    #bioseedin-partner-popup-wrap.active {
      opacity: 1;
      transform: translateY(0) scale(1);
      pointer-events: auto;
    }
    .bioseedin-card {
      background: rgba(9, 14, 28, 0.96);
      border: 1px solid rgba(0, 240, 255, 0.4);
      border-radius: 14px;
      padding: 18px 20px 20px;
      box-shadow: 0 18px 50px rgba(0, 0, 0, 0.85), 0 0 28px rgba(0, 240, 255, 0.18), inset 0 1px 0 rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      position: relative;
      overflow: hidden;
    }
    .bioseedin-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, #00f0ff 0%, #7c3aed 50%, #f59e0b 100%);
    }
    .bioseedin-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
    }
    .bioseedin-badge {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #00f0ff;
      background: rgba(0, 240, 255, 0.12);
      border: 1px solid rgba(0, 240, 255, 0.35);
      border-radius: 99px;
      padding: 3px 9px;
    }
    .bioseedin-badge-dot {
      width: 6px;
      height: 6px;
      background: #00f0ff;
      border-radius: 50%;
      box-shadow: 0 0 8px #00f0ff;
      animation: bioseedin-pulse 2s infinite;
    }
    @keyframes bioseedin-pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }
    .bioseedin-close-btn {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #94a3b8;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 14px;
      line-height: 1;
      transition: all 0.2s ease;
      padding: 0;
    }
    .bioseedin-close-btn:hover {
      background: rgba(239, 68, 68, 0.25);
      border-color: rgba(239, 68, 68, 0.5);
      color: #fca5a5;
    }
    .bioseedin-title {
      font-size: 15px;
      font-weight: 700;
      color: #ffffff;
      margin: 0 0 6px 0;
      line-height: 1.35;
      letter-spacing: -0.01em;
    }
    .bioseedin-desc {
      font-size: 12px;
      color: #cbd5e1;
      line-height: 1.5;
      margin: 0 0 14px 0;
    }
    .bioseedin-cta-btn {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      width: 100%;
      box-sizing: border-box;
      padding: 10px 14px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      text-decoration: none;
      color: #070a14;
      background: linear-gradient(135deg, #00f0ff 0%, #38bdf8 100%);
      border: none;
      border-radius: 8px;
      box-shadow: 0 4px 16px rgba(0, 240, 255, 0.35);
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .bioseedin-cta-btn:hover {
      background: linear-gradient(135deg, #38bdf8 0%, #00f0ff 100%);
      box-shadow: 0 6px 22px rgba(0, 240, 255, 0.55);
      transform: translateY(-1px);
      color: #070a14;
    }
    @media (max-width: 640px) {
      #bioseedin-partner-popup-wrap {
        bottom: 74px; /* avoid overlapping mobile sticky CTA bar */
        right: 16px;
        left: 16px;
        width: auto;
      }
      .bioseedin-card {
        padding: 14px 16px 16px;
      }
      .bioseedin-title {
        font-size: 14px;
      }
      .bioseedin-desc {
        font-size: 11.5px;
        margin-bottom: 12px;
      }
    }
  `;

  function initPopup() {
    const styleEl = document.createElement('style');
    styleEl.innerHTML = styles;
    document.head.appendChild(styleEl);

    const wrap = document.createElement('div');
    wrap.id = 'bioseedin-partner-popup-wrap';
    wrap.setAttribute('role', 'dialog');
    wrap.setAttribute('aria-label', 'Official Media Partner Announcement');

    wrap.innerHTML = `
      <div class="bioseedin-card">
        <div class="bioseedin-header">
          <div class="bioseedin-badge">
            <span class="bioseedin-badge-dot"></span>
            Official Media Partner
          </div>
          <button type="button" class="bioseedin-close-btn" id="bioseedin-close-btn" aria-label="Dismiss Announcement">✕</button>
        </div>
        <h4 class="bioseedin-title">BioSeedin Global Conclave @ JPM 2027</h4>
        <p class="bioseedin-desc">
          BuildTek Events is proud to be the official media partner for BioSeedin JPM 2027. Connect with 1,000+ global biotech innovators, pharmaceutical leaders &amp; venture partners.
        </p>
        <a href="${targetUrl}" target="_blank" rel="noopener noreferrer" class="bioseedin-cta-btn" id="bioseedin-cta-link">
          Explore Event &amp; Partnering →
        </a>
      </div>
    `;

    document.body.appendChild(wrap);

    // Show after slight delay
    setTimeout(() => {
      wrap.classList.add('active');
    }, 1500);

    // Event listeners
    const closeBtn = document.getElementById('bioseedin-close-btn');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        wrap.classList.remove('active');
        sessionStorage.setItem('bioseedin_popup_dismissed', 'true');
        setTimeout(() => wrap.remove(), 400);
      });
    }

    const ctaLink = document.getElementById('bioseedin-cta-link');
    if (ctaLink) {
      ctaLink.addEventListener('click', () => {
        sessionStorage.setItem('bioseedin_popup_dismissed', 'true');
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPopup);
  } else {
    initPopup();
  }
})();
