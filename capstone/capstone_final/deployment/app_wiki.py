import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Someprototype Wiki",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;600;700&display=swap');

/* ── Global resets ── */
html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
}

/* ── Hide default Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="collapsedControl"] { display: none; }

/* ── Responsive page wrapper ── */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 3rem !important;
    padding-left: clamp(1rem, 6vw, 6rem) !important;
    padding-right: clamp(1rem, 6vw, 6rem) !important;
    max-width: 1280px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    box-sizing: border-box !important;
}

/* ── Banner / Header ── */
.wiki-banner {
    background: linear-gradient(135deg, #0d1117 0%, #161b22 40%, #0d1523 100%);
    border-bottom: 1px solid #21262d;
    border-radius: 0 0 12px 12px;
    padding: clamp(1.5rem, 4vw, 2.5rem) clamp(1.25rem, 4vw, 2.5rem) clamp(1.25rem, 3vw, 1.75rem);
    margin: 0 0 2rem 0;
    position: relative;
    overflow: hidden;
}

.wiki-banner::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background:
        radial-gradient(ellipse 60% 80% at 80% 50%, rgba(88, 166, 255, 0.07) 0%, transparent 70%),
        radial-gradient(ellipse 40% 60% at 20% 80%, rgba(63, 185, 80, 0.05) 0%, transparent 60%);
    pointer-events: none;
}

.wiki-banner::after {
    content: '{ }';
    position: absolute;
    right: clamp(1rem, 4vw, 2.5rem);
    top: 50%;
    transform: translateY(-50%);
    font-family: 'IBM Plex Mono', monospace;
    font-size: clamp(2.5rem, 6vw, 5rem);
    font-weight: 600;
    color: rgba(88, 166, 255, 0.06);
    letter-spacing: -0.05em;
    pointer-events: none;
}

.banner-eyebrow {
    font-family: 'IBM Plex Mono', monospace;
    font-size: clamp(0.55rem, 1.2vw, 0.65rem);
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #3fb950;
    margin-bottom: 0.6rem;
}

.banner-title {
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: clamp(1.5rem, 4vw, 2.25rem);
    font-weight: 700;
    color: #e6edf3;
    letter-spacing: -0.02em;
    line-height: 1.15;
    margin-bottom: 0.5rem;
}

.banner-title span {
    color: #58a6ff;
}

.banner-subtitle {
    font-size: clamp(0.8rem, 1.8vw, 0.9rem);
    font-weight: 300;
    color: #8b949e;
    max-width: 540px;
    line-height: 1.6;
}

.banner-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-top: 1.25rem;
}

.banner-badge {
    font-family: 'IBM Plex Mono', monospace;
    font-size: clamp(0.6rem, 1.2vw, 0.7rem);
    background: rgba(88, 166, 255, 0.1);
    color: #58a6ff;
    border: 1px solid rgba(88, 166, 255, 0.25);
    border-radius: 20px;
    padding: 0.2rem 0.75rem;
    letter-spacing: 0.04em;
    white-space: nowrap;
}

/* ── Content cards ── */
.content-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(min(100%, 260px), 1fr));
    gap: 1rem;
    margin-top: 0.5rem;
}

.wiki-card {
    display: block;
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 10px;
    padding: clamp(1rem, 2vw, 1.25rem) clamp(1rem, 2vw, 1.5rem);
    transition: border-color 0.2s ease, transform 0.2s ease;
    cursor: pointer;
    text-decoration: none;
}

.wiki-card:hover {
    border-color: #58a6ff;
    transform: translateY(-2px);
}

.wiki-card, .wiki-card:hover, .wiki-card:visited, .wiki-card:active,
a.wiki-card, a.wiki-card:hover, a.wiki-card:visited, a.wiki-card:active {
    text-decoration: none !important;
    color: inherit;
}

.card-icon {
    font-size: clamp(1.25rem, 2.5vw, 1.5rem);
    margin-bottom: 0.6rem;
}

