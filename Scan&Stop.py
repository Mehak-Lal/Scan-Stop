import streamlit as st 
 
st.set_page_config(page_title="SCAN&STOP - RBI Scam Detector", layout="wide") 


# ---------------------------------------------------------
# LANGUAGE SELECTION
# ---------------------------------------------------------
st.sidebar.header("🌐 Language / भाषा")

language = st.sidebar.selectbox(
    "Preferred Language / पसंदीदा भाषा",
    ["English", "हिंदी"]
)


# ---------------------------------------------------------
# TRANSLATIONS
# ---------------------------------------------------------
translations = {
    "English": {
        "did_you_know": "💡 Did You Know?",
        "did_you_know_text": (
            "According to RBI Digital Lending Guidelines, legitimate lenders are "
            "STRICTLY BANNED from accessing your contacts, gallery, or demanding "
            "repayment under 7 days."
        ),

        "engine_title": "DIGITAL LOAN FRAUD DETECTION ENGINE",
        "description": (
            "Protecting micro-borrowers from illegal loan apps, data theft, and extortion."
        ),

        "tab_sms": "📲 SMS / Message Analyzer",
        "tab_risk": "📋 Risk Score Calculator",
        "tab_help": "🚨 Emergency Help",

        # Tab 1
        "analyze_title": "Analyze Suspicious Messages / Links",
        "analyze_description": (
            "Paste the SMS, WhatsApp message, or offer link you received below:"
        ),
        "enter_message": "Enter the message :",
        "analyze_button": "Analyze Text",
        "paste_first": "Please paste a message first.",

        "documentation_flag": (
            "Claims 'No / Zero Documentation required' "
            "(Classic predatory trap)."
        ),
        "cibil_flag": (
            "Offers loans with 'No CIBIL Check' or bypasses credit health score."
        ),
        "link_flag": (
            "Uses suspicious/shortened links or chat channels instead of "
            "an official website."
        ),
        "guaranteed_flag": (
            "Promises 'Guaranteed Instant Approval' without vetting."
        ),
        "urgency_flag": (
            "Creates false urgency (e.g., 'Get loan instantly' "
            "to force rash decisions)."
        ),

        "scam_alert": "🚨 SCAM ALERT: Found {count} High-Risk Red Flags!",
        "danger": (
            "⛔ DANGER: This looks like an unverified or illegal loan scam trap. "
            "Do not click links, do not provide identity proofs, and block the sender immediately!"
        ),
        "safe_text": (
            "✅ No obvious scam patterns detected in text. "
            "Proceed with caution and verify the lender name!"
        ),

        # Tab 2
        "risk_title": "Assess Loan App Safety",
        "permission_title": "1. Permission & Term Check",
        "contacts": "App asks for Access to Contacts / Phonebook",
        "gallery": "App asks for Access to Photos / Media / Gallery",
        "short": "Repayment tenure is LESS than 7 days",
        "upfront": (
            "Demands an upfront 'processing fee' before disbursing loan"
        ),

        "parent_title": "2. Parent Entity Check",
        "lender_name": (
            "Parent Company / NBFC Name (as listed in terms):"
        ),
        "calculate": "Calculate Safety Score",

        "contact_reason": (
            "Contact access is heavily used for contact harassment."
        ),
        "gallery_reason": (
            "Gallery access is used for photo blackmail."
        ),
        "short_reason": (
            "Tenures under 7 days violate standard RBI lending terms."
        ),
        "upfront_reason": (
            "Asking for upfront fees is a classic advance-fee scam."
        ),
        "not_found_reason": (
            "Lender name was NOT found in the registered RBI list."
        ),

        "matched": (
            "✅ Parent Entity '{name}' matched with RBI-regulated list."
        ),
        "risk_score": "Overall Risk Score",
        "high_risk": "🚨 HIGH RISK / SCAM APP DETECTED!",
        "unsafe": "**Why this app is unsafe:**",
        "moderate": "⚠️ MODERATE RISK: Proceed carefully.",
        "low": "✅ LOW RISK: App meets basic safety guidelines.",

        # Tab 3
        "emergency_title": "Emergency Action Plan for Victims",
        "emergency_description": (
            "If you or someone you know is currently being harassed by a fake "
            "loan app, follow these steps immediately:"
        ),

        "step1_title": "1. Revoke App Permissions Immediately:",
        "step1_text": (
            "Go to `Android Settings -> Apps -> [Scam App Name] -> Permissions` "
            "and turn off **Contacts**, **Storage**, and **SMS**."
        ),

        "step2_title": "2. File an Official Cybercrime Complaint:",
        "step2_text": (
            "Call **1930** (National Cyber Crime Helpline, India).  \n"
            "Report the incident at **cybercrime.gov.in**."
        ),

        "step3_title": "3. Report to RBI Sachet Portal:",
        "step3_text": (
            "Log a formal complaint against illegal lending apps directly at "
            "**sachet.rbi.org.in**."
        ),

        "step4_title": "4. Secure Your Phone:",
        "step4_text": (
            "Uninstall the app after taking screenshots of transaction history "
            "and threatening messages for evidence."
        ),
    },


    "हिंदी": {
        "did_you_know": "💡 क्या आपको पता है?",
        "did_you_know_text": (
            "RBI डिजिटल लेंडिंग गाइडलाइंस (RBI Digital Lending Guidelines) के अनुसार, वैध ऋणदाताओं (legitimate lenders) पर आपके कॉन्टैक्ट्स, गैलरी तक पहुँचने, या 7 दिनों से कम समय के भीतर पुनर्भुगतान (repayment) की मांग करने पर पूरी तरह से प्रतिबंध है।"
        ),

        "engine_title": "डिजिटल लोन धोखाधड़ी पहचान इंजन",
        "description": (
            "अवैध लोन ऐप्स, डेटा चोरी और उत्पीड़न से छोटे उधारकर्ताओं की सुरक्षा।"
        ),

        "tab_sms": "📲 SMS / संदेश विश्लेषक",
        "tab_risk": "📋 जोखिम स्कोर कैलकुलेटर",
        "tab_help": "🚨 आपातकालीन सहायता",

        # Tab 1
        "analyze_title": "संदिग्ध संदेश / लिंक की जाँच करें",
        "analyze_description": (
            "नीचे प्राप्त SMS, WhatsApp संदेश या लोन ऑफर लिंक पेस्ट करें:"
        ),
        "enter_message": "संदेश दर्ज करें :",
        "analyze_button": "संदेश का विश्लेषण करें",
        "paste_first": "कृपया पहले कोई संदेश पेस्ट करें।",

        "documentation_flag": (
            "'बिना / शून्य दस्तावेज़' की आवश्यकता होने का दावा "
            "(आम तौर पर इस्तेमाल किया जाने वाला धोखाधड़ी का तरीका)।"
        ),
        "cibil_flag": (
            "'बिना CIBIL जाँच' के लोन देने का दावा या credit score की "
            "जाँच को bypass करना।"
        ),
        "link_flag": (
            "आधिकारिक वेबसाइट के बजाय संदिग्ध / shortened links या "
            "chat channels का इस्तेमाल किया गया है।"
        ),
        "guaranteed_flag": (
            "बिना उचित जाँच के 'Guaranteed Instant Approval' का वादा।"
        ),
        "urgency_flag": (
            "झूठी जल्दी पैदा की जाती है (जैसे 'तुरंत लोन पाएं') ताकि "
            "आप बिना सोचे निर्णय लें।"
        ),

        "scam_alert": "🚨 SCAM ALERT: {count} High-Risk Red Flags मिले!",
        "danger": (
            "⛔ खतरा: यह एक अप्रमाणित या अवैध लोन scam जैसा दिखता है। "
            "लिंक पर क्लिक न करें, पहचान से जुड़े दस्तावेज़ साझा न करें "
            "और sender को तुरंत block करें!"
        ),
        "safe_text": (
            "✅ संदेश में कोई स्पष्ट scam pattern नहीं मिला। "
            "फिर भी सावधानी बरतें और lender के नाम की पुष्टि करें!"
        ),

        # Tab 2
        "risk_title": "लोन ऐप की सुरक्षा जाँचें",
        "permission_title": "1. परमिशन और शर्तों की जाँच",
        "contacts": "ऐप Contacts / Phonebook की अनुमति माँगता है",
        "gallery": "ऐप Photos / Media / Gallery की अनुमति माँगता है",
        "short": "लोन चुकाने की अवधि 7 दिनों से कम है",
        "upfront": (
            "लोन देने से पहले 'processing fee' की मांग करता है"
        ),

        "parent_title": "2. Parent Entity की जाँच",
        "lender_name": (
            "Parent Company / NBFC का नाम (terms में दिया गया):"
        ),
        "calculate": "सुरक्षा स्कोर निकालें",

        "contact_reason": (
            "Contacts तक पहुँच का इस्तेमाल contact harassment के लिए किया जा सकता है।"
        ),
        "gallery_reason": (
            "Gallery तक पहुँच का इस्तेमाल photo blackmail के लिए किया जा सकता है।"
        ),
        "short_reason": (
            "7 दिनों से कम की repayment अवधि सामान्य RBI lending terms के विरुद्ध है।"
        ),
        "upfront_reason": (
            "पहले से fee माँगना एक सामान्य advance-fee scam का संकेत है।"
        ),
        "not_found_reason": (
            "Lender का नाम registered RBI list में नहीं मिला।"
        ),

        "matched": (
            "✅ Parent Entity '{name}' RBI-regulated list से match हुई।"
        ),
        "risk_score": "कुल जोखिम स्कोर",
        "high_risk": "🚨 HIGH RISK / SCAM APP DETECTED!",
        "unsafe": "**यह ऐप असुरक्षित क्यों है:**",
        "moderate": "⚠️ MODERATE RISK: सावधानी से आगे बढ़ें।",
        "low": "✅ LOW RISK: ऐप basic safety guidelines को पूरा करता है।",

        # Tab 3
        "emergency_title": "पीड़ितों के लिए आपातकालीन कार्य योजना",
        "emergency_description": (
            "अगर आप या आपका कोई परिचित किसी नकली लोन ऐप से परेशान किया जा रहा है, "
            "तो तुरंत ये कदम उठाएँ:"
        ),

        "step1_title": "1. तुरंत App Permissions बंद करें:",
        "step1_text": (
            "`Android Settings -> Apps -> [Scam App Name] -> Permissions` "
            "पर जाएँ और **Contacts**, **Storage** और **SMS** की permissions बंद करें।"
        ),

        "step2_title": "2. Official Cybercrime Complaint दर्ज करें:",
        "step2_text": (
            "**1930** (National Cyber Crime Helpline, India) पर कॉल करें।  \n"
            "**cybercrime.gov.in** पर घटना की report करें।"
        ),

        "step3_title": "3. RBI Sachet Portal पर Report करें:",
        "step3_text": (
            "अवैध lending apps के खिलाफ **sachet.rbi.org.in** पर "
            "formal complaint दर्ज करें।"
        ),

        "step4_title": "4. अपना Phone सुरक्षित करें:",
        "step4_text": (
            "Evidence के लिए transaction history और threatening messages "
            "के screenshots लेने के बाद app को uninstall करें।"
        ),
    }
}


