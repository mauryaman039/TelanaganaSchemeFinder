import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Telangana Scheme Finder",
    page_icon="🌳",
    layout="wide"
)

# --- Data for Government Schemes (with English, Telugu & Hindi) ---
# This comprehensive list includes all schemes from your provided text.
scheme_data = [
    # --- WOMEN / GENDER-BASED ---
    {
        "name_en": "Maha Lakshmi Scheme (State)",
        "name_te": "మహాలక్ష్మి పథకం (రాష్ట్ర)",
        "name_hi": "महा लक्ष्मी योजना (राज्य)",
        "description_en": "A women’s welfare package providing financial aid of ₹2,500 per month, domestic LPG gas cylinders at ₹500, and free TSRTC bus travel.",
        "description_te": "మహిళల సంక్షేమ ప్యాకేజీ, దీని కింద నెలకు ₹2,500 ఆర్థిక సహాయం, ₹500కే వంటగ్యాస్ సిలిండర్, మరియు మహిళలకు ఉచిత TSRTC బస్సు ప్రయాణం అందిస్తారు.",
        "description_hi": "एक महिला कल्याण पैकेज जो प्रति माह ₹2,500 की वित्तीय सहायता, ₹500 में घरेलू एलपीजी गैस सिलेंडर, और मुफ्त TSRTC बस यात्रा प्रदान करता है।",
        "min_age": 18, "max_age": 150, "max_income": 200000,
        "eligible_castes": ["SC", "ST", "BC", "EBC", "Minority", "OC/General"],
        "eligible_genders": ["Female", "Transgender"],
        "link": "https://www.telangana.gov.in/"
    },
    {
        "name_en": "KCR Kit Scheme (State)",
        "name_te": "కేసీఆర్ కిట్ పథకం (రాష్ట్ర)",
        "name_hi": "केसीआर किट योजना (राज्य)",
        "description_en": "Maternal and child welfare scheme for pregnant women delivering in government hospitals, providing a health kit and cash assistance.",
        "description_te": "ప్రభుత్వ ఆసుపత్రులలో ప్రసవించే గర్భిణీ స్త్రీల కోసం మాతాశిశు సంక్షేమ పథకం, ఆరోగ్య కిట్ మరియు నగదు సహాయం అందిస్తుంది.",
        "description_hi": "सरकारी अस्पतालों में प्रसव कराने वाली गर्भवती महिलाओं के लिए मातृ एवं शिशु कल्याण योजना, जो एक स्वास्थ्य किट और नकद सहायता प्रदान करती है।",
        "min_age": 18, "max_age": 50, "max_income": 99999999,
        "eligible_castes": ["All"],
        "eligible_genders": ["Female"],
        "link": "http://kcrkit.telangana.gov.in"
    },
    {
        "name_en": "Kalyana Lakshmi / Shaadi Mubarak (State)",
        "name_te": "కల్యాణ లక్ష్మి / షాదీ ముబారక్ (రాష్ట్ర)",
        "name_hi": "कल्याण लक्ष्मी / शादी मुबारक (राज्य)",
        "description_en": "Financial assistance of ₹1,00,116 for the marriage of unmarried girls from SC, ST, BC, EBC, and Minority communities.",
        "description_te": "ఎస్సీ, ఎస్టీ, బీసీ, ఈబీసీ మరియు మైనారిటీ వర్గాలకు చెందిన అవివాహిత యువతుల వివాహం కోసం ₹1,00,116 ఆర్థిక సహాయం.",
        "description_hi": "एससी, एसटी, बीसी, ईबीसी और अल्पसंख्यक समुदायों की अविवाहित लड़कियों के विवाह के लिए ₹1,00,116 की वित्तीय सहायता।",
        "min_age": 18, "max_age": 100, "max_income": 200000,
        "eligible_castes": ["SC", "ST", "BC", "EBC", "Minority"],
        "eligible_genders": ["Female"],
        "link": "https://telanganaepass.cgg.gov.in/KalyanaLakshmi.do"
    },
    {
        "name_en": "Arogya Lakshmi Scheme (State)",
        "name_te": "ఆరోగ్య లక్ష్మి పథకం (రాష్ట్ర)",
        "name_hi": "आरोग्य लक्ष्मी योजना (राज्य)",
        "description_en": "Nutrition support for pregnant women, lactating mothers, and children (0-6 years) at Anganwadi centers, providing meals, milk, and eggs.",
        "description_te": "అంగన్‌వాడీ కేంద్రాలలో గర్భిణీ స్త్రీలు, పాలిచ్చే తల్లులు మరియు పిల్లలకు (0-6 సంవత్సరాలు) పౌష్టికాహార మద్దతు, భోజనం, పాలు మరియు గుడ్లు అందిస్తుంది.",
        "description_hi": "आंगनवाड़ी केंद्रों में गर्भवती महिलाओं, स्तनपान कराने वाली माताओं और बच्चों (0-6 वर्ष) के लिए पोषण सहायता, भोजन, दूध और अंडे प्रदान करना।",
        "min_age": 0, "max_age": 50,
        "max_income": 99999999,
        "eligible_castes": ["All"],
        "eligible_genders": ["Female"],
        "link": "http://wdcw.tg.nic.in/Arogya_Lakshmi.html"
    },
    # --- FARMER / AGRICULTURE ---
    {
        "name_en": "Rythu Bandhu / Rythu Bharosa (State)",
        "name_te": "రైతు బంధు / రైతు భరోసా (రాష్ట్ర)",
        "name_hi": "रायथु बंधु / रायथु भरोसा (राज्य)",
        "description_en": "Seasonal investment support scheme for farmers, providing direct credit per acre per season to cover input costs.",
        "description_te": "రైతుల కోసం పెట్టుబడి సహాయ పథకం, దీని కింద పంటల ఖర్చుల కోసం ప్రతి ఎకరానికి ప్రతి సీజన్‌లో నేరుగా ఆర్థిక సహాయం అందిస్తారు.",
        "description_hi": "किसानों के लिए मौसमी निवेश सहायता योजना, जो इनपुट लागतों को कवर करने के लिए प्रति एकड़ प्रति सीजन सीधे क्रेडिट प्रदान करती है।",
        "min_age": 18, "max_age": 150, "max_income": 99999999,
        "eligible_castes": ["All"],
        "eligible_genders": ["Male", "Female", "Transgender"],
        "link": "https://rythubandhu.telangana.gov.in/"
    },
    {
        "name_en": "Rythu Bima (Farmer Insurance) (State)",
        "name_te": "రైతు బీమా (రైతు బీమా) (రాష్ట్ర)",
        "name_hi": "रायथु बीमा (किसान बीमा) (राज्य)",
        "description_en": "Life insurance cover of ₹5 lakh for farmers' families in case of the farmer's death.",
        "description_te": "రైతు మరణించిన సందర్భంలో రైతు కుటుంబాలకు ₹5 లక్షల జీవిత బీమా కవరేజ్.",
        "description_hi": "किसान की मृत्यु की स्थिति में किसानों के परिवारों के लिए ₹5 लाख का जीवन बीमा कवर।",
        "min_age": 18, "max_age": 59, "max_income": 99999999,
        "eligible_castes": ["All"],
        "eligible_genders": ["Male", "Female", "Transgender"],
        "link": "https://rythubandhu.telangana.gov.in/"
    },
    {
        "name_en": "PM-KISAN (Central)",
        "name_te": "పీఎం-కిసాన్ (కేంద్ర)",
        "name_hi": "पीएम-किसान (केंद्रीय)",
        "description_en": "Annual income support of ₹6,000 to small & marginal farmer families. Telangana farmers may receive this in addition to Rythu Bandhu.",
        "description_te": "చిన్న మరియు సన్నకారు రైతు కుటుంబాలకు సంవత్సరానికి ₹6,000 ఆదాయ మద్దతు. రైతు బంధుతో పాటుగా ఈ పథకం కూడా వర్తిస్తుంది.",
        "description_hi": "छोटे और सीमांत किसान परिवारों को ₹6,000 की वार्षिक आय सहायता। तेलंगाना के किसानों को रायथु बंधु के अलावा यह भी मिल सकता है।",
        "min_age": 18, "max_age": 150, "max_income": 99999999,
        "eligible_castes": ["All"],
        "eligible_genders": ["Male", "Female", "Transgender"],
        "link": "https://pmkisan.gov.in/"
    },
    # --- SOCIAL SECURITY / PENSIONS ---
    {
        "name_en": "Aasara Pension Scheme (State)",
        "name_te": "ఆసరా పెన్షన్ పథకం (రాష్ట్ర)",
        "name_hi": "आसरा पेंशन योजना (राज्य)",
        "description_en": "Social security pensions for the elderly (57+), widows, persons with disabilities, single women, weavers, and other vulnerable groups.",
        "description_te": "వృద్ధులు (57+), వితంతువులు, వికలాంగులు, ఒంటరి మహిళలు, నేత కార్మికులు మరియు ఇతర బలహీన వర్గాల కోసం సామాజిక భద్రతా పెన్షన్లు.",
        "description_hi": "बुजुर्गों (57+), विधवाओं, विकलांग व्यक्तियों, एकल महिलाओं, बुनकरों और अन्य कमजोर समूहों के लिए सामाजिक सुरक्षा पेंशन।",
        "min_age": 18, "max_age": 150, "max_income": 200000,
        "eligible_castes": ["All"],
        "eligible_genders": ["Male", "Female", "Transgender"],
        "link": "https://aasara.telangana.gov.in/"
    },
    # --- CASTE-BASED ---
    {
        "name_en": "Dalit Bandhu Scheme (State)",
        "name_te": "దళిత బంధు పథకం (రాష్ట్ర)",
        "name_hi": "दलित बंधु योजना (राज्य)",
        "description_en": "Economic upliftment scheme providing a one-time capital grant of ₹10 lakh per eligible SC family to start an income-generating business.",
        "description_te": "ఎస్సీ కుటుంబాల ఆర్థిక సాధికారత కోసం ఉద్దేశించిన పథకం, దీని కింద ప్రతి అర్హతగల కుటుంబానికి వ్యాపారం ప్రారంభించడానికి ₹10 లక్షల మూలధన సహాయం అందిస్తారు.",
        "description_hi": "एक आर्थिक उत्थान योजना जो एक आय-उत्पादक व्यवसाय शुरू करने के लिए प्रति पात्र एससी परिवार को ₹10 लाख का एकमुश्त पूंजी अनुदान प्रदान करती है।",
        "min_age": 18, "max_age": 60, "max_income": 200000,
        "eligible_castes": ["SC"],
        "eligible_genders": ["Male", "Female", "Transgender"],
        "link": "https://dalitbandhu.telangana.gov.in/"
    },
    # --- STUDENT-FOCUSED ---
    {
        "name_en": "Telangana ePASS Scholarships (State)",
        "name_te": "తెలంగాణ ఇ-పాస్ స్కాలర్‌షిప్‌లు (రాష్ట్ర)",
        "name_hi": "तेलंगाना ई-पास छात्रवृत्ति (राज्य)",
        "description_en": "Fee reimbursement and scholarships for school/college students from SC, ST, BC, EBC, and Minority communities.",
        "description_te": "ఎస్సీ, ఎస్టీ, బీసీ, ఈబీసీ మరియు మైనారిటీ వర్గాల విద్యార్థుల కోసం ఫీజు రీయింబర్స్‌మెంట్ మరియు స్కాలర్‌షిప్‌లు.",
        "description_hi": "एससी, एसटी, बीसी, ईबीसी और अल्पसंख्यक समुदायों के स्कूल/कॉलेज के छात्रों के लिए शुल्क प्रतिपूर्ति और छात्रवृत्ति।",
        "min_age": 6, "max_age": 35, "max_income": 200000,
        "eligible_castes": ["SC", "ST", "BC", "EBC", "Minority"],
        "eligible_genders": ["Male", "Female", "Transgender"],
        "link": "https://telanganaepass.cgg.gov.in/"
    },
    {
        "name_en": "Overseas Scholarship Scheme (State)",
        "name_te": "ఓవర్సీస్ స్కాలర్‌షిప్ పథకం (రాష్ట్ర)",
        "name_hi": "ओवरसीज स्कॉलरशिप योजना (राज्य)",
        "description_en": "Financial assistance for meritorious SC/ST/BC/Minority students to pursue postgraduate or PhD studies abroad.",
        "description_te": "విదేశాలలో పోస్ట్ గ్రాడ్యుయేట్ లేదా పీహెచ్‌డీ చదువుల కోసం ప్రతిభావంతులైన ఎస్సీ/ఎస్టీ/బీసీ/మైనారిటీ విద్యార్థులకు ఆర్థిక సహాయం.",
        "description_hi": "मेधावी एससी/एसटी/बीसी/अल्पसंख्यक छात्रों को विदेश में स्नातकोत्तर या पीएचडी की पढ़ाई करने के लिए वित्तीय सहायता।",
        "min_age": 21, "max_age": 35, "max_income": 500000,
        "eligible_castes": ["SC", "ST", "BC", "Minority"],
        "eligible_genders": ["Male", "Female", "Transgender"],
        "link": "https://telanganaepass.cgg.gov.in/"
    },
    # --- HEALTHCARE ---
    {
        "name_en": "Cheyutha Scheme / Rajiv Aarogyasri (State)",
        "name_te": " చేయూత పథకం / రాజీవ్ ఆరోగ్యశ్రీ (రాష్ట్ర)",
        "name_hi": "चेयुथा योजना / राजीव आरोग्यश्री (राज्य)",
        "description_en": "A health insurance scheme for BPL families providing cashless tertiary medical care up to ₹10 lakh per family per year.",
        "description_te": "పేద కుటుంబాల కోసం ఆరోగ్య బీమా పథకం, దీని కింద సంవత్సరానికి ప్రతి కుటుంబానికి ₹10 లక్షల వరకు నగదు రహిత వైద్య సంరక్షణ అందిస్తారు.",
        "description_hi": "BPL परिवारों के लिए एक स्वास्थ्य बीमा योजना जो प्रति परिवार प्रति वर्ष ₹10 लाख तक की कैशलेस तृतीयक चिकित्सा देखभाल प्रदान करती है।",
        "min_age": 0, "max_age": 150, "max_income": 200000,
        "eligible_castes": ["SC", "ST", "BC", "EBC", "Minority", "OC/General"],
        "eligible_genders": ["Male", "Female", "Transgender"],
        "link": "http://www.aarogyasri.telangana.gov.in/"
    },
    {
        "name_en": "Ayushman Bharat / PM-JAY (Central)",
        "name_te": "ఆయుష్మాన్ భారత్ / పీఎం-జేఏవై (కేంద్ర)",
        "name_hi": "आयुष्मान भारत / पीएम-जय (केंद्रीय)",
        "description_en": "National health insurance providing cashless hospitalization up to ₹5 lakh per family per year for poor and vulnerable families.",
        "description_te": "పేద మరియు బలహీన కుటుంబాల కోసం జాతీయ ఆరోగ్య బీమా, దీని కింద సంవత్సరానికి ప్రతి కుటుంబానికి ₹5 లక్షల వరకు నగదు రహిత హాస్పిటలైజేషన్ అందిస్తారు.",
        "description_hi": "गरीब और कमजोर परिवारों के लिए प्रति परिवार प्रति वर्ष ₹5 लाख तक की कैशलेस अस्पताल में भर्ती सुविधा प्रदान करने वाली राष्ट्रीय स्वास्थ्य बीमा।",
        "min_age": 0, "max_age": 150, "max_income": 200000,
        "eligible_castes": ["All"],
        "eligible_genders": ["Male", "Female", "Transgender"],
        "link": "https://nha.gov.in/"
    },
    # --- HOUSING ---
    {
        "name_en": "Housing for the Poor (2BHK / Indiramma) (State)",
        "name_te": "పేదల కోసం గృహ నిర్మాణం (2BHK / ఇందిరమ్మ) (రాష్ట్ర)",
        "name_hi": "गरीबों के लिए आवास (2BHK / इंदिरम्मा) (राज्य)",
        "description_en": "Public housing initiative to provide '2-bedroom, hall, kitchen' homes or financial assistance to homeless low-income families.",
        "description_te": "నిరుపేద, ఇళ్లులేని కుటుంబాలకు '2-బెడ్‌రూమ్, హాల్, కిచెన్' ఇళ్లు లేదా ఆర్థిక సహాయం అందించే ప్రభుత్వ గృహ పథకం.",
        "description_hi": "बेघर कम आय वाले परिवारों को '2-बेडरूम, हॉल, किचन' घर या वित्तीय सहायता प्रदान करने के लिए सार्वजनिक आवास पहल।",
        "min_age": 18, "max_age": 150, "max_income": 200000,
        "eligible_castes": ["All"],
        "eligible_genders": ["Male", "Female", "Transgender"],
        "link": "https://2bhk.telangana.gov.in/"
    },
    {
        "name_en": "PMAY (Pradhan Mantri Awas Yojana) (Central)",
        "name_te": "PMAY (ప్రధాన్ మంత్రి ఆవాస్ యోజన) (కేంద్ర)",
        "name_hi": "PMAY (प्रधानमंत्री आवास योजना) (केंद्रीय)",
        "description_en": "Provides financial assistance and subsidies on home loans under the 'Housing for All' mission for EWS/LIG families.",
        "description_te": "'అందరికీ ఇళ్లు' మిషన్ కింద EWS/LIG కుటుంబాలకు గృహ రుణాలపై ఆర్థిక సహాయం మరియు సబ్సిడీలు అందిస్తుంది.",
        "description_hi": "'सभी के लिए आवास' मिशन के तहत EWS/LIG परिवारों के लिए गृह ऋण पर वित्तीय सहायता और सब्सिडी प्रदान करता है।",
        "min_age": 18, "max_age": 150, "max_income": 600000,
        "eligible_castes": ["All"],
        "eligible_genders": ["Male", "Female", "Transgender"],
        "link": "https://pmaymis.gov.in/"
    },
    # --- ENTREPRENEURSHIP / SKILL DEVELOPMENT ---
    {
        "name_en": "PMEGP / Mudra / Stand-Up India (Central)",
        "name_te": "పీఎంఈజీపీ / ముద్ర / స్టాండ్-అప్ ఇండియా (కేంద్ర)",
        "name_hi": "पीएमईजीपी / मुद्रा / स्टैंड-अप इंडिया (केंद्रीय)",
        "description_en": "Loans and subsidies to promote micro & small enterprises, with special windows for SC/ST/women entrepreneurs.",
        "description_te": "సూక్ష్మ మరియు చిన్న పరిశ్రమలను ప్రోత్సహించడానికి రుణాలు మరియు సబ్సిడీలు, ఎస్సీ/ఎస్టీ/మహిళా పారిశ్రామికవేత్తలకు ప్రత్యేక అవకాశాలు.",
        "description_hi": "सूक्ष्म और छोटे उद्यमों को बढ़ावा देने के लिए ऋण और सब्सिडी, जिसमें एससी/एसटी/महिला उद्यमियों के लिए विशेष खिड़कियां हैं।",
        "min_age": 18, "max_age": 60, "max_income": 99999999,
        "eligible_castes": ["All"],
        "eligible_genders": ["Male", "Female", "Transgender"],
        "link": "https://www.kviconline.gov.in/pmegpeportal/"
    },
    {
        "name_en": "Skill India / PMKVY (Central)",
        "name_te": "స్కిల్ ఇండియా / PMKVY (కేంద్ర)",
        "name_hi": "स्किल इंडिया / पीएमकेवीवाई (केंद्रीय)",
        "description_en": "Short-term skill training with certification and placement support for unemployed youth in various trades.",
        "description_te": "వివిధ ట్రేడ్‌లలో నిరుద్యోగ యువతకు సర్టిఫికేషన్ మరియు ప్లేస్‌మెంట్ మద్దతుతో స్వల్పకాలిక నైపుణ్య శిక్షణ.",
        "description_hi": "विभिन्न ट्रेडों में बेरोजगार युवाओं के लिए प्रमाणन और प्लेसमेंट सहायता के साथ अल्पकालिक कौशल प्रशिक्षण।",
        "min_age": 15, "max_age": 45, "max_income": 99999999,
        "eligible_castes": ["All"],
        "eligible_genders": ["Male", "Female", "Transgender"],
        "link": "https://www.pmkvyofficial.org/"
    },
    # --- WORKER WELFARE ---
    {
        "name_en": "Welfare Schemes for Registered Workers (State)",
        "name_te": "నమోదిత కార్మికుల కోసం సంక్షేమ పథకాలు (రాష్ట్ర)",
        "name_hi": "पंजीकृत श्रमिकों के लिए कल्याणकारी योजनाएं (राज्य)",
        "description_en": "Sector-specific welfare for registered beedi workers, construction workers, weavers, etc., providing pensions, insurance, and scholarships for children.",
        "description_te": "నమోదిత బీడీ కార్మికులు, నిర్మాణ కార్మికులు, నేత కార్మికులు మొదలైన వారి కోసం రంగాల వారీగా సంక్షేమం, పెన్షన్లు, బీమా మరియు పిల్లలకు స్కాలర్‌షిప్‌లు అందిస్తుంది.",
        "description_hi": "पंजीकृत बीड़ी श्रमिकों, निर्माण श्रमिकों, बुनकरों आदि के लिए क्षेत्र-विशिष्ट कल्याण, पेंशन, बीमा और बच्चों के लिए छात्रवृत्ति प्रदान करना।",
        "min_age": 18, "max_age": 60, "max_income": 200000,
        "eligible_castes": ["All"],
        "eligible_genders": ["Male", "Female", "Transgender"],
        "link": "https://labour.telangana.gov.in/"
    }
]

