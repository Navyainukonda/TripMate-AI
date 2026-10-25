
import streamlit as st

st.set_page_config(
    page_title="TripMate AI",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# COMPLETE CSS — TRIPMATE AI
# =========================================================

st.markdown("""
<style>
/* ---------- Global reset ---------- */
* {
    box-sizing: border-box;
}

html, body, [data-testid="stAppViewContainer"] {
    margin: 0;
    padding: 0;
}

.stApp {
    color: #f4f7ff;
    background:
        radial-gradient(
            ellipse 39% 48% at 4% 25%,
            rgba(20, 91, 174, 0.72) 0%,
            rgba(15, 65, 125, 0.35) 42%,
            transparent 78%
        ),
        radial-gradient(
            ellipse 34% 43% at 94% 29%,
            rgba(100, 37, 150, 0.60) 0%,
            rgba(71, 29, 110, 0.25) 45%,
            transparent 78%
        ),
        radial-gradient(
            ellipse 25% 24% at 37% 82%,
            rgba(0, 115, 105, 0.28) 0%,
            transparent 75%
        ),
        linear-gradient(
            112deg,
            #0b1930 0%,
            #0b1429 48%,
            #10142c 100%
        );
}

/* Hide Streamlit header/footer chrome */
header[data-testid="stHeader"] {
    height: 0;
    background: transparent;
}

[data-testid="stToolbar"] {
    visibility: hidden;
    height: 0;
}

#MainMenu,
footer {
    visibility: hidden;
}

/* Main content width and page spacing */
.main .block-container {
    width: 100%;
    max-width: 1600px;
    padding: 4px 32px 12px 32px;
    margin: 0 auto;
}

/* Remove excess vertical space between Streamlit blocks */
div[data-testid="stVerticalBlock"] {
    gap: 0.5rem;
}

/* ---------- Top brand pill ---------- */
.brand-wrap {
    display: flex;
    justify-content: center;
    width: 100%;
    margin: 0 auto 20px auto;
}

.brand-pill {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    min-height: 54px;
    padding: 10px 25px;
    border: 1px solid rgba(166, 180, 211, 0.36);
    border-radius: 999px;
    background: rgba(13, 23, 45, 0.48);
    color: #c6c0fa;
    font-size: 20px;
    font-weight: 750;
    letter-spacing: -0.45px;
    text-align: center;
}

/* ---------- Hero title ---------- */
.hero-title {
    width: 100%;
    margin: 18px auto 17px auto;
    text-align: center;
    font-size: clamp(44px, 6vw, 100px);
    font-weight: 850;
    line-height: 1.12;
    letter-spacing: -4.5px;
    white-space: nowrap;

    background: linear-gradient(
        95deg,
        #e1efff 3%,
        #a8ceff 37%,
        #a9a3ff 69%,
        #d28bfa 100%
    );
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* ---------- Subtitle ---------- */
.hero-subtitle {
    max-width: 1020px;
    width: 100%;
    margin: 20px auto 44px auto;
    padding: 0 12px;
    color: #c7d0e1;
    text-align: center;
    font-size: 22px;
    font-weight: 400;
    line-height: 1.7;
    letter-spacing: -0.25px;
}

/* ---------- Planner card ---------- */
.st-key-planner {
    width: 100%;
    padding: 30px 35px 27px 35px;
    border: 1px solid rgba(138, 155, 192, 0.38);
    border-radius: 37px;
    background:
        radial-gradient(
            ellipse at 40% 100%,
            rgba(0, 103, 99, 0.19),
            transparent 47%
        ),
        rgba(9, 20, 42, 0.82);
    box-shadow: 0 20px 55px rgba(0, 0, 0, 0.12);
}

/* Planner heading and helper text */
.planner-heading {
    color: #f5f7fc;
    font-size: 28px;
    font-weight: 780;
    line-height: 1.3;
    letter-spacing: -0.6px;
    margin: 4px 0 8px 0;
}

.planner-hint {
    color: #a9b6cc;
    font-size: 20px;
    line-height: 1.5;
    margin: 0 0 24px 0;
}

/* Online badge */
.online-wrap {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    width: 100%;
}

.online-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    min-width: 109px;
    height: 43px;
    padding: 0 17px;
    border: 1px solid rgba(50, 190, 127, 0.35);
    border-radius: 999px;
    background: rgba(24, 117, 91, 0.24);
    color: #8ce8b5;
    font-size: 16px;
    font-weight: 700;
}

.online-dot {
    width: 10px;
    height: 10px;
    flex: 0 0 10px;
    border-radius: 50%;
    background: #30d17a;
    box-shadow: 0 0 9px rgba(48, 209, 122, 0.25);
}

/* ---------- Input and action row ---------- */
.st-key-input_row {
    width: 100%;
}

.st-key-input_row [data-testid="stHorizontalBlock"] {
    align-items: stretch !important;
    gap: 18px !important;
}

/* Remove default textarea label space */
.st-key-trip_prompt [data-testid="stWidgetLabel"] {
    display: none;
}

.st-key-trip_prompt {
    width: 100%;
}

.st-key-trip_prompt [data-testid="stTextArea"] {
    width: 100%;
}

.st-key-trip_prompt textarea {
    height: 190px !important;
    min-height: 190px !important;
    max-height: 190px !important;
    resize: vertical;

    background: #030a25 !important;
    color: #e6edff !important;
    border: 1px solid #628ce3 !important;
    border-radius: 29px !important;
    outline: none !important;
    box-shadow:
        0 0 0 4px rgba(50, 100, 202, 0.18),
        inset 0 0 18px rgba(5, 14, 40, 0.35) !important;

    padding: 26px 25px !important;
    font-size: 18px !important;
    line-height: 1.6 !important;
    font-family: inherit !important;
}

.st-key-trip_prompt textarea::placeholder {
    color: #8290aa !important;
    opacity: 1;
}

.st-key-trip_prompt textarea:focus {
    border-color: #8bb1ff !important;
    box-shadow:
        0 0 0 4px rgba(73, 126, 234, 0.24),
        0 0 25px rgba(64, 112, 225, 0.12) !important;
}

/* ---------- Generate button ---------- */
.st-key-generate {
    width: 100%;
    padding-top: 0;
    margin-top: 0;
}

.st-key-generate [data-testid="stButton"] {
    width: 100%;
}

.st-key-generate button {
    width: 100%;
    height: 188px;
    min-height: 188px;
    padding: 15px;

    border: 0 !important;
    border-radius: 28px !important;
    background: linear-gradient(
        125deg,
        #3276f2 0%,
        #5159f1 52%,
        #853cf0 100%
    ) !important;

    color: #ffffff !important;
    font-size: 20px !important;
    font-weight: 800 !important;
    white-space: normal;
    box-shadow: 0 12px 32px rgba(67, 91, 237, 0.22);
    transition: filter 0.2s ease, transform 0.2s ease;
}

.st-key-generate button:hover {
    filter: brightness(1.10);
    transform: translateY(-1px);
}

.st-key-generate button:active {
    transform: translateY(0);
}

/* ---------- Quick suggestion buttons ---------- */
.st-key-suggestions {
    width: 100%;
    margin-top: 18px;
}

.st-key-suggestions [data-testid="stHorizontalBlock"] {
    gap: 12px !important;
}

.st-key-suggestions [data-testid="stButton"] {
    width: 100%;
}

.st-key-suggestions button {
    width: 100%;
    min-height: 47px;
    padding: 8px 16px;

    border: 1px solid rgba(139, 157, 190, 0.35) !important;
    border-radius: 999px !important;
    background: rgba(115, 135, 166, 0.16) !important;
    color: #dbe5f5 !important;

    font-size: 15px !important;
    font-weight: 500 !important;
    white-space: nowrap;
    transition: background 0.2s ease, border-color 0.2s ease;
}

.st-key-suggestions button:hover {
    background: rgba(101, 123, 167, 0.30) !important;
    border-color: rgba(151, 174, 224, 0.65) !important;
    color: #ffffff !important;
}

/* ---------- Footer ---------- */
.footer-text {
    width: 100%;
    margin: 70px auto 12px auto;
    text-align: center;
    color: #697991;
    font-size: 18px;
    font-weight: 400;
    letter-spacing: 0.05px;
}

/* ---------- Responsive layout ---------- */
@media (max-width: 1100px) {
    .main .block-container {
        padding-left: 24px;
        padding-right: 24px;
    }

    .hero-title {
        white-space: normal;
        font-size: clamp(44px, 6.5vw, 72px);
        letter-spacing: -2.5px;
    }

    .hero-subtitle {
        font-size: 19px;
        margin-bottom: 32px;
    }

    .st-key-planner {
        padding: 26px;
        border-radius: 28px;
    }
}

@media (max-width: 700px) {
    .main .block-container {
        padding: 12px 14px 10px;
    }

    .brand-wrap {
        margin-bottom: 20px;
    }

    .brand-pill {
        min-height: 42px;
        padding: 8px 13px;
        font-size: 13px;
    }

    .hero-title {
        margin-top: 18px;
        font-size: clamp(34px, 9vw, 48px);
        line-height: 1.13;
        letter-spacing: -1.8px;
    }

    .hero-subtitle {
        margin: 16px auto 28px;
        font-size: 16px;
        line-height: 1.65;
    }

    .st-key-planner {
        padding: 20px 16px;
        border-radius: 23px;
    }

    .planner-heading {
        font-size: 23px;
    }

    .planner-hint {
        font-size: 16px;
        margin-bottom: 18px;
    }

    .st-key-input_row [data-testid="stHorizontalBlock"] {
        flex-direction: column;
        gap: 12px !important;
    }

    .st-key-trip_prompt textarea {
        height: 150px !important;
        min-height: 150px !important;
        border-radius: 19px !important;
        padding: 18px !important;
        font-size: 15px !important;
    }

    .st-key-generate button {
        height: 58px;
        min-height: 58px;
        border-radius: 16px !important;
        font-size: 17px !important;
    }

    .st-key-suggestions [data-testid="stHorizontalBlock"] {
        flex-wrap: wrap;
        gap: 8px !important;
    }

    .st-key-suggestions [data-testid="column"] {
        min-width: 42% !important;
        flex: 1 1 42% !important;
    }

    .st-key-suggestions button {
        min-height: 42px;
        font-size: 13px !important;
        padding: 7px 8px;
    }

    .footer-text {
        margin-top: 35px;
        font-size: 13px;
        line-height: 1.6;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="brand-wrap">
    <div class="brand-pill">
        ✈️ TripMate AI — A Multi-Agent Travel Planner with LangGraph
    </div>
</div>

<div class="hero-title">
    Plan Your Perfect Trip with AI
</div>

<div class="hero-subtitle">
    Search flights, discover hotels, and generate a complete travel
    itinerary using a multi-agent LangGraph system.
</div>
""", unsafe_allow_html=True)


# =========================================================
# PLANNER CARD
# =========================================================

with st.container(key="planner", border=False):

    # Header and online badge
    header_left, header_right = st.columns(
        [5, 1],
        gap="small",
        vertical_alignment="center",
    )

    with header_left:
        st.markdown(
            '<div class="planner-heading">Where do you want to go?</div>'
            '<div class="planner-hint">'
            'Example: Plan a complete 7 days Japan trip from Bangladesh under 2 lakhs.'
            '</div>',
            unsafe_allow_html=True,
        )

    with header_right:
        st.markdown("""
        <div class="online-wrap">
            <div class="online-badge">
                <span class="online-dot"></span>
                Online
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Prompt + Generate button
    with st.container(key="input_row", border=False):
        input_col, button_col = st.columns(
            [5.2, 1],
            gap="small",
            vertical_alignment="top",
        )

        with input_col:
            prompt = st.text_area(
                "Trip description",
                placeholder=(
                    "Plan a complete 7 days Japan trip including flights, "
                    "hotels and sightseeing under 2 lakhs..."
                ),
                height=190,
                key="trip_prompt",
                label_visibility="collapsed",
            )

        with button_col:
            st.markdown('<div style="height: 4px"></div>',
                        unsafe_allow_html=True)
            with st.container(key="generate", border=False):
                generate_clicked = st.button(
                    "Generate Plan",
                    key="generate_plan_button",
                    use_container_width=True,
                )


# =========================================================
# QUICK SUGGESTIONS — WORKING
# =========================================================

SUGGESTIONS = {
    "🇯🇵 Japan Trip": (
        "Plan a 7-day trip to Japan from Bangladesh, "
        "including flights, hotels, sightseeing, and a realistic budget."
    ),
    "🇦🇪 Dubai Trip": (
        "Plan a 5-day trip to Dubai from Bangladesh, "
        "including flight options, hotels, attractions, and a budget."
    ),
    "🇹🇭 Thailand Trip": (
        "Plan a 6-day trip to Thailand from Bangladesh, "
        "including flights, hotels, beaches, sightseeing, and a budget."
    ),
    "🌍 Global Flights": (
        "Search available international flights from Dhaka, Bangladesh. "
        "Show available routes, airlines, departure and arrival airports, "
        "schedules, and prices when the API provides them."
    ),
}

def select_suggestion(request):
    # Update the prompt widget before it is rendered on the next rerun.
    st.session_state["trip_prompt"] = request
    st.session_state["run_trip_request"] = True


with st.container(key="suggestions", border=False):
    suggestion_cols = st.columns(4, gap="small")

    for col, (label, request) in zip(
        suggestion_cols, SUGGESTIONS.items()
    ):
        with col:
            st.button(
                label,
                key=f"suggestion_{label}",
                use_container_width=True,
                on_click=select_suggestion,
                args=(request,),
            )


# =========================================================
# CONNECT YOUR LANGGRAPH BACKEND HERE
# =========================================================



# =========================================================
# LANGGRAPH BACKEND INTEGRATION
# =========================================================

import uuid

# Create a persistent conversation ID for this Streamlit session
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if generate_clicked:
    if not prompt.strip():
        st.warning("Please describe your trip before generating a plan.")

    else:
        try:
            # Import your existing LangGraph backend
            from backend import run_travel_agent

            with st.spinner(
                "✈️ Your AI travel agents are planning your trip..."
            ):
                result = run_travel_agent(
                    prompt.strip(),
                    thread_id=st.session_state.thread_id,
                )

            # Handle the backend response
            if not isinstance(result, dict):
                st.error(
                    "Unexpected backend response. "
                    "Expected a dictionary from run_travel_agent()."
                )
            else:
                # Preserve thread ID if the backend returns an updated one
                st.session_state.thread_id = result.get(
                    "thread_id",
                    st.session_state.thread_id,
                )

                st.success("Your travel plan is ready!")

                # Main answer
                answer = result.get("answer")

                if answer:
                    st.markdown("## 🌍 Your Travel Plan")
                    st.markdown(answer)

                # Flight results
                flight_results = result.get("flight_results")

                if flight_results:
                    st.markdown("## ✈️ Flight Options")

                    if isinstance(flight_results, (list, tuple)):
                        for flight in flight_results:
                            if isinstance(flight, dict):
                                st.json(flight)
                            else:
                                st.write(flight)
                    else:
                        st.write(flight_results)

                # Hotel results
                hotel_results = result.get("hotel_results")

                if hotel_results:
                    st.markdown("## 🏨 Hotel Options")

                    if isinstance(hotel_results, (list, tuple)):
                        for hotel in hotel_results:
                            if isinstance(hotel, dict):
                                st.json(hotel)
                            else:
                                st.write(hotel)
                    else:
                        st.write(hotel_results)

                # Itinerary
                itinerary = result.get("itinerary")

                if itinerary:
                    st.markdown("## 🗓️ Day-by-Day Itinerary")

                    if isinstance(itinerary, (dict, list)):
                        st.json(itinerary)
                    else:
                        st.markdown(str(itinerary))

                # Inform the user if the backend returned no displayable data
                if not any([
                    answer,
                    flight_results,
                    hotel_results,
                    itinerary,
                ]):
                    st.info(
                        "The agent completed, but no travel details were "
                        "returned. Check the output of run_travel_agent()."
                    )

        except ImportError as exc:
            st.error(
                f"Could not import your LangGraph backend: {exc}"
            )

        except Exception as exc:
            st.error(
                f"Failed to generate your travel plan: {exc}"
            )
            st.exception(exc)




# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer-text">
    Built with FastAPI, LangGraph, Ollama, PostgreSQL, Tavily and AviationStack
</div>
""", unsafe_allow_html=True)