.card-title {
    font-size: clamp(0.85rem, 1.6vw, 0.95rem);
    font-weight: 600;
    color: #e6edf3;
    margin-bottom: 0.35rem;
}

.card-desc {
    font-size: clamp(0.75rem, 1.4vw, 0.8rem);
    color: #8b949e;
    line-height: 1.55;
}

/* ── Section heading ── */
.section-heading {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #484f58;
    margin-bottom: 0.75rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #21262d;
}

/* ── Recent updates ── */
.update-item {
    display: flex;
    align-items: flex-start;
    gap: 0.85rem;
    padding: 0.75rem 0;
    border-bottom: 1px solid #161b22;
}

.update-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #3fb950;
    margin-top: 5px;
    flex-shrink: 0;
}

.update-title {
    font-size: clamp(0.8rem, 1.5vw, 0.875rem);
    color: #c9d1d9;
    font-weight: 500;
}

.update-meta {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    color: #484f58;
    margin-top: 2px;
}

/* ── Mobile breakpoint ── */
@media (max-width: 600px) {
    .wiki-banner::after { display: none; }
    .content-grid { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)

# ── Banner ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="wiki-banner">
    <div class="banner-eyebrow">● Documentation</div>
    <div class="banner-title">Someprototype <span>Wiki</span></div>
    <div class="banner-subtitle">
        A centralized knowledge base, FAQ for fictional company called Someprototype. 
        Built with Streamlit to demonstrate a clean, modern design for internal documentation and onboarding as part of a capstone project.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Browse Topics ──────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">Browse Topics</div>', unsafe_allow_html=True)

st.markdown("""
<div class="content-grid">
    <a class="wiki-card" href="access_requests.html" target="_blank">
        <div class="card-title">Access Requests</div>
        <div class="card-desc">Newhire Onboard, Application access, permission issues, API keys. Start here.</div>
    </a>
    <a class="wiki-card" href="password.html" target="_blank">
        <div class="card-title">Password</div>
        <div class="card-desc">Understand how to reset your password.</div>
    </a>
    <a class="wiki-card" href="network.html" target="_blank">
        <div class="card-title">Network</div>
        <div class="card-desc">Having connectivity issues? Getting a connection error?</div>
    </a>
    <a class="wiki-card" href="hardware.html" target="_blank">
        <div class="card-title">Hardware</div>
        <div class="card-desc">Are you having issues with your laptop, desktop? Trouble printing. This is what you want.</div>
    </a>
    <a class="wiki-card" href="platform.html" target="_blank">
        <div class="card-title">Platform</div>
        <div class="card-desc">Having VM or cloud instance issues. Click here.</div>
    </a>
    <a class="wiki-card" href="security.html" target="_blank">
        <div class="card-title">Security</div>
        <div class="card-desc">Did you get a virus error or suspect a phishing attempt.</div>
    </a>
    <a class="wiki-card" href="software.html" target="_blank">
        <div class="card-title">Software</div>
        <div class="card-desc">All your application issues.</div>
    </a>
    <a class="wiki-card" href="system.html" target="_blank">
        <div class="card-title">System</div>
        <div class="card-desc">Issues with your operating system or system configuration?</div>
    </a>
    <a class="wiki-card" href="other.html" target="_blank">
        <div class="card-title">Other</div>
        <div class="card-desc">Need general assistance or have a question?</div>
    </a>
</div>
""", unsafe_allow_html=True)

# ── Recent Updates ─────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-heading">Recent Updates</div>', unsafe_allow_html=True)

updates = [
    ("Submitted Capstone Report", "2 hours ago · deployment"),
]

updates_html = ""
for title, meta in updates:
    updates_html += f"""
    <div class="update-item">
        <div class="update-dot"></div>
        <div>
            <div class="update-title">{title}</div>
            <div class="update-meta">{meta}</div>
        </div>
    </div>
    """
st.markdown(updates_html, unsafe_allow_html=True)