# --- UI Text Translations ---
ui_texts = {
    "title": {"en": "Telangana Government Scheme Finder", "te": "తెలంగాణ ప్రభుత్వ పథకాల ఫైండర్",
              "hi": "तेलंगाना सरकार योजना खोजक"},
    "subtitle": {"en": "Enter your details to discover the government schemes you might be eligible for.",
                 "te": "మీకు అర్హత ఉన్న ప్రభుత్వ పథకాలను కనుగొనడానికి మీ వివరాలను నమోదు చేయండి.",
                 "hi": "आप जिन सरकारी योजनाओं के लिए पात्र हो सकते हैं, उन्हें खोजने के लिए अपना विवरण दर्ज करें।"},
    "sidebar_header": {"en": "👤 Your Details", "te": "👤 మీ వివరాలు", "hi": "👤 आपका विवरण"},
    "age_label": {"en": "Enter your Age", "te": "మీ వయస్సును నమోదు చేయండి", "hi": "अपनी आयु दर्ज करें"},
    "income_label": {"en": "Enter your Annual Family Income (₹)", "te": "మీ వార్షిక కుటుంబ ఆదాయం (₹) నమోదు చేయండి",
                     "hi": "अपनी वार्षिक पारिवारिक आय (₹) दर्ज करें"},
    "gender_label": {"en": "Select your Gender", "te": "మీ లింగాన్ని ఎంచుకోండి", "hi": "अपना लिंग चुनें"},
    "caste_label": {"en": "Select your Caste/Community", "te": "మీ కులం/వర్గాన్ని ఎంచుకోండి",
                    "hi": "अपनी जाति/समुदाय चुनें"},
    "button_text": {"en": "Find My Schemes", "te": "నా పథకాలను కనుగొనండి", "hi": "मेरी योजनाएं खोजें"},
    "results_header": {"en": "✅ Here are the schemes you may be eligible for:",
                       "te": "✅ మీకు అర్హత ఉన్న పథకాలు ఇక్కడ ఉన్నాయి:",
                       "hi": "✅ यहां वे योजनाएं हैं जिनके लिए आप पात्र हो सकते हैं:"},
    "no_results": {"en": "No schemes found based on your current details. Please try adjusting the filters.",
                   "te": "మీ ప్రస్తుత వివరాల ఆధారంగా ఏ పథకాలు కనుగొనబడలేదు. దయచేసి ఫిల్టర్‌లను సర్దుబాటు చేసి ప్రయత్నించండి.",
                   "hi": "आपके वर्तमान विवरण के आधार पर कोई योजना नहीं मिली। कृपया फ़िल्टर समायोजित करने का प्रयास करें।"},
    "initial_info": {"en": "Please enter your details in the sidebar and click 'Find My Schemes' to see the results.",
                     "te": "దయచేసి సైడ్‌బార్‌లో మీ వివరాలను నమోదు చేసి, ఫలితాలను చూడటానికి 'నా పథకాలను కనుగొనండి' బటన్‌పై క్లిక్ చేయండి.",
                     "hi": "परिणाम देखने के लिए कृपया साइडबार में अपना विवरण दर्ज करें और 'मेरी योजनाएं खोजें' पर क्लिक करें।"},
    "link_text": {"en": "Click Here for More Details", "te": "మరిన్ని వివరాల కోసం ఇక్కడ క్లిక్ చేయండి",
                  "hi": "अधिक विवरण के लिए यहां क्लिक करें"},
    "eligibility_header": {"en": "Eligibility Criteria", "te": "అర్హత ప్రమాణాలు", "hi": "पात्रता मापदंड"},
    "age_range": {"en": "Age", "te": "వయస్సు", "hi": "आयु"},
    "max_income_info": {"en": "Max. Annual Income", "te": "గరిష్ట వార్షిక ఆదాయం", "hi": "अधिकतम वार्षिक आय"},
    "gender_info": {"en": "Gender", "te": "లింగం", "hi": "लिंग"},
    "caste_info": {"en": "Caste", "te": "కులం", "hi": "जाति"}
}

