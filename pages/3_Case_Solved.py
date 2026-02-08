import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Case Solved ✅",
    page_icon="✅",
    layout="wide"  # IMPORTANT for fullscreen
)

# -----------------------------
# FULLSCREEN + HIDE SIDEBAR
# -----------------------------
st.markdown(
    """
    <style>
      /* Hide sidebar + top padding */
      [data-testid="stSidebar"] { display: none; }
      [data-testid="stAppViewContainer"] {
        padding-top: 0rem;
        padding-bottom: 0rem;
      }
      [data-testid="stHeader"] { display: none; }

      /* Center title overlay */
      .overlay {
        position: absolute;
        top: 5%;
        width: 100%;
        text-align: center;
        z-index: 10;
        color: white;
        text-shadow: 0 4px 20px rgba(0,0,0,0.6);
      }
      .title {
        font-size: 3.2rem;
        font-weight: 950;
        letter-spacing: 1px;
      }
      .sub {
        font-size: 1.2rem;
        opacity: 0.9;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# LOCK: YES ONLY
# -----------------------------
if not st.session_state.get("case_solved", False):
    st.error("🚫 Access denied. This page unlocks only after choosing YES.")
    if st.button("⬅️ Back to Execution", use_container_width=True, key="back_exec_lock"):
        st.switch_page("pages/2_Execution.py")
    st.stop()

# -----------------------------
# PATH
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
IMG_PATH = BASE_DIR / "assets" / "images" / "me_n_goldi.PNG"

# -----------------------------
# OVERLAY TEXT
# -----------------------------
st.markdown(
    """
    <div class="overlay">
        <div class="title">CASE SOLVED ✅</div>
        <div class="sub">Valentine secured. Mission complete.</div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# FULLSCREEN IMAGE
# -----------------------------
if IMG_PATH.exists():
    st.image(str(IMG_PATH), use_container_width=True)
else:
    st.warning(f"Image not found at: {IMG_PATH}")

# -----------------------------
# CELEBRATION
# -----------------------------
st.balloons()

# -----------------------------
# FOOTER CONTROLS (OPTIONAL)
# -----------------------------
st.write("")
col1, col2 = st.columns(2)

with col1:
    if st.button("🔄 Replay Execution", use_container_width=True, key="replay_exec"):
        st.switch_page("pages/2_Execution.py")

with col2:
    if st.button("🗑️ Reset Everything", use_container_width=True, key="reset_all"):
        for k in ["profile", "vibe", "generated", "outcome", "case_solved"]:
            if k in st.session_state:
                del st.session_state[k]
        st.switch_page("app.py")
