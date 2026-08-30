import streamlit as st

st.set_page_config(page_title="SCAN&STOP - RBI Scam Detector", layout="wide")

def load_css(filename):
    try:
        with open(filename, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)      
    except FileNotFoundError:
        pass # Prevents crash if CSS file is missing locally
load_css ("scanstyle.css")
# 1. Main massive glowing center header
st.markdown("<h1 class='cyber-center-title'>Scan&Stop</h1>", unsafe_allow_html=True)

# 2. Secondary engine title header in cyan
st.markdown("<h2 class='cyber-engine-title'> DIGITAL LOAN FRAUD DETECTION ENGINE</h2>", unsafe_allow_html=True)

# 3. Your existing subtext line
st.write("Protecting micro-borrowers from illegal loan apps, data theft, and extortion.")

# Sidebar - Quick Stats
st.sidebar.header("💡 Did You Know?")
st.sidebar.info(
    "According to RBI Digital Lending Guidelines, legitimate lenders are "
    "STRICTLY BANNED from accessing your contacts, gallery, or demanding repayment under 7 days."
)

# Tabs
tab1, tab2, tab3 = st.tabs(["📲 SMS / Message Analyzer", "📋 Risk Score Calculator", "🚨 Emergency Help"])

# --------------------------------------
# TAB 1: SMS / WHATSAPP TEXT ANALYZER 
# --------------------------------------
with tab1:
    st.header("Analyze Suspicious Messages / Links")
    st.write("Paste the SMS, WhatsApp message, or offer link you received below :")
    
    user_text = st.text_area(
        "Enter the message :", 
        placeholder="e.g., Get instant ₹10,000 loan without CIBIL or documentation! Click bit.ly/loan-now"
    )
    
    if st.button("Analyze Text"):
        if user_text:
            text_lower = user_text.lower()
            flags = []

            # 1. FIXED: Dynamic checking for "No Documentation" variations
            if "documentation" in text_lower or "no doc" in text_lower:
                if "without" in text_lower or "no " in text_lower or "zero" in text_lower:
                    flags.append("Claims 'No / Zero Documentation required' (Classic predatory trap).")
            
            # 2. FIXED: Dynamic checking for "No CIBIL" variations
            if "cibil" in text_lower:
                if "no " in text_lower or "without" in text_lower or "zero" in text_lower or "low" in text_lower:
                    flags.append("Offers loans with 'No CIBIL Check' or bypasses credit health score.")

            # 3. Link shortener alerts
            if any(link in text_lower for link in ["bit.ly", "tinyurl", "telegram", "t.me", "wa.me"]):
                flags.append("Uses suspicious/shortened links or chat channels instead of an official website.")

            # 4. Urgency & Guarantee triggers
            if "100%" in text_lower or "guaranteed" in text_lower or "approve" in text_lower:
                flags.append("Promises 'Guaranteed Instant Approval' without vetting.")
            
            if "instant" in text_lower or "urgently" in text_lower or "mins" in text_lower or "minutes" in text_lower:
                flags.append("Creates false urgency (e.g., 'Get loan instantly' to force rash decisions).")

            # Display results
            if flags:
                st.error(f"🚨 **SCAM ALERT: Found {len(flags)} High-Risk Red Flags!**")
                for flag in flags:
                    st.write(f"- ⚠️ {flag}")
                st.markdown(
                    "<div style='background-color:#ffcccc; padding:10px; border-radius:5px; border-left:5px solid #ff0000; color:#990000; font-weight:bold;'>"
                    "⛔ DANGER: This looks like an unverified or illegal loan scam trap. Do not click links, do not provide identity proofs, and block the sender immediately!"
                    "</div>", 
                    unsafe_allow_html=True
                )
            else:
                st.success("✅ No obvious scam patterns detected in text. Proceed with caution and verify the lender name!")
        else:
            st.warning("Please paste a message first.")

# ---------------------------------------------------------
# TAB 2: RISK SCORE CALCULATOR & LENDER CHECK
# ---------------------------------------------------------
with tab2:
    st.header("Assess Loan App Safety")
    st.subheader("1. Permission & Term Check")
    p_contacts = st.checkbox("App asks for Access to Contacts / Phonebook")
    p_gallery = st.checkbox("App asks for Access to Photos / Media / Gallery")
    p_short = st.checkbox("Repayment tenure is LESS than 7 days")
    p_upfront = st.checkbox("Demands an upfront 'processing fee' before disbursing loan")
    
    st.subheader("2. Parent Entity Check")
    lender_name = st.text_input("Parent Company / NBFC Name (as listed in terms):").strip().lower()
    
    legit_nbfcs = ["krazybee", "navi", "stashfin", "cashe", "fibe", "muthoot", "bajaj"]
    
    if st.button("Calculate Safety Score"):
        score = 0
        reasons = []
        
        if p_contacts:
            score += 35
            reasons.append("Contact access is heavily used for contact harassment.")
        if p_gallery:
            score += 35
            reasons.append("Gallery access is used for photo blackmail.")
        if p_short:
            score += 20
            reasons.append("Tenures under 7 days violate standard RBI lending terms.")
        if p_upfront:
            score += 10
            reasons.append("Asking for upfront fees is a classic advance-fee scam.")
            
        if lender_name:
            if any(nbfc in lender_name for nbfc in legit_nbfcs):
                st.success(f"✅ Parent Entity '{lender_name.title()}' matched with RBI-regulated list.")
            else:
                score += 25
                reasons.append("Lender name was NOT found in the registered RBI list.")
                
        st.markdown("---")
        st.metric(label="Overall Risk Score", value=f"{score}% Risk")
        
        if score >= 50:
            st.error("🚨 HIGH RISK / SCAM APP DETECTED!")
            st.write("**Why this app is unsafe:**")
            for r in reasons:
                st.write(f"- {r}")
        elif score > 0:
            st.warning("⚠️ MODERATE RISK: Proceed carefully.")
            for r in reasons:
                st.write(f"- {r}")
        else:
            st.success("✅ LOW RISK: App meets basic safety guidelines.")

# ---------------------------------------------------------
# TAB 3: EMERGENCY ACTION GUIDE
# ---------------------------------------------------------
with tab3:
    st.header("Emergency Action Plan for Victims")
    st.write("If you or someone you know is currently being harassed by a fake loan app, follow these steps immediately:")
    st.markdown("""
    1. **Revoke App Permissions Immediately:**
       * Go to `Android Settings -> Apps -> [Scam App Name] -> Permissions` and turn off **Contacts**, **Storage**, and **SMS**.
    2. **File an Official Cybercrime Complaint:**
       * Call **1930** (National Cyber Crime Helpline, India).
       * Report the incident at **cybercrime.gov.in**.
    3. **Report to RBI Sachet Portal:**
       * Log a formal complaint against illegal lending apps directly at **sachet.rbi.org.in**.
    4. **Secure Your Phone:**
       * Uninstall the app after taking screenshots of transaction history and threatening messages for evidence.
    """)
