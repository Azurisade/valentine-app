import streamlit as st
from pathlib import Path
import base64
import streamlit.components.v1 as components
import random

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="The Investigation 🕵🏽‍♀️",
    page_icon="🕵🏽‍♀️",
    layout="centered"
)

# -----------------------------
# PATHS
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent  # pages/ -> project root
AUDIO_FILE = BASE_DIR / "assets" / "audio" / "miro.mp3"

# -----------------------------
# STYLING
# -----------------------------
st.markdown(
    """
    <style>
      .title { font-size: 2.0rem; font-weight: 950; margin-bottom: 0.2rem; }
      .sub { font-size: 1.0rem; opacity: 0.85; margin-top: 0; }
      .card {
        border: 1px solid rgba(255,255,255,0.18);
        border-radius: 18px;
        padding: 18px;
        background: rgba(255,255,255,0.04);
        margin-top: 14px;
      }
      .big { font-size: 1.1rem; font-weight: 800; }
      .tiny { font-size: 0.9rem; opacity: 0.75; }
      .pill {
        display:inline-block; padding:6px 10px; border-radius:999px;
        border: 1px solid rgba(255,255,255,0.18); background: rgba(255,255,255,0.05);
        margin-right: 8px; margin-bottom: 8px; font-weight:700;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="title">THE INVESTIGATION 🕵🏽‍♀️</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">This is not a questionnaire. This is a highly unserious operation.</div>', unsafe_allow_html=True)

# -----------------------------
# AUDIO (JS buttons)
# -----------------------------
if AUDIO_FILE.exists():
    b64 = base64.b64encode(AUDIO_FILE.read_bytes()).decode("utf-8")
    components.html(
        f"""
        <div style="display:flex; gap:10px; margin: 10px 0 0 0;">
          <button id="playBtn" style="
              flex:1; padding:12px; border-radius:12px; border:1px solid rgba(255,255,255,0.25);
              background: rgba(255,255,255,0.06); color:pink; font-weight:900; cursor:pointer;">
            🎧 Play Vibes
          </button>

          <button id="muteBtn" style="
              flex:1; padding:12px; border-radius:12px; border:1px solid rgba(255,255,255,0.25);
              background: rgba(255,255,255,0.06); color:pink; font-weight:900; cursor:pointer;">
            🔇 Stop
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
              alert("Tap again — your browser is being dramatic.");
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
    st.warning(f"Audio not found at: {AUDIO_FILE}")

# -----------------------------
# SESSION STATE
# -----------------------------
if "profile" not in st.session_state:
    st.session_state.profile = {
        "name": "Karah",
        "codename": "Goldi",
        "weakness": "",
        "fav_thing": "",
        "inside_joke": "",
        "moment": "",
    }

if "vibe" not in st.session_state:
    st.session_state.vibe = "Goofy & Cute"

# -----------------------------
# FUN BRIEFING
# -----------------------------
st.markdown(
    """
    <div class="card">
      <div class="big">🧾 Agent Briefing</div>
      <div style="margin-top:8px;">
        Welcome to Operation: <b>Get Goldi to Say Yes</b>.
        Your job is to create a message so good she cant say no.
      </div>
      <div style="margin-top:10px;">
        <span class="pill">Risk: She Hates It</span>
        <span class="pill">Threat level: Medium</span>
        <span class="pill">Outcome: Valentine Secured</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# CHOOSE YOUR CHAOS
# -----------------------------
st.markdown('<div class="card"><div class="big">🎛️ Choose Your Chaos</div><div class="tiny">Pick a vibe.</div></div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("Spicy", use_container_width=True):
        st.session_state.vibe = "Spicy"
with c2:
    if st.button("Flirty", use_container_width=True):
        st.session_state.vibe = "Flirty"
with c3:
    if st.button("More Romantic", use_container_width=True):
        st.session_state.vibe = "More Romantic"

st.info(f"Current vibe: **{st.session_state.vibe}**")

# -----------------------------
# SUSPECT PROFILE
# -----------------------------
st.markdown('<div class="card"><div class="big">🗂️ Suspect Profile (low effort, high impact)</div></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.session_state.profile["name"] = st.text_input("Her name (for display)", st.session_state.profile["name"])
    st.session_state.profile["codename"] = st.text_input("Her code name", st.session_state.profile["codename"])
    st.session_state.profile["weakness"] = st.text_input("Her weakness (what melts her)", st.session_state.profile["weakness"])

with col2:
    st.session_state.profile["fav_thing"] = st.text_input("One thing she likes about you", st.session_state.profile["fav_thing"])
    st.session_state.profile["inside_joke"] = st.text_input("Inside joke / nickname", st.session_state.profile["inside_joke"])
    st.session_state.profile["moment"] = st.text_input("A moment y’all had (short)", st.session_state.profile["moment"])

# -----------------------------
# GENERATOR (FUN LINES)
# -----------------------------
p = st.session_state.profile
vibe = st.session_state.vibe

fun_openers = [
    "🚨 BREAKING NEWS:",
    "📌 OFFICIAL NOTICE:",
    "🕵🏽‍♀️ CASE UPDATE:",
    "⚠️ ALERT:",
    "🧾 REPORT:",
]
spicy_lines = [
    "You`re my favorite thing to eat",
    "I wonder how you`d diagnose me the way im bricked whenever you`re around",
    "I need you and I want to make love to you every night. ",
    "I tried to focus today. Then the thought of you naked got in my head",
]
flirty_lines = [
    "Some people feel like noise, you feel like the pause I never knew I needed.",
    "I’m not saying I’m obsessed… but I’m definitely investigating.",
    "If comfort had a personality, it would have your voice.",
]
sweet_lines = [
    "You make my world feel lighter, and you brighten it all at the same time.",
    "I like who I am when I’m with you.",
    "I could do this life over and over with you",
]

def build_message():
    name = (p.get("name") or "you").strip()
    code = (p.get("codename") or "Goldi").strip()
    weakness = (p.get("weakness") or "").strip()
    fav = (p.get("fav_thing") or "").strip()
    joke = (p.get("inside_joke") or "").strip()
    moment = (p.get("moment") or "").strip()

    opener = random.choice(fun_openers) + f" Subject **{code}** spotted."

    if vibe == "Spicy":
        line1 = random.choice(spicy_lines)
    elif vibe == "Flirty":
        line1 = random.choice(flirty_lines)
    else:
        line1 = random.choice(sweet_lines)

    personal_bits = []
    if fav:
        personal_bits.append(f"I love your {fav}.")
    if moment:
        personal_bits.append(f"And I still think about {moment}.")
    if weakness:
        personal_bits.append(f"Also your weakness is **{weakness}** so I’m using that respectfully. 😇")
    if joke:
        personal_bits.append(f'Code phrase: “{joke}” (you know what that means).')

    bits = "\n".join(personal_bits).strip()
    ask = f"So {name}… be my Valentine? 💘"
    backup = "no isn`t an option"

    return opener, line1, bits, ask, backup

# -----------------------------
# AUTO-GENERATE + REMIX BUTTON
# -----------------------------
has_any = any([
    (p.get("name") or "").strip(),
    (p.get("codename") or "").strip(),
    (p.get("weakness") or "").strip(),
    (p.get("fav_thing") or "").strip(),
    (p.get("inside_joke") or "").strip(),
    (p.get("moment") or "").strip(),
])

colA, colB = st.columns(2)
with colA:
    remix = st.button("🎲 Press Me", use_container_width=True)
with colB:
    st.write("")

if has_any:
    if "generated" not in st.session_state or remix:
        opener, line1, bits, ask, backup = build_message()
        st.session_state.generated = {
            "opener": opener,
            "line1": line1,
            "bits": bits,
            "ask": ask,
            "backup": backup
        }
else:
    st.session_state.generated = None

# -----------------------------
# OUTPUT
# -----------------------------
st.markdown(
    '<div class="card"><div class="big">💬 Mission Text</div><div class="tiny">Copy/paste and hit send when you’re brave.</div></div>',
    unsafe_allow_html=True
)

g = st.session_state.get("generated")

if not g:
    st.write("Type anything in the profile above — then I’ll generate your mission text automatically 😌")
else:
    msg = f"""{g['opener']}

{g['line1']}

{g['bits']}

{g['ask']}

{g['backup']}

💋 — Courtney
"""
    st.text_area("Your Message", msg, height=260)
    st.caption("Mix this up and add what you want")

# -----------------------------
# NEXT STEP (placeholder)
# -----------------------------
st.write("")
    # later: st.switch_page(\"pages/2_Execution.py\")

if st.button("➡️ Next: The Big Ask (Execution)", use_container_width=True):
    st.switch_page("pages/2_Execution.py")

