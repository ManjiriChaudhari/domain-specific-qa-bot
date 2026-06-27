/* ===============================
   GLOBAL
================================ */

html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
}

/* Main App */

.stApp{
    background:#0d1117;
    color:white;
}

/* ===============================
SIDEBAR
================================ */

section[data-testid="stSidebar"]{

    background:#161b22;
    border-right:1px solid #30363d;

}

/* ===============================
BUTTONS
================================ */

.stButton>button{

    width:100%;

    border-radius:10px;

    border:none;

    background:#2383e2;

    color:white;

    font-weight:600;

    transition:.3s;

}

.stButton>button:hover{

    background:#1d6fd6;

    transform:scale(1.02);

}

/* ===============================
CHAT INPUT
================================ */

.stChatInput{

    border-radius:15px;

}

/* ===============================
USER CHAT
================================ */

[data-testid="stChatMessageContent"]{

    border-radius:12px;

    padding:15px;

}

/* ===============================
SUCCESS BOX
================================ */

.stSuccess{

    border-radius:10px;

}

/* ===============================
EXPANDER
================================ */

.streamlit-expanderHeader{

    font-weight:700;

}

/* ===============================
HEADINGS
================================ */

h1{

    color:#4aa3ff;

}

h2{

    color:#4aa3ff;

}

h3{

    color:#4aa3ff;

}

/* ===============================
DIVIDER
================================ */

hr{

    border:1px solid #30363d;

}

/* ===============================
SCROLLBAR
================================ */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#2383e2;

    border-radius:10px;

}

::-webkit-scrollbar-track{

    background:#161b22;

}

/* ===============================
METRICS
================================ */

[data-testid="metric-container"]{

    background:#161b22;

    border-radius:12px;

    padding:10px;

}

/* ===============================
CODE BLOCK
================================ */

pre{

    border-radius:12px;

}

/* ===============================
ANIMATION
================================ */

.stChatMessage{

    animation:fade .4s ease;

}

@keyframes fade{

    from{

        opacity:0;

        transform:translateY(10px);

    }

    to{

        opacity:1;

        transform:translateY(0px);

    }

}
/* ==========================================
   CHAT MESSAGES
========================================== */

/* Chat bubble */
[data-testid="stChatMessage"]{
    background-color:#161b22;
    border-radius:12px;
    padding:15px;
    margin-bottom:10px;
    border:1px solid #30363d;
}

/* Chat text */
[data-testid="stChatMessageContent"]{
    color:#FFFFFF !important;
    font-size:16px;
    line-height:1.7;
}

/* Make ALL text inside chat white */
[data-testid="stChatMessageContent"] *{
    color:#FFFFFF !important;
}

/* Markdown paragraphs */
[data-testid="stMarkdownContainer"] p{
    color:#FFFFFF !important;
}

/* Lists */
[data-testid="stMarkdownContainer"] li{
    color:#FFFFFF !important;
}

/* Bold */
[data-testid="stMarkdownContainer"] strong{
    color:#FFFFFF !important;
}

/* Headers inside chat */
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] h4{
    color:#4aa3ff !important;
}
