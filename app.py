import streamlit as st
from pathlib import Path
from datetime import date

import base64
import streamlit.components.v1 as components

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(
    page_title="Case File: The Goldi Affair 💌",
    page_icon="💌",
    layout="centered"
)

# -----------------------------
# PATHS (robust)
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
COVER_IMG = BASE_DIR / "assets" / "images" / "goldi.png"
AUDIO_FILE = BASE_DIR / "assets" / "audio" / "harry.mp3"

st.write("BASE_DIR:", BASE_DIR)
st.write("Exists assets?:", (BASE_DIR / "assets").exists())
st.write("Exists images?:", (BASE_DIR / "assets" / "images").exists())
st.write("Exists goldi?:", (BASE_DIR / "assets" / "images" / "goldi.png").exists())
st.write("Images folder contents:", list((BASE_DIR / "assets" / "images").glob("*")) if (BASE_DIR / "assets" / "images").exists() else "NO FOLDER")


# -----------------------------
# AUDIO
# -----------------------------
AUDIO_FILE = BASE_DIR / "assets" / "audio" / "harry.mp3"

if AUDIO_FILE.exists():
    b64 = base64.b64encode(AUDIO_FILE.read_bytes()).decode("utf-8")

    components.html(
        f"""
        <div style="display:flex; gap:10px; margin: 10px 0;">
          <button id="playBtn" style="
              flex:1; padding:12px; border-radius:12px; border:1px solid rgba(255,255,255,0.25);
              background: rgba(255,255,255,0.06); color:white; font-weight:700; cursor:pointer;">
            🔊 Enable Mission Audio
          </button>

          <button id="muteBtn" style="
              flex:1; padding:12px; border-radius:12px; border:1px solid rgba(255,255,255,0.25);
              background: rgba(255,255,255,0.06); color:white; font-weight:700; cursor:pointer;">
            🔇 Mute
          </button>
        </div>

        <audio id="bgAudio" loop>
          <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>

        <script>
          const audio = document.getElementById("bgAudio");

          document.getElementById("playBtn").addEventListener("click", async () => {{
            try {{
              audio.muted = false;
              audio.volume = 0.85;
              await audio.play();
            }} catch (e) {{
              console.log("Play blocked:", e);
              alert("Your browser blocked autoplay. Tap again or check silent mode / site settings.");
            }}
          }});

          document.getElementById("muteBtn").addEventListener("click", () => {{
            audio.pause();
            audio.currentTime = 0;
          }});
        </script>
        """,
        height=90,
    )
else:
    st.warning(f"Audio file not found at: {AUDIO_FILE}")


# -----------------------------
# SIMPLE THEME STYLING
# (kept minimal so it won’t break easily)
# -----------------------------
st.markdown(
    """
    <style>
      .case-title { font-size: 2.1rem; font-weight: 800; margin-bottom: 0.25rem; }
      .case-subtitle { font-size: 1.05rem; opacity: 0.85; margin-top: 0; }
      .case-card {
        border: 1px solid rgba(255,255,255,0.18);
        border-radius: 18px;
        padding: 18px 18px 10px 18px;
        background: rgba(255,255,255,0.04);
        margin-top: 14px;
      }
      .label { font-weight: 700; opacity: 0.85; }
      .value { opacity: 0.95; }
      .tiny { font-size: 0.9rem; opacity: 0.75; }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="case-title">CASE FILE: THE GOLDI AFFAIR 💌</div>', unsafe_allow_html=True)
st.markdown('<div class="case-subtitle">Confidential • Romantic Investigation Unit </div>', unsafe_allow_html=True)

# -----------------------------
# COVER IMAGE
# -----------------------------
if COVER_IMG.exists():
    st.image(str(COVER_IMG), use_container_width=True)
else:
    st.warning(f"Cover image not found at: {COVER_IMG}")

# -----------------------------
# CASE DETAILS (edit these!)
# -----------------------------
CASE_ID = "Valentine-0214"  # change to whatever you want
PRIMARY_SUBJECT = "Karah Womack"
CODE_NAME = "Goldilocks"
CASE_STATUS = "OPEN"
OPENED_ON = date.today().strftime("%B %d, %Y")  # auto

st.markdown(
    f"""
    <div class="case-card">
      <div><span class="label">Case ID:</span> <span class="value">{CASE_ID}</span></div>
      <div><span class="label">Primary Subject:</span> <span class="value">{PRIMARY_SUBJECT}</span></div>
      <div><span class="label">Code Name:</span> <span class="value">{CODE_NAME}</span></div>
      <div><span class="label">Status:</span> <span class="value">{CASE_STATUS}</span></div>
      <div><span class="label">Opened:</span> <span class="value">{OPENED_ON}</span></div>
      <hr style="opacity:0.2;">
      <div class="label">Case Summary</div>
      <div class="value">
        The subject has been causing widespread emotional disruption.
Armed with unmatched beauty, a hot body, sharp wit, and dangerously effective charm, Goldi not only bends herself to get what she wants from her 
lover but she'll also bend situations too. Her eyes and voice may just be the most captivating thing about her. 

Witness reports confirm that both men and women have fallen under her spell, often without warning. Resistance is rare. Immunity is nonexistent.

🎯 Your Mission:
Convince the elusive Goldi to agree to be my Valentine. 

The odds are stacked against you.
Both men and only a few brave women have tried. Few have remained to tell the story.

But I believe you have what it takes.

Proceed carefully 💋
      </div>
      <p class="tiny" style="margin-top:12px;">
        Next step: proceed to Evidence Intake when ready.
      </p>
    </div>
    """,
    unsafe_allow_html=True
)

if st.button("Start The Mission", type="primary", use_container_width=True):
    st.switch_page("pages/1_Investigation.py")