# Select translations for current language
text = translations[language]


# ---------------------------------------------------------
# CSS
# ---------------------------------------------------------
def load_css(filename): 
    try: 
        with open(filename, "r") as f: 
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)       
    except FileNotFoundError: 
        pass # Prevents crash if CSS file is missing locally


load_css("scanstyle.css")


# ---------------------------------------------------------
# MAIN HEADER
# ---------------------------------------------------------

# 1. Main massive glowing center header 
st.markdown(
    "<h1 class='cyber-center-title'>Scan&Stop</h1>",
    unsafe_allow_html=True
)


# 2. Secondary engine title header in cyan 
st.markdown(
    f"<h2 class='cyber-engine-title'>{text['engine_title']}</h2>",
    unsafe_allow_html=True
)


# 3. Your existing subtext line 
st.write(text["description"])


# ---------------------------------------------------------
# SIDEBAR - QUICK STATS
# ---------------------------------------------------------

st.sidebar.header(text["did_you_know"])

st.sidebar.info(
    text["did_you_know_text"]
)


# ---------------------------------------------------------
# TABS
# ---------------------------------------------------------

tab1, tab2, tab3 = st.tabs([
    text["tab_sms"],
    text["tab_risk"],
    text["tab_help"]
])


# --------------------------------------
# TAB 1: SMS / WHATSAPP TEXT ANALYZER
# --------------------------------------

