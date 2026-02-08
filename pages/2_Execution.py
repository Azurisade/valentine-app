# pages/2_Execution.py
import streamlit as st
from pathlib import Path
import base64
import streamlit.components.v1 as components
import random

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Execution 💘",
    page_icon="💘",
    layout="centered"
)

# -----------------------------
# PATHS
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent  # pages/ -> project root
AUDIO_FILE = BASE_DIR / "assets" / "audio" / "ordinary people.mp3"

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
      .big { font-size: 1.1rem; font-weight: 900; }
      .tiny { font-size: 0.9rem; opacity: 0.75; }
      .pill {
        display:inline-block; padding:6px 10px; border-radius:999px;
        border: 1px solid rgba(255,255,255,0.18); background: rgba(255,255,255,0.05);
        margin-right: 8px; margin-bottom: 8px; font-weight:750;
      }
      .center { text-align: center; }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# SAFE GETTERS
# -----------------------------
profile = st.session_state.get("profile", {})
generated = st.session_state.get("generated", {})
vibe = st.session_state.get("vibe", "Flirty")

name = (profile.get("name") or "Goldi").strip()
codename = (profile.get("codename") or "Goldi").strip()
weakness = (profile.get("weakness") or "").strip()
inside_joke = (profile.get("inside_joke") or "").strip()

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="title">EXECUTION: THE BIG ASK 💘</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">This is the moment. Be brave. Be cute. Be a little delusional (in a charming way).</div>', unsafe_allow_html=True)

# -----------------------------
# AUDIO (optional)
# -----------------------------
with st.expander("🎧 Optional: Play Vibes", expanded=False):
    if AUDIO_FILE.exists():
        b64 = base64.b64encode(AUDIO_FILE.read_bytes()).decode("utf-8")
        components.html(
            f"""
            <div style="display:flex; gap:10px; margin: 8px 0 0 0;">
              <button id="playBtn" style="
                  flex:1; padding:12px; border-radius:12px; border:1px solid rgba(255,255,255,0.25);
                  background: rgba(255,255,255,0.06); color:pink; font-weight:900; cursor:pointer;">
                ▶️ Play
              </button>

              <button id="muteBtn" style="
                  flex:1; padding:12px; border-radius:12px; border:1px solid rgba(255,255,255,0.25);
                  background: rgba(255,255,255,0.06); color:pink; font-weight:900; cursor:pointer;">
                ⏹ Stop
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
                  alert("Tap again — browser being dramatic.");
                }}
              }});
              document.getElementById("muteBtn").addEventListener("click", () => {{
                audio.pause();
                audio.currentTime = 0;
              }});
            </script>
            """,
            height=80,
        )
    else:
        st.warning(f"Audio not found at: {AUDIO_FILE}")

# -----------------------------
# SHOW THE MESSAGE TO SEND
# -----------------------------
st.markdown(
    """
    <div class="card">
      <div class="big">📤 Your Mission Text</div>
      <div class="tiny">Send this. Or tweak it.</div>
    </div>
    """,
    unsafe_allow_html=True
)

default_msg = (
    f"🚨 BREAKING NEWS: Subject **{codename}** spotted.\n\n"
    f"I had to report it because… you’re kinda impossible to ignore.\n\n"
    f"So {name}… be my Valentine? 💘\n\n"
    f"💋 — Courtney"
)

msg = generated.get("opener")
if generated:
    message_text = f"""{generated.get('opener','')}

{generated.get('line1','')}

{generated.get('bits','')}

{generated.get('ask','')}

{generated.get('backup','')}

💋 — Courtney
""".strip()
else:
    message_text = default_msg

st.text_area("Message ready to send:", message_text, height=240)

# -----------------------------
# OUTCOME SIMULATOR
# -----------------------------
st.markdown(
    f"""
    <div class="card">
      <div class="big">🎬 Choose the Outcome (for fun)</div>
      <div class="tiny">She taps one. The universe responds.</div>
      <div style="margin-top:10px;">
        <span class="pill">Vibe: {vibe}</span>
        <span class="pill">Subject: {codename}</span>
        <span class="pill">Likelihood of being success: high</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

if "outcome" not in st.session_state:
    st.session_state.outcome = None

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Duh, Pretty Girl 🤍", use_container_width=True):
        st.session_state.outcome = "yes"
        st.session_state.case_solved = True
        st.switch_page("pages/3_Case_Solved.py")
with col2:
    if st.button("👅 Show Me You Want Me First 💦", use_container_width=True):
        st.session_state.outcome = "maybe"
with col3:
    if st.button("No, I hate you", use_container_width=True):
        st.session_state.outcome = "stop"

# -----------------------------
# RESPONSES
# -----------------------------
yes_lines = [
    f"CASE CLOSED. Valentine secured. {codename} has agreed. 🎉",
    f"CONFIRMED: {name} said yes. Please proceed to celebration activities immediately.",
    f"Update: {codename} accepted."
]

maybe_lines = [
    "I need dat 😌",
]

stop_lines = [
    "👎🏼"
]

def follow_up_for(outcome: str) -> str:
    # Optional personalization
    hook = ""
    if weakness:
        hook = f"\n\n(Also I remembered your weakness is **{weakness}**… so I’m coming prepared 😇)"
    joke = f'\n\nCode phrase: “{inside_joke}”' if inside_joke else ""

    if outcome == "yes":
        options = [
            "I love you baby ❤️‍🔥, I know this game was a bit corny but thank you for playing. Closest thing I could do to that Club Penguin game you like lol"
        ]
        return random.choice(options) + hook + joke

    if outcome == "maybe":
        options = [
            "We can move this to the bedroom, so I can do more convincing. 😌",
        ]
        return random.choice(options) + hook + joke

    # stop
    options = [
        "Yeah, not accepted.",
    ]
    return random.choice(options) + hook + joke

# Display outcome result
if st.session_state.outcome:
    st.markdown('<div class="card"><div class="big">📨 Her Response</div></div>', unsafe_allow_html=True)

    if st.session_state.outcome == "yes":
        st.success(random.choice(yes_lines))
        st.balloons()
    elif st.session_state.outcome == "maybe":
        st.warning(random.choice(maybe_lines))
        st.snow()
    else:
        st.info(random.choice(stop_lines))

    st.markdown('<div class="card"><div class="big">🧠 Your Follow-Up</div><div class="tiny">Send this right after her reply.</div></div>', unsafe_allow_html=True)
    st.text_area("Follow-up message:", follow_up_for(st.session_state.outcome), height=140)

# -----------------------------
# NAV / RESET
# -----------------------------
st.write("")
nav1, nav2, nav3 = st.columns(3)

with nav1:
    if st.button("⬅️ Back to Investigation", use_container_width=True):
        st.switch_page("pages/1_Investigation.py")

with nav2:
    if st.button("🔄 Reset Outcome", use_container_width=True):
        st.session_state.outcome = None

with nav3:
    if st.button("🗑️ Full Reset (Start Over)", use_container_width=True):
        # Clears everything we created in these pages
        for k in ["profile", "vibe", "generated", "outcome"]:
            if k in st.session_state:
                del st.session_state[k]
        st.switch_page("pages/1_Investigation.py")