# Initialize session state for language
if 'lang' not in st.session_state:
    st.session_state.lang = 'en'


def set_language():
    lang_map = {"English": "en", "తెలుగు": "te", "हिन्दी": "hi"}
    st.session_state.lang = lang_map[st.session_state.lang_choice]


# --- User Interface ---

# Sidebar for user inputs and language selection
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/92/Telangana_Rashtra_Prabhutvam_logo.png", width=100)
    lang_choice = st.radio(
        "Language / భాష / भाषा",
        ["English", "తెలుగు", "हिन्दी"],
        key='lang_choice',
        on_change=set_language,
        horizontal=True
    )

    lang = st.session_state.lang
    st.header(ui_texts['sidebar_header'][lang])
    age = st.number_input(ui_texts['age_label'][lang], min_value=0, max_value=120, value=25, step=1)
    income = st.number_input(ui_texts['income_label'][lang], min_value=0, value=100000, step=10000)
    gender = st.selectbox(ui_texts['gender_label'][lang], ["Female", "Male", "Transgender"])
    caste = st.selectbox(
        ui_texts['caste_label'][lang],
        ["SC", "ST", "BC", "EBC", "Minority", "OC/General"]
    )
    find_button = st.button(f"**{ui_texts['button_text'][lang]}**", use_container_width=True)