with tab1:
    st.header(text["analyze_title"])
    st.write(text["analyze_description"])
     
    user_text = st.text_area(
        text["enter_message"],  
        placeholder="e.g., Get instant ₹10,000 loan without CIBIL or documentation! Click bit.ly/loan-now"
    )
     
    if st.button(text["analyze_button"]): 
        if user_text: 
            text_lower = user_text.lower() 
            flags = [] 
 
            # 1. FIXED: Dynamic checking for "No Documentation" variations 
            if "documentation" in text_lower or "no doc" in text_lower: 
                if "without" in text_lower or "no " in text_lower or "zero" in text_lower: 
                    flags.append(text["documentation_flag"])
             
            # 2. FIXED: Dynamic checking for "No CIBIL" variations 
            if "cibil" in text_lower: 
                if "no " in text_lower or "without" in text_lower or "zero" in text_lower or "low" in text_lower: 
                    flags.append(text["cibil_flag"])
 
            # 3. Link shortener alerts 
            if any(link in text_lower for link in ["bit.ly", "tinyurl", "telegram", "t.me", "wa.me"]): 
                flags.append(text["link_flag"])
 
            # 4. Urgency & Guarantee triggers 
            if "100%" in text_lower or "guaranteed" in text_lower or "approve" in text_lower: 
                flags.append(text["guaranteed_flag"])
             
            if "instant" in text_lower or "urgently" in text_lower or "mins" in text_lower or "minutes" in text_lower: 
                flags.append(text["urgency_flag"])
 
            # Display results 
            if flags: 
                st.error(
                    text["scam_alert"].format(count=len(flags))
                )

                for flag in flags: 
                    st.write(f"- ⚠️ {flag}") 

                st.markdown( 
                    "<div style='background-color:#ffcccc; padding:10px; border-radius:5px; border-left:5px solid #ff0000; color:#990000; font-weight:bold;'>" 
                    + text["danger"] +
                    "</div>",  
                    unsafe_allow_html=True 
                ) 
            else: 
                st.success(text["safe_text"]) 
        else: 
            st.warning(text["paste_first"])