# Main Page Display
lang = st.session_state.lang
st.title(ui_texts['title'][lang])
st.write(ui_texts['subtitle'][lang])
st.markdown("---")

# --- Filtering and Display Logic ---
if find_button:
    st.subheader(ui_texts['results_header'][lang])
    eligible_schemes = []

    for scheme in scheme_data:
        is_age_eligible = scheme["min_age"] <= age <= scheme["max_age"]
        is_income_eligible = income <= scheme["max_income"]
        is_gender_eligible = "All" in scheme["eligible_genders"] or gender in scheme["eligible_genders"]
        is_caste_eligible = "All" in scheme["eligible_castes"] or caste in scheme["eligible_castes"]

        if is_age_eligible and is_income_eligible and is_gender_eligible and is_caste_eligible:
            eligible_schemes.append(scheme)

    if eligible_schemes:
        # Sort schemes alphabetically by name for consistent ordering
        eligible_schemes.sort(key=lambda x: x[f'name_{lang}'])
        for scheme in eligible_schemes:
            with st.expander(f"**{scheme[f'name_{lang}']}**"):
                st.write(scheme[f'description_{lang}'])
                st.markdown(f"**🔗 [{ui_texts['link_text'][lang]}]({scheme['link']})**", unsafe_allow_html=True)

                st.markdown(f"**{ui_texts['eligibility_header'][lang]}:**")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**{ui_texts['age_range'][lang]}:** {scheme['min_age']} - {scheme['max_age']}")
                    st.markdown(f"**{ui_texts['gender_info'][lang]}:** {', '.join(scheme['eligible_genders'])}")
                with col2:
                    st.markdown(f"**{ui_texts['max_income_info'][lang]}:** ₹{scheme['max_income']:,}")
                    st.markdown(f"**{ui_texts['caste_info'][lang]}:** {', '.join(scheme['eligible_castes'])}")

    else:
        st.warning(ui_texts['no_results'][lang])
else:
    st.info(ui_texts['initial_info'][lang])