# ---------------------------------------------------------
# TAB 2: RISK SCORE CALCULATOR & LENDER CHECK
# ---------------------------------------------------------

with tab2:
    st.header(text["risk_title"])
    st.subheader(text["permission_title"])

    p_contacts = st.checkbox(text["contacts"])
    p_gallery = st.checkbox(text["gallery"])
    p_short = st.checkbox(text["short"])
    p_upfront = st.checkbox(text["upfront"])
     
    st.subheader(text["parent_title"])

    lender_name = st.text_input(
        text["lender_name"]
    ).strip().lower()
     
    legit_nbfcs = [
        "krazybee",
        "navi",
        "stashfin",
        "cashe",
        "fibe",
        "muthoot",
        "bajaj"
    ]
     
    if st.button(text["calculate"]): 
        score = 0 
        reasons = [] 
         
        if p_contacts: 
            score += 35 
            reasons.append(text["contact_reason"])

        if p_gallery: 
            score += 35 
            reasons.append(text["gallery_reason"])

        if p_short: 
            score += 20 
            reasons.append(text["short_reason"])

        if p_upfront: 
            score += 10 
            reasons.append(text["upfront_reason"])
             
        if lender_name: 
            if any(nbfc in lender_name for nbfc in legit_nbfcs): 
                st.success(
                    text["matched"].format(name=lender_name.title())
                )
            else: 
                score += 25 
                reasons.append(text["not_found_reason"])
                 
        st.markdown("---")

        st.metric(
            label=text["risk_score"],
            value=f"{score}% Risk"
        )
         
        if score >= 50: 
            st.error(text["high_risk"])

            st.write(text["unsafe"])

            for r in reasons: 
                st.write(f"- {r}")

        elif score > 0: 
            st.warning(text["moderate"])

            for r in reasons: 
                st.write(f"- {r}")

        else: 
            st.success(text["low"])


# ---------------------------------------------------------
# TAB 3: EMERGENCY ACTION GUIDE
# ---------------------------------------------------------

with tab3:
    st.header(text["emergency_title"])

    st.write(text["emergency_description"])

    st.markdown(
        f"""
        1. **{text["step1_title"].split(". ", 1)[1]}**
           * {text["step1_text"]}

        2. **{text["step2_title"].split(". ", 1)[1]}**
           * {text["step2_text"]}

        3. **{text["step3_title"].split(". ", 1)[1]}**
           * {text["step3_text"]}

        4. **{text["step4_title"].split(". ", 1)[1]}**
           * {text["step4_text"]}
        """
    )
